import json
import os



# =====================================================
# 基础函数
# =====================================================

def split_refs(refs):

    if refs is None:
        return []


    if isinstance(refs, list):

        return [
            x for x in refs
            if x
        ]


    return [
        x.strip()
        for x in str(refs).split(",")
        if x.strip()
    ]



# =====================================================
# 获取活动名称
# =====================================================

def get_activity_name(
        data,
        node_id,
        visited=None
):

    if visited is None:
        visited=set()


    if node_id in visited:
        return ""


    visited.add(node_id)



    if node_id not in data:
        return ""



    node=data[node_id]


    name=node.get(
        "name",
        ""
    )


    if name:
        return name



    targets=split_refs(
        node.get(
            "targetRef"
        )
    )


    for t in targets:

        result=get_activity_name(
            data,
            t,
            visited
        )

        if result:
            return result


    return ""



# =====================================================
# gateway source
# =====================================================

def get_gateway_sources(
        data,
        gateway_id
):

    if gateway_id not in data:
        return []


    return split_refs(
        data[gateway_id].get(
            "sourceRef"
        )
    )



# =====================================================
# gateway target
# =====================================================

def get_gateway_targets(
        data,
        gateway_id
):

    if gateway_id not in data:
        return []


    return split_refs(
        data[gateway_id].get(
            "targetRef"
        )
    )



# =====================================================
# 删除join gateway
# =====================================================

def remove_gateway_and_reconnect(
        data,
        gateway_id
):


    if gateway_id not in data:
        return



    gateway=data[gateway_id]


    # ==============================
    # 防止误删普通节点
    # ==============================

    if gateway.get("module") not in [
        "exclusiveGateway",
        "parallelGateway",
        "inclusiveGateway"
    ]:

        print(
            "Skip non gateway:",
            gateway_id
        )

        return



    sources=get_gateway_sources(
        data,
        gateway_id
    )


    targets=get_gateway_targets(
        data,
        gateway_id
    )


    print(
        "Reconnect gateway:",
        gateway_id
    )

    print(
        "sources:",
        sources
    )

    print(
        "targets:",
        targets
    )



    # =====================================================
    # source -> target
    # 将每个前驱节点中指向 gateway_id 的引用，
    # 替换为该汇聚网关的后继节点
    # =====================================================

    for s in sources:

        if s not in data:
            continue

        old_targets = split_refs(
            data[s].get("targetRef")
        )

        new_targets = []

        for old_target in old_targets:

            # 原来指向即将删除的汇聚网关
            if old_target == gateway_id:

                # 替换为汇聚网关的全部后继
                for target in targets:

                    if target not in new_targets:
                        new_targets.append(target)

            else:

                # 保留原有的其他连接
                if old_target not in new_targets:
                    new_targets.append(old_target)

        data[s]["targetRef"] = new_targets

    print(
        "Reconnect source:",
        s,
        "old:",
        old_targets,
        "new:",
        new_targets
    )


    # target source更新

    for t in targets:


        if t not in data:
            continue



        old_sources=split_refs(
            data[t].get(
                "sourceRef"
            )
        )



        old_sources=[
            x for x in old_sources
            if x != gateway_id
        ]



        for s in sources:

            if s not in old_sources:

                old_sources.append(s)



        data[t]["sourceRef"]=old_sources



    del data[gateway_id]



# =====================================================
# 修复悬空引用
# =====================================================

def repair_dangling_reference(data):


    valid_nodes=set(
        data.keys()
    )



    for node_id,node in data.items():


        if not isinstance(node,dict):
            continue



        if "targetRef" not in node:
            continue



        targets=split_refs(
            node.get(
                "targetRef"
            )
        )



        new_targets=[]


        for t in targets:


            if t in valid_nodes:

                new_targets.append(t)


            else:

                print(
                    "Remove broken target:",
                    node_id,
                    "->",
                    t
                )



        # 永远保存list

        node["targetRef"]=new_targets



# =====================================================
# Branch Mapping同步
# =====================================================
def sync_gateway_mapping(data):

    for node_id,node in data.items():

        if not isinstance(node,dict):
            continue


        if node.get("module")!="decide":
            continue


        targets=node.get(
            "targetRef",
            []
        )


        new_mapping={}


        for t in targets:

            if t in data:

                name=get_activity_name(
                    data,
                    t
                )

                if name:

                    new_mapping[t]=name


        node["Branch_Mapping"]=new_mapping


        print(
            "SYNC DECIDE:",
            node_id,
            node["targetRef"],
            node["Branch_Mapping"]
        )

  

# =====================================================
# 主函数
# =====================================================

def process_gateway(
        input_json_file
):


    with open(
        input_json_file,
        "r",
        encoding="utf-8"
    ) as f:

        data=json.load(f)



    print(
        "Loaded:",
        input_json_file
    )



    # =================================================
    # 第一阶段
    # Gateway split
    # =================================================

    for key,value in list(data.items()):


        if not isinstance(value,dict):
            continue



        module=value.get(
            "module"
        )


        direction=value.get(
            "gatewayDirection"
        )



        # =============================
        # XOR Diverging
        # =============================

        if (

            module=="exclusiveGateway"

            and

            direction=="Diverging"

        ):


            targets=get_gateway_targets(
                data,
                key
            )



            value["module"]="decide"


            value["Gateway_Type"]="XOR"


            value["Gateway_ID"]=key



            value["targetRef"]=targets



            branch={}


            for t in targets:

                branch[t]=get_activity_name(
                    data,
                    t
                )



            value["Branch_Mapping"]=branch


            value["Probability"]={}



            print(
                "XOR Decide:",
                key
            )

            print(
                targets
            )



        # =============================
        # AND Diverging
        # =============================

        elif (

            module=="parallelGateway"

            and

            direction=="Diverging"

        ):


            targets=get_gateway_targets(
                data,
                key
            )


            value["module"]="separate"


            value["targetRef"]=targets





    # =================================================
    # 第二阶段
    # 删除join gateway
    # =================================================

    for key,value in list(data.items()):


        if not isinstance(value,dict):
            continue



        module=value.get(
            "module"
        )


        direction=value.get(
            "gatewayDirection"
        )



        # =============================
        # XOR Join
        # =============================

        if (

            module=="exclusiveGateway"

            and

            direction=="Converging"

        ):


            remove_gateway_and_reconnect(
                data,
                key
            )



        # =============================
        # AND Join
        # =============================

        elif (

            module=="parallelGateway"

            and

            direction=="Converging"


        ):


            remove_gateway_and_reconnect(
                data,
                key
            )



        # =============================
        # Inclusive
        # =============================

        elif (

            module=="inclusiveGateway"
            and
            direction=="Converging"

        ):


            remove_gateway_and_reconnect(
                data,
                key
            )





    # =================================================
    # 第三阶段
    # 清理
    # =================================================

    repair_dangling_reference(
        data
    )


    sync_gateway_mapping(
        data
    )




    output_file=os.path.splitext(
        input_json_file
    )[0]+"_final.json"



    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:


        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )



    print(
        "Gateway processing completed:"
    )


    print(
        output_file
    )



    # 最终检查

    gid="node_b41a98ce-a48c-4369-880c-ffeb5ff98ee9"


    if gid in data:


        print(
            "FINAL gateway targetRef:"
        )


        print(
            data[gid].get(
                "targetRef"
            )
        )



    return output_file





# =====================================================
# main
# =====================================================

if __name__=="__main__":


    process_gateway(

        r"D:\SplitMinerForArena\char4\bpmn_vbs\output\note_light_json.json"

    )