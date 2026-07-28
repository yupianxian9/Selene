
import sklearn.linear_model as lm
import sklearn.metrics as sm
import numpy as np 
import matplotlib.pyplot as plt

'''
#创建模型
model = lm.LinearRegression()
# 训练模型
# 输入为一个二维数组表示的样本矩阵输出为每个样本最终的结果
# 通过梯度下降法计算模型参数
mode1.fit(输入，输出)  

# 预测输出
# 输入array是一个二维数组，每一行是一个样本，每一列是一个特征。
result = model.predict(array)
'''


'''
线性回归模型评估
import sklearn.metrics as sm
#平均绝对值误差:1/mz|实际输出-预测输出
sm.mean_absolute_error(y, pred_y)
#平均平方误差:SQRT(1/mz(实际输出-预测输出)^2)
sm.mean_squared_error(y, pred_y)
# 中位绝对值误差:MEDIAN(实际输出-预测输出I)
sm.median_absolute_error(y, pred_y)
# R2得分，(0,1]区间的分值。分数越高，误差越小。
sm.r2_score(y,pred_y)
'''

x=np.array([1,3,5,7,9,11,13,15])
y=np.array([2,5,9,10,15,18,20,27])

#绘制画布
plt.figure(figsize=(10, 6), dpi=100,facecolor='lightgray')

#设置总标题及轴标题
plt.title('LinearRegression')
plt.xlabel('x')
plt.ylabel('y')

#设置散点图
plt.scatter(x,y)
#设置回归线
x=x.reshape(-1,1) #将数组x重塑为一个二维数组，其中每个元素都变成了一个单独的行向量。
model = lm.LinearRegression()
model.fit(x,y)
pred_y=model.predict(x)
plt.plot(x,pred_y)
plt.show()

#平均绝对值误差:1/mz|实际输出-预测输出
mae=sm.mean_absolute_error(y, pred_y)
#平均平方误差:SQRT(1/mz(实际输出-预测输出)^2)
mse=sm.mean_squared_error(y, pred_y)
# 中位绝对值误差:MEDIAN(实际输出-预测输出I)
medae=sm.median_absolute_error(y, pred_y)
# R2得分，(0,1]区间的分值。分数越高，误差越小。
r2=sm.r2_score(y,pred_y)

print(f'平均绝对值误差:{mae},平均平方误差:{mse},中位绝对值误差:{medae},R2得分:{r2}.')