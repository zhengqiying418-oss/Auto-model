import pandas as pd
import json


def final_to_json(json_file_path,parameter_file_path):
    print("Reading JSON...")


    with open(
        json_file_path,
        "r",
        encoding="utf-8"
    ) as f:

        json_data=json.load(f)



    print("Reading parameters...")


    # ==========================
    # 参数读取
    # ==========================

    delay_df=pd.read_excel(
        parameter_file_path,
        sheet_name="Delay"
    )


    resource_df=pd.read_excel(
        parameter_file_path,
        sheet_name="resource"
    )


    gateway_df=pd.read_excel(
        parameter_file_path,
        sheet_name="Gateway"
    )


    loop_df=pd.read_excel(
        parameter_file_path,
        sheet_name="Loop"
    )


    arrival_df=pd.read_excel(
        parameter_file_path,
        sheet_name="Arrival"
    )



    # ==========================
    # Activity参数
    # ==========================

    activity_parameters={}


    # Delay

    for _,row in delay_df.iterrows():

        activity=row["Activity"]


        activity_parameters.setdefault(
            activity,
            {}
        )


        activity_parameters[
            activity
        ][
            "Expression"
        ]=row[
            "Delay_Function"
        ]



    # Resource

    for _,row in resource_df.iterrows():

        activity=row["Activity"]


        activity_parameters.setdefault(
            activity,
            {}
        )


        activity_parameters[
            activity
        ].update({

            "Resource_Set":
            row["Resource_Set"],


            "Resource_Number":
            int(
                row["Resource_Number"]
            ),


            # 新增
            "Resource_Requirement":
            int(
                row["Resource_Requirement"]
            )

        })



    # Loop

    for _,row in loop_df.iterrows():

        activity=row["Activity"]


        if activity in activity_parameters:

            activity_parameters[
                activity
            ][
                "Loop_Probability"
            ]=row[
                "Loop_Probability"
            ]



    # ==========================
    # Gateway概率
    # ==========================

    gateway_probability={}


    for _,row in gateway_df.iterrows():

        gateway=str(
            row["Gateway"]
        )


        branch=row["Branch"]


        probability=float(
            row["Probability"]
        )


        if gateway not in gateway_probability:

            gateway_probability[gateway]={}



        gateway_probability[gateway][branch]=probability



    # ==========================
    # Arrival参数
    # ==========================

    arrival_parameter={}


    for _,row in arrival_df.iterrows():

        arrival_parameter[
            row["Parameter"]
        ]=row[
            "Expression"
        ]



    # ==========================
    # 注入JSON
    # ==========================

    for node_id,node_info in json_data.items():


        if not isinstance(
            node_info,
            dict
        ):

            continue



        module=node_info.get(
            "module"
        )



        # ----------------------
        # Activity节点
        # ----------------------

        if module=="task":


            activity=node_info.get(
                "name"
            )


            if activity in activity_parameters:


                node_info.update(
                    activity_parameters[
                        activity
                    ]
                )



        # ----------------------
        # Decide节点
        # ----------------------

        elif module=="decide":


            gateway_id=str(
                node_info.get(
                    "Gateway_ID"
                )
            )


            if gateway_id in gateway_probability:


                node_info[
                    "Probability"
                ]=gateway_probability[
                    gateway_id
                ]

            else:

                print(
                    "Gateway probability missing:",
                    gateway_id
                )



    # ==========================
    # Process级参数
    # ==========================

    json_data[
        "Process_Parameter"
    ]={

        "Arrival":
        arrival_parameter

    }


    output_file=json_file_path.replace(
        ".json",
        "_parameter.json"
    )


    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:


        json.dump(
            json_data,
            f,
            indent=4,
            ensure_ascii=False
        )


    print(
        "Saved:",
        output_file
    )

    return output_file

json_file_path=r'D:\SplitMinerForArena\char4\bpmn_vbs\output\note_light_json_final.json'
parameter_file_path=r"D:\SplitMinerForArena\char4\bpmn_vbs\output\parameters.xlsx"
final_to_json(json_file_path,parameter_file_path)