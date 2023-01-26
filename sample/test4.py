import numpy as np
import pandas as pd

# 计算占比sample（计算sheet中sku_amount和quantity的百分比占比）


# ---------- 读取excel或csv格式文件 ----------
#   目标文件target.xlsx 放在当前文件的目录同级
#   参数1 - 'target.xlsx' 目标文件名
#   参数2 - '拣选作业抬头' 要读取的sheet名称
res = pd.read_excel('target.xlsx', sheet_name='拣选作业抬头')

# ---------- 查看sheet内容 ----------
print(res)

# ---------- 查看表数据的行长度 ----------
print(len(res.values))

# ---------- 计算每条数据中sku_amount与quantity的占比(sku_amount/quantity) ----------
diff = res['sku_amount'] / res['quantity']

# ---------- 查看表数据每一行的占比值 ----------
print(diff)
