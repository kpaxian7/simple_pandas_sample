import numpy as np
import pandas as pd

# 数据清洗sample


# ---------- 读取excel或csv格式文件 ----------
#   目标文件target.xlsx 放在当前文件的目录同级
#   参数1 - 'target.xlsx' 目标文件名
#   参数2 - '拣选作业抬头' 要读取的sheet名称
res = pd.read_excel('target.xlsx', sheet_name='拣选作业抬头')

# ---------- 查看sheet内容 ----------
print(res)

# ---------- 查看表数据的行长度 ----------
print(len(res.values))

# ---------- 清洗掉数据残缺的行（picking_work_id存在空 或 NaN的数据） ----------
#   使用dropna函数，进行数据清理
#       axis：默认为 0，表示逢空值剔除整行，如果设置参数 axis＝1 表示逢空值去掉整列。
#       how：默认为 'any' 如果一行（或一列）里任何一个数据有出现 NA 就去掉整行，如果设置 how='all' 一行（或列）都是 NA 才去掉这整行。
#       thresh：设置需要多少非空值的数据才可以保留下来的。
#       subset：设置想要检查的列。如果是多个列，可以使用列名的 list 作为参数。
#       inplace：如果设置 True，将计算得到的值直接覆盖之前的值并返回 None，修改的是源数据。
res_after_drop = res.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

# ---------- 查看表数据的行长度（清洗后的） ----------
print(len(res_after_drop.values))
