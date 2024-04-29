import numpy as np
import csv
from scipy.spatial import distance
from tqdm import tqdm

def load_embeddings(file_path):
    embeddings = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        total_embeddings = int(next(file).split()[0])  # 读取并忽略维度，只获取总词数
        for line in tqdm(file, total=total_embeddings, desc="Loading embeddings"):
            parts = line.strip().split()
            word = parts[0]
            try:
                vector = np.array([float(x) for x in parts[1:]])
                embeddings[word] = vector
            except ValueError as e:
                print(f"Error processing line: {line}")
                print(e)
                continue
    return embeddings

def find_closest_embeddings(embeddings, target_word, top_n=100):
    if target_word not in embeddings:
        return []
    target_vector = embeddings[target_word]
    distances = []
    for word, vector in embeddings.items():
        if word != target_word:
            cos_sim = 1 - distance.cosine(target_vector, vector)
            distances.append((word, cos_sim))
    distances.sort(key=lambda x: x[1], reverse=True)
    return distances[:top_n]

def read_target_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        return [row[0] for row in reader]

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Target Word', 'Similar Word', 'Similarity'])
        for target_word, words in data:
            for word, similarity in words:
                writer.writerow([target_word, word, similarity])

# 加载嵌入向量
embeddings = load_embeddings(r"D:\File\HK\ZhiCheng\data\tencent-ailab-embedding-zh-d100-v0.2.0\tencent-ailab-embedding-zh-d100-v0.2.0\tencent-ailab-embedding-zh-d100-v0.2.0.txt")

# 读取目标词
target_words = read_target_words(r"C:\Users\11153\Desktop\Raw.csv")

# 为每个目标词找到同义词并保存
all_closest_words = [(word, find_closest_embeddings(embeddings, word, 100)) for word in target_words]

# 将结果保存到CSV文件
save_to_csv(all_closest_words, r"D:\File\HK\ZhiCheng\data\Pre_process\closest_words.csv")

print("所有同义词和相似度已保存到'closest_words.csv'文件中。")