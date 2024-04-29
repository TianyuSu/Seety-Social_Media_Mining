import pandas as pd
import re
from tqdm import tqdm

# 定义切分函数
def cut_sentence(comment):
    comment = re.sub('([。！？～\?])([^”’])', r"\1\n\2", comment)
    comment = re.sub('(\.{6})([^”’])', r"\1\n\2", comment)
    comment = re.sub('(\…{2})([^”’])', r"\1\n\2", comment)
    comment = re.sub('([。！？\?][”’])([^，。！？\?])', r'\1\n\2', comment)
    comment = comment.rstrip()
    return comment.split("\n")

# 读取 keywords.csv 文件
keywords_df = pd.read_csv(r"D:\File\HK\ZhiCheng\data\Pre_process\Keywords_shaixuan2_04.csv", encoding='utf-8')

# 构建关键词词典
keywords_dict = set(keywords_df['Context'].astype(str))  # 将关键词转换为字符串型

# 读取 Time_ZCL_2.csv 文件
data_df = pd.read_csv(r"D:\File\HK\ZhiCheng\data\Pre_process\Reduce_less50\Time_analysis\Period_three.csv", encoding='utf-8')

# 筛选包含关键词的 review 及其相关列
selected_reviews = []
for review in tqdm(data_df['review_sum'], desc="Processing reviews"):
    sentences = cut_sentence(review)
    for sentence in sentences:
        for keyword in keywords_dict:
            if keyword in sentence:
                selected_reviews.append(data_df[data_df['review_sum'] == review].iloc[0])
                break
        else:
            continue
        break


# 保存筛选后的数据到新文件 Shaixuan.csv
selected_reviews_df = pd.DataFrame(selected_reviews)
selected_reviews_df.to_csv(r"D:\File\HK\ZhiCheng\data\Pre_process\Reduce_less50\Time_analysis\Period_three_Social.csv", index=False, encoding='utf-8')

print("筛选后的数据已保存到 Shaixuan.csv 文件中。")