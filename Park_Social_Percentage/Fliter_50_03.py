import pandas as pd

# 读取 Time_ZCL_01_less50.csv 文件
file_path = r"D:\File\HK\ZhiCheng\data\Pre_process\Reduce_less50\Time_ZCL_01_less50.csv"
data_df = pd.read_csv(file_path)

# 统计 park_id 列中每个值的出现次数
park_id_counts = data_df['park_id'].value_counts()

# 获取出现次数小于 50 次的 park_id 值
less_than_50 = park_id_counts[park_id_counts < 50].index

# 删除出现次数小于 50 次的行
filtered_data_df = data_df[~data_df['park_id'].isin(less_than_50)]

# 保存处理后的结果到新文件
filtered_data_df.to_csv(r"D:\File\HK\ZhiCheng\data\Pre_process\Reduce_less50\Time_ZCL_01_less50_filtered.csv", index=False)

print("已删除出现次数小于50次的行，并将结果保存到新文件中。")