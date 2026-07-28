#导入库
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 生成模拟数据
np.random.seed(0)
X = np.sort(np.random.rand(100, 1) * 5, axis=0)
y = np.sin(X).ravel() + np.random.randn(100) * 0.2


# 构建多项式回归模型的管线
degree = 6  # 多项式的度数
pipeline = Pipeline([
    ("poly_features", PolynomialFeatures(degree=degree)),
    ("lin_reg", LinearRegression())
])

# 分割数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 训练模型
pipeline.fit(X_train, y_train)

# 预测
y_pred = pipeline.predict(X_test)

# 计算模型性能
print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred))

#分割500个点
x1=np.linspace(X.min(),X.max(),500)
x1=x1.reshape(-1,1)
y1=pipeline.predict(x1)
# 可视化结果
plt.scatter(X_test, y_test, color='black')
plt.plot(x1, y1, color='blue', linewidth=3)
plt.show()