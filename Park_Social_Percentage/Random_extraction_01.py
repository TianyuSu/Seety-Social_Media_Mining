# 随机提取
import pandas as pd
import numpy as np

# 读取CSV文件
df = pd.read_csv(r"D:\File\HK\ZhiCheng\data\Time_ZCL.csv")

# 计算每个park_name出现的次数比例
park_name_counts = df['park_name'].value_counts(normalize=True)

# 打印每个park_name出现的次数比例
print("Park Name Counts:")
print(park_name_counts)

# 计算park_name列中不同类型的数量(一共多少个不同的公园)
num_park_names = df['park_name'].nunique()
print("Total number of unique park_name types:", num_park_names)

# 根据比例随机提取3000条数据
random_data = pd.concat([df[df['park_name'] == name].sample(int(3000 * count), replace=True) for name, count in park_name_counts.items()])

# 将提取的数据保存到新的CSV文件
random_data.to_csv(r"D:\File\HK\ZhiCheng\data\Random_ZCL.csv", index=False)