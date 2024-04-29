# 首先确定时间范围
import pandas as pd

# 读取CSV文件
df = pd.read_csv(r"D:\File\HK\ZhiCheng\data\ZCL_Dianping_review_shanghai_raw2.csv", encoding='utf-8')

# 将time列转换为日期时间格式
df['time'] = pd.to_datetime(df['time'])

# 设置筛选条件为2019年1月1日至2021年1月1日
start_date = pd.to_datetime('2019-01-01')
end_date = pd.to_datetime('2021-01-31')

# 筛选出符合条件的数据
filtered_data = df[(df['time'] >= start_date) & (df['time'] < end_date)]

# 将筛选后的数据保存到新的CSV文件
filtered_data.to_csv(r"D:\File\HK\ZhiCheng\data\Time_ZCL.csv", index=False)