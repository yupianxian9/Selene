import numpy as np
import sklearn.tree as st
import sklearn.metrics as sm
import sklearn.ensemble as se

# 设置随机种子以确保结果可复现
np.random.seed(7)

# 生成随机数据集
# 假设我们有10个特征和100个样本
n_samples = 100
n_features = 10
X = np.random.rand(n_samples, n_features)
y = np.random.randint(2, size=n_samples)  # 二分类问题

# 划分训练集和测试集
train_size = int(len(X) * 0.8)
train_x, test_x = X[:train_size], X[train_size:]
train_y, test_y = y[:train_size], y[train_size:]

# 创建决策树模型
#回归算法为：DecisionTreeRegressor
tree_model = st.DecisionTreeClassifier(max_depth=4)
tree_model.fit(train_x, train_y)

# 预测测试集
tree_pred = tree_model.predict(test_x)

# 评估决策树模型
print("决策树模型 - 准确率:", sm.accuracy_score(test_y, tree_pred))

# 使用AdaBoost进行正向激励，指定SAMME算法
#AdaBoostRegressor为回归算法
ada_model = se.AdaBoostClassifier(st.DecisionTreeClassifier(max_depth=4), 
                                  n_estimators=300, 
                                  algorithm='SAMME', 
                                  random_state=7)
ada_model.fit(train_x, train_y)

# 预测测试集
ada_pred = ada_model.predict(test_x)

# 评估AdaBoost模型
print("AdaBoost模型 - 准确率:", sm.accuracy_score(test_y, ada_pred))