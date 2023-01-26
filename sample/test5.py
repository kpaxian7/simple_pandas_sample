import numpy as np
import pandas as pd

# 提取特定条件的数据sample（提取sku_amount与quantity占比为1.0的数据）

# ---------- 读取excel或csv格式文件 ----------
#   目标文件target.xlsx 放在当前文件的目录同级
#   参数1 - 'target.xlsx' 目标文件名
#   参数2 - '拣选作业抬头' 要读取的sheet名称
res = pd.read_excel('target.xlsx', sheet_name='拣选作业抬头')

# ---------- 查看sheet内容 ----------
print(res)

# ---------- 查看表数据的行长度 ----------
print(len(res.values))

# ---------- 使用loc切片方法，进行表达式筛选 ----------
# 示例：
# res[res['Q1'] == 8] # Q1 等于8
# res[~(res['Q1'] == 8)] # 不等于8
# res[res.name == 'Ben'] # 姓名为Ben
# res.loc[res['Q1'] > 90, 'Q1':]  # Q1 大于90，显示Q1后边的所有列
# res.loc[(res.Q1 > 80) & (res.Q2 < 15)] # and 关系
# res.loc[(res.Q1 > 90) | (res.Q2 < 90)] # or 关系
# res[res.Q1 > res.Q2]
diff = res.loc[res['sku_amount'] / res['quantity'] >= 1]

# ---------- 查看筛选后的数据 ----------
print(diff)
