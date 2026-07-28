# 岭回归
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import Ridge
from sklearn.datasets import make_regression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# 生成模拟数据
x=np.array([0.5,0.6,0.8,1.1,1.4])
y=np.array([5.0,5.5,6.0,6.8,7.0])

# 将数据划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
X_train=X_train.reshape(-1,1)
y_train=y_train.reshape(-1,1)
X_test=X_test.reshape(-1,1)
y_test=y_test.reshape(-1,1)
# 创建岭回归模型
ridge = Ridge(alpha=1.0)

# 训练模型
ridge.fit(X_train, y_train)

# 预测
y_pred = ridge.predict(X_test)

# 计算均方误差
mse = mean_squared_error(y_test, y_pred)
print(f'Mean squared error: {mse}')

# 查看回归系数
print(f'Coefficients: {ridge.coef_}')

# 设置不同的alpha值
alphas = [0.001, 0.01, 0.1, 1, 10, 100]

# 存储每个alpha的交叉验证分数
scores = []

for alpha in alphas:
    ridge = Ridge(alpha=alpha)
    #cross_val_score用于通过交叉验证评估机器学习模型的性能。
    score = cross_val_score(ridge, X_train, y_train, scoring='neg_mean_squared_error', cv=4)
    scores.append(score.mean())

# 找到最佳的alpha值
#np.argmax 是 NumPy 库中的一个函数，用于返回数组中最大值的索引
best_alpha = alphas[np.argmax(scores)]
print(f'Best alpha: {best_alpha}')

# 使用最佳alpha值重新训练模型
best_ridge = Ridge(alpha=best_alpha)
best_ridge.fit(X_train, y_train)
y_pred_best = best_ridge.predict(X_test)

# 评估最佳模型
mse_best = mean_squared_error(y_test, y_pred_best)
print(f'Mean squared error with best alpha: {mse_best}')
