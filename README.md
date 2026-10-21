# Readme
此仓库保存了论文中所涉及的模型和代码

## 运行环境 
- **Python 3.10**
- **PIP 26.1.2**
- **Java 1.8**
  - Java 依赖保存在`external_tools` 中，可以通过[SplitMiner](https://apromore.com/research-lab/) (v1, 2, 3)下载
- **Arena 14**

## 1. bpmn_vbs文件夹
其中代码主要实现BPMN怎样融合参数并最终转换成vbs代码，运行生成ARENA模型。

运行main.py,在UI界面上传事件日志转化的BPMN文件和事件日志xlsx文件即可

main.py中引入了该目录下其他.py函数的功能，进行了集成，各单步以及最终生成的结果输出在output目录下

## 2. external_tools文件夹
分割算法工具包

## 3. 其余文件
- **PurchasingExample.xlsx**: 事件日志原始数据

- **transXES.py**: 由于分割算法输入要求xes格式数据，本代码实现xlsx格式到xes格式的转换，输入PurchasingExample.xlsx，输出PurchasingExample.xes

- **splitminer.py**: 分割算法挖掘流程，输入PurchasingExample.xes，输出PurchasingExample_bpmn.bpmn



