import pandas as pd
import numpy as np
import os
import xml.etree.ElementTree as ET
from scipy.stats import (
    norm,
    uniform,
    expon,
    lognorm,
    gamma,
    weibull_min,
    triang,
    poisson,
    kstest
)

# 1. 活动延迟函数拟合 (单位秒)
def fit_activity_duration(df):
    results = []
    # 按照活动分类
    for activity in df["activity"].unique():
        activity_data = df[ df["activity"] == activity ]

        duration = (activity_data["duration"] .values)

        if len(duration) < 5: continue

        # 初始化
        best_model = None
        best_score = float('inf')

        # Normal
        try:
            mu, std = norm.fit(duration)
            if std > 0:
                score = ( ((duration-mu)/std)**2).mean()

                if score < best_score:
                    best_score = score
                    best_model = (f"NORM({mu:.0f},{std:.0f})")
        except Exception as e:

            print(
                "Normal fitting error:",
                activity,
                e
            )


        # Constant
        try:
            value = duration.mean()
            score = ( (duration-value)**2).mean()
            if score < best_score:
                best_score = score
                best_model = ( f"{value:.0f}")
        except Exception as e:

            print(
                "Constant fitting error:",
                activity,
                e
            )

        # Triangular
        try:
            c, loc, scale = triang.fit( duration)
            score = ((duration-loc)**2).mean()
            if score < best_score:
                best_score = score
                best_model = (
                    f"TRIA({loc:.0f},"
                    f"{c:.0f},"
                    f"{loc+scale:.0f})"
                )

        except Exception as e:
            print(
                "Triangular fitting error:",
                activity,
                e
            )

        # Uniform
        try:
            low = duration.min()
            high = duration.max()
            if high > low:
                score = (((duration-low) /(high-low))**2 ).mean()
                if score < best_score:
                    best_score = score
                    best_model = (
                        f"UNIF({low:.0f},"
                        f"{high:.0f})"
                    )
        except Exception as e:

            print(
                "Uniform fitting error:",
                activity,
                e
            )

        # Exponential
        try:
            loc, scale = expon.fit(duration)
            if scale > 0:
                score = (((duration-loc) /scale)**2).mean()
                if score < best_score:
                    best_score = score
                    best_model = ( f"EXPO({loc:.0f})")
        except Exception as e:
            print(
                "Exponential fitting error:",
                activity,
                e
            )

        # Poisson
        try:
            lam = duration.mean()
            if lam > 0:
                score = (((duration-lam)/lam)**2 ).mean()
                if score < best_score:
                    best_score = score
                    best_model = ( f"POIS({lam:.0f})")
        except Exception as e:
            print(
                "Poisson fitting error:",
                activity,
                e
            )

        results.append({
            "Activity":activity,
            "Delay_Function":best_model,
            "Fit_Score": best_score
        })



    return pd.DataFrame(results)

# 2. 资源参数提取（数量）
def extract_resource_parameter(df):
    results=[]
    for activity in df["activity"].unique():
        temp=df[df["activity"]==activity]
        resources=(temp["resource"].dropna().unique())

        case_resource_count=(temp.groupby("case_id")["resource"].nunique())

        if len(case_resource_count)>0:
            resource_requirement=int(case_resource_count.mode()[0])

        else:
            resource_requirement=1

        results.append({
            "Activity":activity,
            "Resource_Set":",".join(resources),
            "Resource_Number":len(resources),
            "Resource_Requirement":resource_requirement
        })
    return pd.DataFrame(results)

# 3. Case到达参数（单位秒）
def calculate_arrival_parameter(df):
    # 1. 提取每个Case的首次事件时间
    first_event = (
        df.sort_values(["case_id", "start_time"])
        .groupby("case_id")["start_time"]
        .first()
        .sort_values()
    )

    # 2. 计算相邻Case到达间隔，单位为秒
    intervals = (
        first_event
        .diff()
        .dt.total_seconds()
        .dropna()
    )

    intervals = intervals[
        np.isfinite(intervals) & (intervals >= 0)
    ].astype(float)

    if len(intervals) == 0:
        return pd.DataFrame([{
            "Parameter": "Case Arrival Rate",
            "Distribution": "Constant",
            "Expression": "0",
            "KS_Statistic": np.nan,
            "KS_PValue": np.nan,
            "AIC": np.nan,
            "Sample_Size": 0,
            "Zero_Interval_Count": 0,
            "Zero_Interval_Ratio": 0
        }])

    all_x = intervals.to_numpy(dtype=float)
    # 3. 诊断零间隔
    zero_count = int(np.sum(all_x == 0))
    zero_ratio = zero_count / len(all_x)

    # Lognormal、Gamma、Weibull等分布要求样本严格大于0
    positive_x = all_x[all_x > 0]

    print("\nArrival interval diagnostics:")
    print("Total intervals:", len(all_x))
    print("Zero intervals:", zero_count)
    print("Zero interval ratio:", round(zero_ratio, 4))
    print("Positive intervals:", len(positive_x))


    # 4. 常数分布判断
    mean_all = float(np.mean(all_x))

    if np.allclose(
        all_x,
        mean_all,
        rtol=1e-6,
        atol=1e-6
    ):
        return pd.DataFrame([{
            "Parameter": "Case Arrival Rate",
            "Distribution": "Constant",
            "Expression": f"{mean_all:.0f}",
            "KS_Statistic": 0.0,
            "KS_PValue": 1.0,
            "AIC": 0.0,
            "Sample_Size": len(all_x),
            "Zero_Interval_Count": zero_count,
            "Zero_Interval_Ratio": zero_ratio
        }])

    if len(positive_x) < 5:
        print(
            "Warning: fewer than 5 positive arrival intervals; "
            "distribution fitting is unreliable."
        )

        return pd.DataFrame([{
            "Parameter": "Case Arrival Rate",
            "Distribution": "Constant",
            "Expression": f"{mean_all:.0f}",
            "KS_Statistic": np.nan,
            "KS_PValue": np.nan,
            "AIC": np.nan,
            "Sample_Size": len(all_x),
            "Zero_Interval_Count": zero_count,
            "Zero_Interval_Ratio": zero_ratio
        }])

    candidates = []

    # 5. 通用评价函数

    def evaluate_distribution(
        sample,
        distribution_name,
        scipy_distribution,
        params,
        expression,
        parameter_count
    ):
        try:
            log_pdf = scipy_distribution.logpdf(
                sample,
                *params
            )

            if not np.all(np.isfinite(log_pdf)):
                print(
                    distribution_name,
                    "contains invalid log-likelihood values."
                )
                return

            log_likelihood = float(np.sum(log_pdf))

            # AIC = 2k - 2ln(L)
            aic = (
                2 * parameter_count
                - 2 * log_likelihood
            )

            ks_statistic, ks_pvalue = kstest(
                sample,
                scipy_distribution.cdf,
                args=params
            )

            candidates.append({
                "Parameter": "Case Arrival Rate",
                "Distribution": distribution_name,
                "Expression": expression,
                "KS_Statistic": float(ks_statistic),
                "KS_PValue": float(ks_pvalue),
                "AIC": float(aic),
                "Sample_Size": len(sample),
                "Zero_Interval_Count": zero_count,
                "Zero_Interval_Ratio": zero_ratio
            })

        except Exception as e:
            print(
                f"{distribution_name} arrival evaluation error:",
                e
            )

    # 6. 指数分布
    try:
        loc, scale = expon.fit(
            positive_x,
            floc=0
        )

        if scale > 0:
            evaluate_distribution(
                sample=positive_x,
                distribution_name="Exponential",
                scipy_distribution=expon,
                params=(loc, scale),
                expression=f"EXPO({scale:.0f})",
                parameter_count=1
            )

    except Exception as e:
        print("Exponential arrival fitting error:", e)

    # 7. 正态分布

    try:
        mu, sigma = norm.fit(positive_x)

        if sigma > 0:
            negative_probability = norm.cdf(
                0,
                loc=mu,
                scale=sigma
            )

            # 避免正态分布生成过多负到达间隔
            if negative_probability <= 0.01:
                evaluate_distribution(
                    sample=positive_x,
                    distribution_name="Normal",
                    scipy_distribution=norm,
                    params=(mu, sigma),
                    expression=f"NORM({mu:.0f},{sigma:.0f})",
                    parameter_count=2
                )
            else:
                print(
                    "Normal excluded: probability of negative "
                    f"intervals = {negative_probability:.4f}"
                )

    except Exception as e:
        print("Normal arrival fitting error:", e)

    
    # 8. 均匀分布

    try:
        low = float(np.min(positive_x))
        high = float(np.max(positive_x))
        width = high - low

        if width > 0:
            evaluate_distribution(
                sample=positive_x,
                distribution_name="Uniform",
                scipy_distribution=uniform,
                params=(low, width),
                expression=f"UNIF({low:.0f},{high:.0f})",
                parameter_count=2
            )

    except Exception as e:
        print("Uniform arrival fitting error:", e)


    # 9 选择最优分布
    if len(candidates) == 0:
        return pd.DataFrame([{
            "Parameter": "Case Arrival Rate",
            "Distribution": "Constant",
            "Expression": f"{np.mean(positive_x):.0f}",
            "KS_Statistic": np.nan,
            "KS_PValue": np.nan,
            "AIC": np.nan,
            "Sample_Size": len(positive_x),
            "Zero_Interval_Count": zero_count,
            "Zero_Interval_Ratio": zero_ratio
        }])

    candidate_df = pd.DataFrame(candidates)

    accepted = candidate_df[
        candidate_df["KS_PValue"] >= 0.05
    ]

    if not accepted.empty:
        # 通过KS检验后选择AIC最小者
        best = (
            accepted
            .sort_values(
                ["AIC", "KS_Statistic"],
                ascending=[True, True]
            )
            .iloc[0]
        )

        selection_status = "Passed KS test"

    else:
        # 没有候选分布通过KS检验
        best = (
            candidate_df
            .sort_values(
                ["KS_Statistic", "AIC"],
                ascending=[True, True]
            )
            .iloc[0]
        )

        selection_status = (
            "No candidate passed KS test; "
            "selected minimum KS statistic"
        )

    print("\nArrival distribution candidates:")
    print(
        candidate_df
        .sort_values(
            ["KS_Statistic", "AIC"]
        )
        .to_string(index=False)
    )

    print("\nSelected arrival distribution:")
    print(best.to_dict())

    print("Selection status:", selection_status)

    result = best.to_dict()
    result["Selection_Status"] = selection_status

    return pd.DataFrame([result])

# 4. XOR分支概率
def resolve_gateway_path(
        node,
        node_name_map,
        flow_source
):


    result=[]


    # 如果是任务节点

    if node in node_name_map:

        result.append(
            node_name_map[node]
        )

        return result



    # 如果还是Gateway

    if node in flow_source:


        for next_node in flow_source[node]:

            result.extend(

                resolve_gateway_path(
                    next_node,
                    node_name_map,
                    flow_source
                )

            )


    return result
def extract_bpmn_gateway(bpmn_file):

    tree = ET.parse(
        bpmn_file
    )

    root = tree.getroot()


    # ======================
    # 节点名称映射
    # ======================

    node_name_map={}


    for elem in root.iter():

        node_id=elem.attrib.get(
            "id"
        )

        node_name=elem.attrib.get(
            "name"
        )


        if node_id and node_name:

            node_name_map[node_id]=node_name



    # ======================
    # sequenceFlow关系
    # ======================

    flow_source={}
    flow_target={}


    for flow in root.iter():


        if flow.tag.endswith(
            "sequenceFlow"
        ):

            source=flow.attrib.get(
                "sourceRef"
            )

            target=flow.attrib.get(
                "targetRef"
            )


            flow_source.setdefault(
                source,
                []
            ).append(target)


            flow_target.setdefault(
                target,
                []
            ).append(source)



    gateways=[]



    # ======================
    # 查找XOR Gateway
    # ======================

    for elem in root.iter():


        if not elem.tag.endswith(
            "exclusiveGateway"
        ):
            continue



        gateway_id=elem.attrib["id"]



        incoming_nodes=flow_target.get(
            gateway_id,
            []
        )


        outgoing_nodes=flow_source.get(
            gateway_id,
            []
        )


        # ======================
        # 只保留split gateway
        #
        # outgoing > 1
        #
        # ======================

        if len(outgoing_nodes)<=1:

            continue



        incoming=[]

        outgoing=[]



        # 输入任务

        for node in incoming_nodes:


            if node in node_name_map:

                incoming.append(
                    node_name_map[node]
                )



        # 输出任务
        # 处理Gateway嵌套

        for node in outgoing_nodes:


            outgoing.extend(

                resolve_gateway_path(
                    node,
                    node_name_map,
                    flow_source
                )

            )



        gateways.append({

            "gateway_id":
            gateway_id,


            "source":
            incoming,


            "branches":
            outgoing

        })


    return gateways
def calculate_gateway_probability(
        df,
        gateways
):


    results=[]



    for gateway in gateways:


        sources=gateway["source"]

        branches=gateway["branches"]



        if len(sources)==0:

            continue



        source=sources[0]



        count={}


        for b in branches:

            count[b]=0



        # 遍历日志

        for case,trace in df.groupby(
            "case_id"
        ):


            trace=trace.sort_values(
                "start_time"
            )


            activities=list(
                trace["activity"]
            )


            if source not in activities:

                continue



            index=activities.index(
                source
            )



            if index+1 < len(activities):


                next_act=activities[
                    index+1
                ]



                if next_act in count:

                    count[next_act]+=1




        total=sum(
            count.values()
        )


        if total==0:

            continue



        for branch,num in count.items():


            results.append({

                "Gateway":

                gateway["gateway_id"],


                "Source":

                source,


                "Branch":

                branch,


                "Probability":

                round(
                    num/total,
                    4
                ),


                "Type":

                "XOR"

            })



    return pd.DataFrame(results)
# 5. 循环概率
def calculate_loop_probability(df):
    loop_results=[]
    transitions=[]
    for case,trace in df.groupby("case_id"):
        activities=list(
            trace.sort_values("start_time")["activity"])
        for i in range(len(activities)-1):
            transitions.append(
                [
                    activities[i],
                    activities[i+1]
                ]
            )
    transition_df=pd.DataFrame(
        transitions,
        columns=["source","target"]
    )

    for activity in transition_df["source"].unique():
        outgoing=transition_df[transition_df["source"]==activity]
        total=len(outgoing)

        loop_count=len(
            outgoing[
                outgoing["target"]==activity
            ]
        )

        if loop_count>0:
            loop_results.append({
                "Activity":activity,
                "Loop_Probability":round(loop_count/total,4)
            })

    return pd.DataFrame(loop_results)


# 主函数
def generate_simulation_parameters(input_file, bpmn_file,output_file):
    print("Reading event log..." )
    df=pd.read_excel(input_file)

    # 时间转换
    df["start_time"] = pd.to_datetime( df["start_time"],utc=True)
    df["end_time"] = pd.to_datetime(df["end_time"],utc=True)

    # 计算duration
    df["duration"]=( df["end_time"]-df["start_time"]).dt.total_seconds()

    print("Mining delay parameters...")
    delay_df = fit_activity_duration(df)
    
    print("Mining resource parameters...")
    resource_df = (extract_resource_parameter(df))

    print("Mining arrival parameters...")
    arrival_df = ( calculate_arrival_parameter(df))

    print( "Mining gateway probabilities...")
    gateways = extract_bpmn_gateway(bpmn_file)
    print("Detected BPMN gateways:")

    for g in gateways:

        print(g)
    gateway_df = calculate_gateway_probability(df,gateways)

    print("Mining loop probabilities...")
    loop_df = (calculate_loop_probability(df))

    os.makedirs(
        os.path.dirname(output_file),
        exist_ok=True
    )

    with pd.ExcelWriter(
        output_file
    ) as writer:

        delay_df.to_excel(
            writer,
            sheet_name="Delay",
            index=False
        )


        resource_df.to_excel(
            writer,
            sheet_name="resource",
            index=False
        )


        arrival_df.to_excel(
            writer,
            sheet_name="Arrival",
            index=False
        )


        gateway_df.to_excel(
            writer,
            sheet_name="Gateway",
            index=False
        )


        loop_df.to_excel(
            writer,
            sheet_name="Loop",
            index=False
        )

    print("Parameter generation completed:")
    print(output_file)


# 程序入口
if __name__=="__main__":
    generate_simulation_parameters(
        input_file= r"D:\SplitMinerForArena\char4\PurchasingExample.xlsx",
        bpmn_file=r"D:\SplitMinerForArena\char4\PurchasingExample_bpmn.bpmn",
        output_file= r"D:\SplitMinerForArena\char4\bpmn_vbs\output\parameters.xlsx"
    )
