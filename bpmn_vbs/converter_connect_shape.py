import os
import json
import subprocess
import pandas as pd


def clean_name(name):
    if not name:
        return "Node"

    for c in [" ", "-", "'", ",", "(", ")", "/"]:
        name = str(name).replace(c, "_")

    return name
def clean_display_name(name):
    if not name:
        return ""

    name = str(name)

    # 统一单双撇号
    name = name.replace("’", "'")
    name = name.replace("‘", "'")

    # 去除撇号
    name = name.replace("'", "")

    # 去除多余空格
    name = " ".join(name.split())

    return name


def generate_vbs(json_file, parameter_file):

    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 读取 Delay 参数
    delay_df = pd.read_excel(
        parameter_file,
        sheet_name="Delay"
    )

    delay_map = {}

    for _, row in delay_df.iterrows():

        activity = clean_display_name(
            row["Activity"]
        )   

        delay_function = str(
            row["Delay_Function"]
        ).strip()

        delay_map[activity] = delay_function

    # 读取到达参数
    arrival_df = pd.read_excel(parameter_file,sheet_name="Arrival")
    arrival_function = str(arrival_df.iloc[0]["Expression"]).strip()

    # 读取网关参数
    gateway_df = pd.read_excel( parameter_file,sheet_name="Gateway")

    for col in ["Gateway", "Source", "Branch", "Type"]:
        gateway_df[col] = gateway_df[col].astype(str).str.strip()

    # 读取资源参数
    resource_df = pd.read_excel(parameter_file,sheet_name="resource")
    for col in ["Activity", "Resource_Set"]:
        resource_df[col] = (
            resource_df[col]
            .fillna("")
            .astype(str)
            .apply(clean_display_name)
            .str.strip()
        )

    resource_map = {}

    for _, row in resource_df.iterrows():

        activity = clean_display_name(row["Activity"] )

        resource_set = str( row["Resource_Set"] ).strip()

        resource_number = int(row["Resource_Number"])

        resource_requirement = int(row["Resource_Requirement"])

        # 拆分人员
        resources = [
            clean_display_name(r.strip())
            for r in resource_set.split(",")
            if r.strip()
        ]

        resource_map[activity] = {
            "resources": resources,
            "resource_number": resource_number,
            "requirement": resource_requirement
        }


    vbs = []
    visited = set()
    node_modules = {}

    resource_variables = {}
    resource_sets = {}

    x = 1400
    y = 700

    # 节点编号计数
    module_index = {
        "Create": 0,
        "Dispose": 0,
        "Decide": 0
    }
        

    def get_position():
        nonlocal x, y
        pos = (x, y)
        x += 1000
        if x > 6000:
            x = 1400
            y += 800
        return pos

    def create_resources():
        # 1. 收集所有唯一 Resource
        all_resources = set()

        for info in resource_map.values():

            for resource in info["resources"]:

                if resource:
                    all_resources.add(resource)

        # 2. 每个人创建一个 Resource
        for resource_name in sorted(all_resources):

            resource_var = "Res_" + clean_name(resource_name)

            resource_variables[resource_name] = resource_var

            vbs.append(
                f'Set {resource_var}=Model.Modules.Create("BasicProcess","Resource",0,0)\n'
            )

            vbs.append(
                f'{resource_var}.Data("Name")="{resource_name}"\n'
            )

            # 每个人一个 Resource，Capacity = 1
            vbs.append(
                f'{resource_var}.Data("Capacity")="1"\n'
            )
    def create_resource_sets():
        for activity, info in resource_map.items():
            set_var = (
                "Set_" +
                clean_name(activity)
            )
            resource_sets[activity] = set_var

            vbs.append(
                f'Set {set_var}=Model.Modules.Create("BasicProcess","Set",0,0)\n'
            )

            vbs.append(
                f'{set_var}.Data("Name")="{set_var}"\n'
            )

            resources = info["resources"]

            for index, resource_name in enumerate(
                resources,
                start=1
            ):

                resource_name = clean_display_name(
                    resource_name
                )

                if resource_name not in resource_variables:

                    print(
                        "WARNING: Resource not found:",
                        resource_name
                    )

                    continue

                vbs.append(
                    f'{set_var}.Data("Resource Name({index})")="{resource_name}"\n'
                )

    def create_module(node_id, module, prefix, node):

        px, py = get_position()
        name = node.get("name", node_id)
        clean_display = clean_display_name(name)
  

        if module == "Create":

            module_index["Create"] += 1

            var = (
                "Create"
                + str(module_index["Create"])
            )

            clean_display = var


        elif module == "Dispose":

            module_index["Dispose"] += 1

            var = (
                "Dispose"
                + str(module_index["Dispose"])
            )

            clean_display = var

        elif module == "Decide":

            module_index["Decide"] += 1

            var = (
                "Decide"
                + str(module_index["Decide"])
            )

            clean_display = var
    

        else:
            var = (
                prefix
                + clean_name(clean_display)
            )


        vbs.append(
            f'Set {var}=Model.Modules.Create("BasicProcess","{module}",{px},{py})\n'
        )

        vbs.append(
            f'{var}.Data("Name")="{clean_display}"\n'
        )

        # 到达参数
        if module == "Create":

            vbs.append(
                f'{var}.Data("Interarrival Type")="Expression"\n'
            )

            vbs.append(
                f'{var}.Data("Units")="Seconds"\n'
            )

            vbs.append(
                f'{var}.Data("Expression")="{arrival_function}"\n'
            )

        # 延迟参数、资源参数
        if module == "Process":

            activity_name = clean_display_name(clean_display)

            delay_function = delay_map.get(clean_display)
            resource_info = resource_map.get(activity_name)

            if (
                delay_function is not None
                or resource_info is not None
            ):

                vbs.append(
                    f'{var}.Data("Action")="Seize Delay Release"\n'
                )
                
            if delay_function is not None:
                vbs.append(
                    f'{var}.Data("DelayType")="Expression"\n'
                )

                vbs.append(
                    f'{var}.Data("Units")="Seconds"\n'
                )

                vbs.append(
                    f'{var}.Data("Expression")="{delay_function}"\n'
                )
                
            if resource_info is not None:

                set_var = resource_sets.get(
                    activity_name
                )

                requirement = resource_info[
                    "requirement"
                ]

                if set_var is not None:

                    vbs.append(
                        f'{var}.Data("Resource Type(1)")="Set"\n'
                    )

                    vbs.append(
                        f'{var}.Data("Set Name(1)")="{set_var}"\n'
                    )

                    vbs.append(
                        f'{var}.Data("Quantity(1)")="{requirement}"\n'
                    )

                    vbs.append(
                        f'{var}.Data("Selection Rule(1)")="Smallest Number Busy"\n'
                    )

        # 网关参数
        if module == "Decide":

             # BPMN Gateway ID
            gateway_id = str(node_id).strip()

            # 根据 Gateway ID 查找参数
            gateway_rows = gateway_df[
                gateway_df["Gateway"] == gateway_id
            ]

            if len(gateway_rows) == 0:

                print(
                    "WARNING: Gateway parameter not found:",
                    gateway_id
                )

            else:

                targets = node.get("targetRef", [])

                if isinstance(targets, str):
                    targets = targets.split(",")

                targets = [
                    t.strip()
                    for t in targets
                    if t.strip()
                ]

                # XOR 两个出口
                if len(targets) == 2:

                    # 当前规则：
                    # 第一个出口 = No
                    # 第二个出口 = Yes

                    yes_target_id = targets[1]

                    yes_node = data.get(
                        yes_target_id
                    )

                    if yes_node:

                        yes_branch = clean_display_name(
                            yes_node.get(
                                "name",
                                yes_target_id
                            )
                        )

                        yes_rows = gateway_rows[
                            gateway_rows["Branch"].apply(clean_display_name)
                            == yes_branch
                        ]

                        if len(yes_rows) == 1:

                            probability = float(
                                yes_rows.iloc[0]["Probability"]
                            )

                            percent_true = (
                                probability * 100
                            )

                            vbs.append(
                                f'{var}.Data("Type")="2-way by Chance"\n'
                            )

                            vbs.append(
                                f'{var}.Data("Percent True")="{percent_true:g}"\n'
                            )

                            print(
                                "GATEWAY:",
                                var,
                                "|",
                                gateway_id,
                                "| YES:",
                                yes_branch,
                                "|",
                                probability,
                                "=>",
                                percent_true
                            )

                        else:

                            print(
                                "WARNING: Branch probability not found:",
                                yes_branch
                            )

                    else:

                        print(
                            "WARNING: target node not found:",
                            yes_target_id
                        )

                else:

                    print(
                        "WARNING: Gateway is not XOR 2-way:",
                        gateway_id
                    )


        node_modules[node_id] = var


    def traverse(node_id):

        if node_id in visited or node_id not in data:
            return

        visited.add(node_id)

        node = data[node_id]
        module = node.get("module", "")

        if module == "startEvent":
            create_module(node_id, "Create", "Create_", node)

        elif module == "task":
            create_module(node_id, "Process", "Process_", node)

        elif module == "decide":
            create_module(node_id, "Decide", "Decide_", node)

        elif module == "endEvent":
            create_module(node_id, "Dispose", "Dispose_", node)
        
        elif module=="exclusiveGateway":
            # BPMN合并网关跳过
            pass


        targets = node.get("targetRef", [])

        if isinstance(targets, str):
            targets = targets.split(",")

        for t in targets:
            traverse(t.strip())


    def create_connections():

        for node_id, node in data.items():

            if node_id not in node_modules:
                continue

            source = node_modules[node_id]
            source_type = node.get("module", "")

            targets = node.get("targetRef", [])

            if isinstance(targets, str):
                targets = targets.split(",")

            for index,target_id in enumerate(targets):

                target_id = target_id.strip()

                if target_id not in node_modules:
                    continue

                target = node_modules[target_id]


                # ==========================
                # Decide出口
                # ==========================
                if source_type == "decide":

                    if index == 0:
                        label = "Next Label No"
                    else:
                        label = "Next Label Yes"


                    vbs.append(
                        f'''Model.Connections.Create _
                    {source}.Shape, _
                    {target}.Shape, _
                    "{label}"

                    '''
                                    )
                 # 普通连接
                else:
                    vbs.append(
                        f'''Model.Connections.Create _
                        {source}.Shape, _
                        {target}.Shape

                        '''
                                        )

                print("CONNECT:", node_id, "->", target_id)

    create_resources()
    create_resource_sets()

    for nid, node in data.items():
        if node.get("module") == "startEvent":
            traverse(nid)
            break


    create_connections()




    output = os.path.splitext(json_file)[0] + ".vbs"

    with open(output, "w", encoding="utf-8") as f:

        f.write(
'''
On Error Resume Next
Set app=createobject("arena.application")

app.visible=true

Set Model=app.models.add()

Model.ActiveView.AutoConnect = False
Model.ActiveView.SmartConnections = True

Dim xValues(1)
Dim yValues(1)


xValues(0)=0
xValues(1)=0

yValues(0)=0
yValues(1)=0

'''
        )

        for line in vbs:
            f.write(line)

        f.write(
'''
Model.ReplicationLength = 8

Model.BaseTimeUnits = 2



'''
        )

    print("Generated:", output)

    subprocess.run(["wscript", output])


if __name__ == "__main__":

    json_file=r"D:\SplitMinerForArena\char4\bpmn_vbs\output\note_light_json_final_parameter.json"
    parameter_file = r"D:\SplitMinerForArena\char4\bpmn_vbs\output\parameters.xlsx"
    generate_vbs(json_file, parameter_file)
