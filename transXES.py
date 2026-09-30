import xml.etree.ElementTree as ET
from xml.dom import minidom
import pandas as pd


def transxml():
    # 读取 Excel 文件
    input_path = r'D:\SplitMinerForArena\char4\PurchasingExample.xlsx'
    output_path = r'D:\SplitMinerForArena\char4\PurchasingExample.xes'

    df = pd.read_excel(input_path)

    # 检查 Excel 是否包含必要字段
    required_columns = [
        'case_id',
        'activity',
        'resource',
        'start_time',
        'end_time'
    ]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f'Excel 缺少以下字段：{missing_columns}'
        )

    # 将带时区的 ISO 8601 时间转换为 datetime
    # 例如：2011-01-01T12:37:00+02:00
    df['start_time'] = pd.to_datetime(
        df['start_time'],
        utc=True,
        errors='coerce'
    )

    df['end_time'] = pd.to_datetime(
        df['end_time'],
        utc=True,
        errors='coerce'
    )

    # 删除案例、活动或时间缺失的记录
    df = df.dropna(
        subset=[
            'case_id',
            'activity',
            'start_time',
            'end_time'
        ]
    )

    # 按案例编号、开始时间、结束时间排序
    df = df.sort_values(
        by=['case_id', 'start_time', 'end_time']
    )

    # 创建 XES 根节点
    root = ET.Element(
        'log',
        attrib={
            'xes.version': '1.0',
            'xes.features': 'nested-attributes',
            'xmlns': 'http://www.xes-standard.org',
            'xes.creator': 'Python XES Converter'
        }
    )

    # XES 扩展声明
    ET.SubElement(
        root,
        'extension',
        attrib={
            'name': 'Concept',
            'prefix': 'concept',
            'uri': 'http://www.xes-standard.org/concept.xesext'
        }
    )

    ET.SubElement(
        root,
        'extension',
        attrib={
            'name': 'Lifecycle',
            'prefix': 'lifecycle',
            'uri': 'http://www.xes-standard.org/lifecycle.xesext'
        }
    )

    ET.SubElement(
        root,
        'extension',
        attrib={
            'name': 'Time',
            'prefix': 'time',
            'uri': 'http://www.xes-standard.org/time.xesext'
        }
    )

    ET.SubElement(
        root,
        'extension',
        attrib={
            'name': 'Organizational',
            'prefix': 'org',
            'uri': 'http://www.xes-standard.org/org.xesext'
        }
    )

    # 声明全局 trace 属性
    global_trace = ET.SubElement(
        root,
        'global',
        attrib={'scope': 'trace'}
    )

    ET.SubElement(
        global_trace,
        'string',
        attrib={
            'key': 'concept:name',
            'value': 'name'
        }
    )

    ET.SubElement(
        global_trace,
        'string',
        attrib={
            'key': 'variant',
            'value': 'Variant'
        }
    )

    ET.SubElement(
        global_trace,
        'int',
        attrib={
            'key': 'variant-index',
            'value': '0'
        }
    )

    # 声明全局 event 属性
    global_event = ET.SubElement(
        root,
        'global',
        attrib={'scope': 'event'}
    )

    ET.SubElement(
        global_event,
        'string',
        attrib={
            'key': 'concept:name',
            'value': 'name'
        }
    )

    ET.SubElement(
        global_event,
        'string',
        attrib={
            'key': 'lifecycle:transition',
            'value': 'complete'
        }
    )

    ET.SubElement(
        global_event,
        'string',
        attrib={
            'key': 'org:resource',
            'value': 'resource'
        }
    )

    ET.SubElement(
        global_event,
        'date',
        attrib={
            'key': 'time:timestamp',
            'value': '1970-01-01T00:00:00.000+00:00'
        }
    )

    ET.SubElement(
        global_event,
        'string',
        attrib={
            'key': 'Activity',
            'value': 'activity'
        }
    )

    ET.SubElement(
        global_event,
        'string',
        attrib={
            'key': 'Resource',
            'value': 'resource'
        }
    )

    # 分类器
    ET.SubElement(
        root,
        'classifier',
        attrib={
            'name': 'Activity',
            'keys': 'Activity'
        }
    )

    ET.SubElement(
        root,
        'classifier',
        attrib={
            'name': 'Resource',
            'keys': 'Resource'
        }
    )

    # 日志级属性
    ET.SubElement(
        root,
        'string',
        attrib={
            'key': 'lifecycle:model',
            'value': 'standard'
        }
    )

    ET.SubElement(
        root,
        'string',
        attrib={
            'key': 'creator',
            'value': 'Fluxicon Disco'
        }
    )

    # 创建 XML 属性节点的工具函数
    def create_element(parent, tag, value=None, key=None):
        element = ET.SubElement(parent, tag)

        if key is not None:
            element.set('key', str(key))

        if value is not None:
            element.set('value', str(value))

        return element

    # 格式化为 XES 时间格式，并保留原始时区
    def format_xes_time(timestamp):
        """
        输入示例：
        2011-01-01 12:37:00+02:00

        输出示例：
        2011-01-01T12:37:00.000+02:00
        """
        text = timestamp.isoformat(timespec='milliseconds')

        return text

    # 计算每个案例的活动序列，用于生成 variant
    case_sequences = {}

    for case_id, group in df.groupby('case_id', sort=False):
        activity_sequence = tuple(
            group['activity'].astype(str).tolist()
        )
        case_sequences[str(case_id)] = activity_sequence

    # 记录不同活动序列对应的 Variant 编号
    variant_mapping = {}
    variant_counter = 1

    for case_id, sequence in case_sequences.items():
        if sequence not in variant_mapping:
            variant_mapping[sequence] = variant_counter
            variant_counter += 1

    # 保存每个 case_id 对应的 trace 节点
    trace_dict = {}

    # 逐行创建事件
    for _, row in df.iterrows():
        case_id = str(row['case_id'])
        activity = str(row['activity'])

        if pd.isna(row['resource']):
            resource = ''
        else:
            resource = str(row['resource'])

        start_time_iso = format_xes_time(row['start_time'])
        end_time_iso = format_xes_time(row['end_time'])

        # 首次遇到该案例时创建 trace
        if case_id not in trace_dict:
            trace = ET.SubElement(root, 'trace')

            # case_id
            create_element(
                trace,
                'string',
                value=case_id,
                key='concept:name'
            )

            # 该案例所属 Variant
            sequence = case_sequences[case_id]
            current_variant_index = variant_mapping[sequence]

            create_element(
                trace,
                'string',
                value=f'Variant {current_variant_index}',
                key='variant'
            )

            create_element(
                trace,
                'int',
                value=current_variant_index,
                key='variant-index'
            )

            create_element(
                trace,
                'string',
                value='Fluxicon Disco',
                key='creator'
            )

            trace_dict[case_id] = trace

        else:
            trace = trace_dict[case_id]

        # ----------------------------
        # 生成 start 事件
        # ----------------------------
        start_event = ET.SubElement(trace, 'event')

        create_element(
            start_event,
            'string',
            value=activity,
            key='concept:name'
        )

        create_element(
            start_event,
            'string',
            value='start',
            key='lifecycle:transition'
        )

        create_element(
            start_event,
            'string',
            value=resource,
            key='org:resource'
        )

        create_element(
            start_event,
            'date',
            value=start_time_iso,
            key='time:timestamp'
        )

        create_element(
            start_event,
            'string',
            value=activity,
            key='Activity'
        )

        create_element(
            start_event,
            'string',
            value=resource,
            key='Resource'
        )

        # ----------------------------
        # 生成 complete 事件
        # ----------------------------
        complete_event = ET.SubElement(trace, 'event')

        create_element(
            complete_event,
            'string',
            value=activity,
            key='concept:name'
        )

        create_element(
            complete_event,
            'string',
            value='complete',
            key='lifecycle:transition'
        )

        create_element(
            complete_event,
            'string',
            value=resource,
            key='org:resource'
        )

        create_element(
            complete_event,
            'date',
            value=end_time_iso,
            key='time:timestamp'
        )

        create_element(
            complete_event,
            'string',
            value=activity,
            key='Activity'
        )

        create_element(
            complete_event,
            'string',
            value=resource,
            key='Resource'
        )

    # 转为 XML 字符串
    xmlstr = ET.tostring(
        root,
        encoding='utf-8',
        xml_declaration=True
    )

    # 美化 XML 缩进格式
    xml_dom = minidom.parseString(xmlstr)

    pretty_xml = xml_dom.toprettyxml(
        indent='    ',
        encoding='utf-8'
    )

    # 删除 minidom 产生的空白行
    pretty_xml = b'\n'.join(
        line for line in pretty_xml.splitlines()
        if line.strip()
    )

    # 写入 XES 文件
    with open(output_path, 'wb') as f:
        f.write(pretty_xml)

    print(f'XES 文件已生成：{output_path}')
    print(f'案例数量：{df["case_id"].nunique()}')
    print(f'活动记录数量：{len(df)}')
    print(f'XES 事件数量：{len(df) * 2}')
    print(f'流程变体数量：{len(variant_mapping)}')

# 测试
if __name__ == '__main__':
    transxml()