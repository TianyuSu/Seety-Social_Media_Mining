import pandas as pd

# 读取 Time_ZCL_2.csv 文件
time_df = pd.read_csv(r"D:\File\HK\ZhiCheng\data\Pre_process\Reduce_less50\Time_analysis\Period_three.csv")

# 读取 Shaixuan.csv 文件
shaixuan_df = pd.read_csv(r"D:\File\HK\ZhiCheng\data\Pre_process\Reduce_less50\Time_analysis\Period_three_Social.csv")

# 将 Shaixuan.csv 文件中的 review_id 列转换为集合，以便快速查找
review_id_set = set(shaixuan_df['review_id'])

# 在 Time_ZCL_2.csv 中根据 review_id 的出现情况给 Social 列赋值
time_df['Social'] = time_df['review_id'].apply(lambda x: 1 if x in review_id_set else 0)

# 保存结果到新的文件 Time_ZCL_2_with_Social.csv
time_df.to_csv(r"D:\File\HK\ZhiCheng\data\Pre_process\Reduce_less50\Time_analysis\Period_three_Social_Merge.csv", index=False)

print("Social 列已添加到 Time_ZCL_2.csv 文件中，并保存为 Time_ZCL_2_with_Social.csv。")