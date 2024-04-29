import pandas as pd

# 读取 Time_ZCL_2_with_Social.csv 文件
time_social_df = pd.read_csv(r"D:\File\HK\ZhiCheng\data\Pre_process\Reduce_less50\Time_analysis\Period_three_Social_Merge.csv")

# 计算每个 park_id 中 Social 列为 1 的占比
percentage_df = time_social_df.groupby('park_id')['Social'].mean().reset_index()
percentage_df.rename(columns={'Social': 'Percentage'}, inplace=True)

# 保存结果到新的文件 Percentage.csv
percentage_df.to_csv(r"D:\File\HK\ZhiCheng\data\Pre_process\Reduce_less50\Time_analysis\Period_three_Social_Merge_Percentage.csv", index=False)

print("每个 park_id 中 Social 列为 1 的占比已计算并保存到 Percentage.csv 文件中。")