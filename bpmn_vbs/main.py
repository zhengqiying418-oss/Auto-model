import os
import sys
import glob
import ast
import queue
import shutil
import inspect
import traceback
import threading
import importlib.util
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.scrolledtext import ScrolledText

APP_TITLE = "BPMN to Arena Converter"
# BPMN → 补充 sourceRef/targetRef → 精简 BPMN → XML 转 JSON → 网关处理 → 参数提取 → 参数写入 JSON → 生成 VBS → 自动调用 Arena

def app_dir():
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


def find_module_file(*base_names):
    """Find exact or downloaded-with-suffix variants, e.g. gateway.py / gateway(8).py."""
    folder = app_dir()
    for base in base_names:
        exact = os.path.join(folder, f"{base}.py")
        if os.path.isfile(exact):
            return exact

    candidates = []
    for base in base_names:
        candidates.extend(glob.glob(os.path.join(folder, f"{base}*.py")))

    # Don't accidentally select this GUI file.
    this_file = os.path.abspath(__file__)
    candidates = [p for p in candidates if os.path.abspath(p) != this_file]
    if not candidates:
        raise FileNotFoundError(
            f"Cannot find module file for: {', '.join(base_names)}\n"
            f"Please place the Python subfiles in the same directory as main.py."
        )

    candidates.sort(key=lambda p: (len(os.path.basename(p)), os.path.basename(p)))
    return candidates[0]


def load_module_from_path(alias, path):
    spec = importlib.util.spec_from_file_location(alias, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_resource_module_safely(path):
    with open(path, "r", encoding="utf-8-sig") as f:
        source = f.read()

    tree = ast.parse(source, filename=path)
    allowed = []
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom, ast.FunctionDef,
                             ast.AsyncFunctionDef, ast.ClassDef)):
            allowed.append(node)

    safe_tree = ast.Module(body=allowed, type_ignores=[])
    ast.fix_missing_locations(safe_tree)

    import types
    module = types.ModuleType("resource_runtime")
    module.__file__ = path
    exec(compile(safe_tree, path, "exec"), module.__dict__)
    return module


def process_sequence_flows_portable(input_file, output_dir):
    tree = ET.parse(input_file)
    root = tree.getroot()
    ns = "{http://www.omg.org/spec/BPMN/20100524/MODEL}"

    flows = root.findall(f".//{ns}sequenceFlow")
    if not flows:
        # Fallback for BPMN files with a different/default namespace handling.
        flows = [elem for elem in root.iter() if elem.tag.endswith("sequenceFlow")]

    for sequence_flow in flows:
        source_ref = sequence_flow.get("sourceRef")
        target_ref = sequence_flow.get("targetRef")
        if not source_ref or not target_ref:
            continue

        source_node = root.find(f".//*[@id='{source_ref}']")
        target_node = root.find(f".//*[@id='{target_ref}']")

        if source_node is None:
            raise ValueError(f"Source node with ID {source_ref} not found.")
        if target_node is None:
            raise ValueError(f"Target node with ID {target_ref} not found.")

        targets = [x.strip() for x in source_node.get("targetRef", "").split(",") if x.strip()]
        if target_ref not in targets:
            targets.append(target_ref)
        source_node.set("targetRef", ",".join(targets))

        sources = [x.strip() for x in target_node.get("sourceRef", "").split(",") if x.strip()]
        if source_ref not in sources:
            sources.append(source_ref)
        target_node.set("sourceRef", ",".join(sources))

    os.makedirs(output_dir, exist_ok=True)
    base = os.path.splitext(os.path.basename(input_file))[0]
    output_file = os.path.join(output_dir, f"{base}_connected.xml")
    tree.write(output_file, encoding="utf-8", xml_declaration=True)
    return output_file



class QueueWriter:
    def __init__(self, q):
        self.q = q

    def write(self, text):
        if text:
            self.q.put(text)

    def flush(self):
        pass



class BPMNToArenaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        self.geometry("920x680")
        self.minsize(820, 600)

        self.log_queue = queue.Queue()
        self.worker = None

        self.bpmn_var = tk.StringVar()
        self.log_var = tk.StringVar()
        self.output_var = tk.StringVar()
        self.status_var = tk.StringVar(value="Ready")
        self.progress_var = tk.DoubleVar(value=0)

        self._build_ui()
        self.after(100, self._drain_log_queue)

    def _build_ui(self):
        outer = ttk.Frame(self, padding=14)
        outer.pack(fill="both", expand=True)
        outer.columnconfigure(1, weight=1)
        outer.rowconfigure(6, weight=1)

        ttk.Label(outer, text="BPMN → Arena automatic converter",
                  font=("Segoe UI", 16, "bold")).grid(
            row=0, column=0, columnspan=3, sticky="w", pady=(0, 12)
        )

        self._file_row(outer, 1, "BPMN file (.bpmn):", self.bpmn_var,
                       self._browse_bpmn)
        self._file_row(outer, 2, "Event log (.xlsx):", self.log_var,
                       self._browse_log)
        self._file_row(outer, 3, "Output folder:", self.output_var,
                       self._browse_output)

        action_frame = ttk.Frame(outer)
        action_frame.grid(row=4, column=0, columnspan=3, sticky="ew", pady=(12, 8))
        action_frame.columnconfigure(0, weight=1)

        self.convert_btn = ttk.Button(
            action_frame,
            text="Convert and run Arena model",
            command=self.start_conversion
        )
        self.convert_btn.grid(row=0, column=0, sticky="ew", ipady=7)

        ttk.Progressbar(
            outer,
            variable=self.progress_var,
            maximum=100,
            mode="determinate"
        ).grid(row=5, column=0, columnspan=3, sticky="ew", pady=(0, 8))

        log_frame = ttk.LabelFrame(outer, text="Processing log", padding=8)
        log_frame.grid(row=6, column=0, columnspan=3, sticky="nsew")
        log_frame.rowconfigure(0, weight=1)
        log_frame.columnconfigure(0, weight=1)

        self.log_text = ScrolledText(
            log_frame,
            wrap="word",
            height=20,
            font=("Consolas", 10),
            state="disabled"
        )
        self.log_text.grid(row=0, column=0, sticky="nsew")

        status = ttk.Label(outer, textvariable=self.status_var, anchor="w")
        status.grid(row=7, column=0, columnspan=3, sticky="ew", pady=(8, 0))

    def _file_row(self, parent, row, label, variable, command):
        ttk.Label(parent, text=label).grid(row=row, column=0, sticky="w", pady=5)
        ttk.Entry(parent, textvariable=variable).grid(
            row=row, column=1, sticky="ew", padx=(8, 8), pady=5
        )
        ttk.Button(parent, text="Browse...", command=command).grid(
            row=row, column=2, sticky="ew", pady=5
        )

    def _browse_bpmn(self):
        path = filedialog.askopenfilename(
            title="Select BPMN file",
            filetypes=[("BPMN files", "*.bpmn"), ("XML files", "*.xml"), ("All files", "*.*")]
        )
        if path:
            self.bpmn_var.set(path)
            if not self.output_var.get():
                self.output_var.set(os.path.join(os.path.dirname(path), "arena_output"))

    def _browse_log(self):
        path = filedialog.askopenfilename(
            title="Select event log",
            filetypes=[("Excel files", "*.xlsx"), ("Excel 97-2003", "*.xls"), ("All files", "*.*")]
        )
        if path:
            self.log_var.set(path)

    def _browse_output(self):
        path = filedialog.askdirectory(title="Select output folder")
        if path:
            self.output_var.set(path)

    def _set_status(self, text, progress=None):
        self.status_var.set(text)
        if progress is not None:
            self.progress_var.set(progress)

    def _append_log(self, text):
        self.log_text.configure(state="normal")
        self.log_text.insert("end", text)
        self.log_text.see("end")
        self.log_text.configure(state="disabled")

    def _drain_log_queue(self):
        try:
            while True:
                msg = self.log_queue.get_nowait()
                if isinstance(msg, tuple):
                    kind = msg[0]
                    if kind == "status":
                        _, text, progress = msg
                        self._set_status(text, progress)
                    elif kind == "done":
                        _, output_dir, vbs_file = msg
                        self.convert_btn.configure(state="normal")
                        self._set_status("Completed", 100)
                        messagebox.showinfo(
                            "Success",
                            "Conversion completed and Arena launch command was executed.\n\n"
                            f"Output folder:\n{output_dir}\n\n"
                            f"Generated VBS:\n{vbs_file}"
                        )
                    elif kind == "error":
                        _, message = msg
                        self.convert_btn.configure(state="normal")
                        self._set_status("Failed", 0)
                        messagebox.showerror("Conversion failed", message)
                else:
                    self._append_log(str(msg))
        except queue.Empty:
            pass
        self.after(100, self._drain_log_queue)

    def _validate_inputs(self):
        bpmn = self.bpmn_var.get().strip()
        event_log = self.log_var.get().strip()
        output_dir = self.output_var.get().strip()

        if not bpmn or not os.path.isfile(bpmn):
            raise ValueError("Please select a valid .bpmn file.")

        if not event_log:
            folder = os.path.dirname(bpmn)
            stem = os.path.splitext(os.path.basename(bpmn))[0]
            stem_candidates = [
                stem,
                stem.replace("_bpmn", ""),
                stem.replace("-bpmn", ""),
                stem.replace(" bpmn", ""),
            ]
            candidates = []
            for candidate_stem in stem_candidates:
                for ext in (".xlsx", ".xls"):
                    candidate = os.path.join(folder, candidate_stem + ext)
                    if os.path.isfile(candidate):
                        candidates.append(candidate)
            if not candidates:
                candidates = sorted(
                    glob.glob(os.path.join(folder, "*.xlsx")) +
                    glob.glob(os.path.join(folder, "*.xls"))
                )
            if len(candidates) == 1:
                event_log = candidates[0]
                self.log_var.set(event_log)
            elif len(candidates) > 1:
                # Prefer an exact/similar basename if available.
                event_log = candidates[0]
                self.log_var.set(event_log)
            else:
                raise ValueError(
                    "No event-log Excel file was found next to the BPMN file. "
                    "Please select the event log once; afterward conversion is one click."
                )

        if not os.path.isfile(event_log):
            raise ValueError("Please select a valid event-log Excel file.")
        if not output_dir:
            output_dir = os.path.join(os.path.dirname(bpmn), "arena_output")
            self.output_var.set(output_dir)

        return bpmn, event_log, output_dir

    def start_conversion(self):
        if self.worker and self.worker.is_alive():
            return

        try:
            bpmn, event_log, output_dir = self._validate_inputs()
        except Exception as e:
            messagebox.showerror("Input error", str(e))
            return

        self.log_text.configure(state="normal")
        self.log_text.delete("1.0", "end")
        self.log_text.configure(state="disabled")
        self.progress_var.set(0)
        self.convert_btn.configure(state="disabled")

        self.worker = threading.Thread(
            target=self._convert_worker,
            args=(bpmn, event_log, output_dir),
            daemon=True
        )
        self.worker.start()

    def _convert_worker(self, bpmn_file, event_log_file, output_dir):
        old_stdout, old_stderr = sys.stdout, sys.stderr
        writer = QueueWriter(self.log_queue)
        sys.stdout = writer
        sys.stderr = writer

        try:
            os.makedirs(output_dir, exist_ok=True)

            self.log_queue.put(("status", "Loading conversion modules...", 5))

            delflow_path = find_module_file("delflow")
            transjson_path = find_module_file("transjson")
            gateway_path = find_module_file("gateway")
            parameter_path = find_module_file("parameter")
            resource_path = find_module_file("resource")
            converter_path = find_module_file("converter_connect_shape", "converter")

            delflow = load_module_from_path("delflow_runtime", delflow_path)
            transjson = load_module_from_path("transjson_runtime", transjson_path)
            gateway = load_module_from_path("gateway_runtime", gateway_path)
            parameter = load_module_from_path("parameter_runtime", parameter_path)
            resource = load_resource_module_safely(resource_path)
            converter = load_module_from_path("converter_runtime", converter_path)

            required = [
                (delflow, "extract_elements_with_attributes"),
                (transjson, "xml_to_json"),
                (gateway, "process_gateway"),
                (parameter, "generate_simulation_parameters"),
                (resource, "final_to_json"),
                (converter, "generate_vbs"),
            ]
            for module, fn in required:
                if not hasattr(module, fn):
                    raise AttributeError(f"{os.path.basename(module.__file__)} is missing function: {fn}()")

            print("=== BPMN → ARENA PIPELINE ===")
            print("BPMN:", bpmn_file)
            print("Event log:", event_log_file)
            print("Output:", output_dir)
            print()

            # 1. Add sourceRef / targetRef to BPMN nodes.
            self.log_queue.put(("status", "1/7 Building BPMN node connections...", 12))
            enhanced_file = process_sequence_flows_portable(bpmn_file, output_dir)
            print("[1/7] Connected BPMN:", enhanced_file)

            # 2. Remove irrelevant BPMN elements.
            self.log_queue.put(("status", "2/7 Simplifying BPMN...", 24))
            light_file = delflow.extract_elements_with_attributes(enhanced_file)
            if not light_file or not os.path.isfile(light_file):
                raise RuntimeError("delflow did not produce a valid light XML file.")
            print("[2/7] Light BPMN:", light_file)

            # 3. XML → JSON.
            self.log_queue.put(("status", "3/7 Converting BPMN XML to JSON...", 36))
            json_file = transjson.xml_to_json(light_file)
            if not json_file or not os.path.isfile(json_file):
                raise RuntimeError("transjson did not produce a valid JSON file.")
            print("[3/7] JSON:", json_file)

            # 4. Gateway normalization.
            self.log_queue.put(("status", "4/7 Processing gateways...", 48))
            json_gateway = gateway.process_gateway(json_file)
            if not json_gateway or not os.path.isfile(json_gateway):
                raise RuntimeError("gateway processing did not produce a valid JSON file.")
            print("[4/7] Gateway JSON:", json_gateway)

            # 5. Mine DES parameters from event log.
            self.log_queue.put(("status", "5/7 Mining simulation parameters...", 63))
            parameter_file = os.path.join(output_dir, "parameters.xlsx")
            parameter.generate_simulation_parameters(
                input_file=event_log_file,
                bpmn_file=bpmn_file,
                output_file=parameter_file
            )
            if not os.path.isfile(parameter_file):
                raise RuntimeError("parameter.py did not produce parameters.xlsx.")
            print("[5/7] Parameters:", parameter_file)

            # 6. Inject parameters into normalized JSON.
            self.log_queue.put(("status", "6/7 Merging parameters into model JSON...", 78))
            final_json = resource.final_to_json(json_gateway, parameter_file)
            if not final_json or not os.path.isfile(final_json):
                raise RuntimeError("resource.py did not produce the parameterized JSON file.")
            print("[6/7] Parameterized JSON:", final_json)

            # 7. Generate VBS and launch Arena.
            self.log_queue.put(("status", "7/7 Generating and launching Arena model...", 92))
            converter.generate_vbs(final_json, parameter_file)
            vbs_file = os.path.splitext(final_json)[0] + ".vbs"
            if not os.path.isfile(vbs_file):
                raise RuntimeError("converter did not produce the VBS file.")
            print("[7/7] VBS:", vbs_file)
            print("Pipeline finished.")

            self.log_queue.put(("done", output_dir, vbs_file))

        except Exception as e:
            traceback.print_exc()
            self.log_queue.put(("error", f"{type(e).__name__}: {e}"))
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr


if __name__ == "__main__":
    app = BPMNToArenaApp()
    app.mainloop()
