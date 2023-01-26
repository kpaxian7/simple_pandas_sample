import numpy as np
import pandas as pd

# 获取sheet中某一列的数据sample


# ---------- 读取excel或csv格式文件 ----------
#   目标文件target.xlsx 放在当前文件的目录同级
#   参数1 - 'target.xlsx' 目标文件名
#   参数2 - '拣选作业抬头' 要读取的sheet名称
res = pd.read_excel('target.xlsx', sheet_name='拣选作业抬头')

# ---------- 查看sheet内容 ----------
print(res)

# ---------- 查看表数据的行长度 ----------
print(len(res.values))

# ---------- 通过方括号，获取对应列的数据 ----------
warehouse_id_arr = res['warehouse_id']
sku_amount_arr = res['sku_amount']
quantity_arr = res['quantity']

# ---------- 查看提取的对应列数据 ----------
print(warehouse_id_arr)
print(sku_amount_arr)
print(quantity_arr)
