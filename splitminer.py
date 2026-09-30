import subprocess

jar_path = r'D:\SplitMinerForArena\char4\external_tools\splitminer\splitminer.jar'
xes_path = r'D:\SplitMinerForArena\char4\PurchasingExample.xes'
bpmn_path = r'D:\SplitMinerForArena\char4\PurchasingExample_bpmn'

# 定义其他参数，例如epsilon和eta
epsilon = 0.1
eta = 0.4

# 构建命令行参数列表
args = ['java', '-jar', jar_path, str(epsilon), str(eta), xes_path, bpmn_path]

# 使用subprocess.call()执行命令
try:
    subprocess.call(args)
    print('Split Miner 运行完成。')
except Exception as e:
    print(f"Error occurred while running splitminer: {e}")