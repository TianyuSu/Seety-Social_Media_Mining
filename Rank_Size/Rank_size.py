import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from matplotlib.ticker import FuncFormatter, ScalarFormatter

# 读取CSV文件
# df = pd.read_csv(r"D:\File\HK\ZhiCheng\data\Pre_process\Rank_size\Rank_size_three_period.csv")
df = pd.read_csv(r"D:\File\HK\ZhiCheng\data\Pre_process\Rank_size\Rank_size_one_period.csv")

# 确保排名是整数
df['Rank'] = df['Rank'].astype(int)

# 对数据按Rank列进行排序
df = df.sort_values(by='Rank')

# 进行对数转换
log_rank = np.log(df['Rank'])
log_percentage = np.log(df['Percentage'])

# 进行线性回归
X = log_rank.values.reshape(-1, 1)  # 转换为2D array
y = log_percentage.values
model = LinearRegression().fit(X, y)

# 从模型中提取参数
slope = model.coef_[0]
intercept = model.intercept_

# 计算R^2值
y_pred = model.predict(X)
r2 = r2_score(y, y_pred)

# 绘制图表
plt.figure(figsize=(10, 6))
# plt.plot(df['Rank'], 100 * df['Percentage'], 'ro', linestyle='none', markerfacecolor='none', label='Phase Three Observation')
# plt.plot(df['Rank'], 100 * np.exp(intercept + slope * log_rank), 'r-', alpha=0.6, label='Power-Law Fitted Curve')
plt.plot(df['Rank'], 100 * df['Percentage'], 'bo', linestyle='none', markerfacecolor='none', label='Phase One Observation')
plt.plot(df['Rank'], 100 * np.exp(intercept + slope * log_rank), 'b-', alpha=0.6, label='Power-Law Fitted Curve')

# 设置图表标题和坐标轴标签
plt.title('Rank-Size Distribution of Park Social Interaction')
plt.xlabel('Rank')
plt.ylabel('Social interaction intensity')

# 格式化纵轴为百分比形式
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y:.2f}%'))

# 格式化横轴为整数形式
plt.gca().xaxis.set_major_formatter(ScalarFormatter())

# 显示网格
plt.grid(True, which="both", ls="--")

# 添加图例和拟合方程及R^2值
plt.legend()
plt.text(5, 60, f'y = {100 * np.exp(intercept):.2f} * x^{slope:.2f}\n$R^2 = {r2:.2f}$', fontsize=12)

# 显示图表
plt.show()