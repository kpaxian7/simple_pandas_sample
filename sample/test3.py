import numpy as np
import pandas as pd

# 时间差值提取sample


# ---------- 读取excel或csv格式文件 ----------
#   目标文件target.xlsx 放在当前文件的目录同级
#   参数1 - 'target.xlsx' 目标文件名
#   参数2 - '拣选作业抬头' 要读取的sheet名称
res = pd.read_excel('target.xlsx', sheet_name='拣选作业抬头')

# ---------- 查看sheet内容 ----------
print(res)

# ---------- 查看表数据的行长度 ----------
print(len(res.values))

# ---------- 计算[get_job_time]和[finish_job_time]的列差值 ----------
diff = res['finish_job_time'] - res['get_job_time']

# ---------- 查看表数据每一行的时间差值 ----------
print(diff)
