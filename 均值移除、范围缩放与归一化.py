#导入库
import numpy as np
import sklearn.preprocessing as sp

#1.均值移除scale
raw_sample=np.array([[17,90,4000],[20,80,5000],[21,85,4500]])
reasult=sp.scale(raw_sample)
# print(reasult)


#2.范围缩放（多为列处理）
#例如，将一组数缩放为0-1间
raw_array=np.array([[17,39,23],[23,33,45],[22,31,29]])

# 创建MinMax缩放器
#feature_range=(0, 1)是MinMaxScaler的一个参数，指定了缩放后的特征值是(0, 1)
mms = sp.MinMaxScaler(feature_range=(0,1))

# 调用mms对象的方法执行缩放操作，返回缩放过后的结果
#fit_transform方法首先计算训练数据的最小值和最大值，然后使用这些值来缩放数据
result1=mms.fit_transform(raw_array)
# print(result1)

"""
补充：lstsq方法,用于矩阵A*x=b计算,返回最小二乘解x
numpy.linalg.lstsq(a, b, rcond=None) 
a 是一个M×N 的数组，表示系数矩阵。
b 是一个 M×K 维的数组，表示结果向量或矩阵。
rcond 或 cond 是一个可选参数，用于确定奇异值的截断阈值。
"""

#范围缩放手动计算
#原理，利用A*x=B,设B为[0,1]以确定最大最小值的线性方程，中间的则直接代入方程

new_samples =[]
for row in raw_sample.T: #列为特征，需要缩放，所以要转置才能处理列
	min_val = row.min()
	max_val =row.max()
	#整理求出缩放线性关系所需要的矩阵:A与B
	A=np.array([[min_val,1],[max_val,1]])
	B=np.array([0,1])
	#x=np.linalg.lstsq(A，B)[0]   #法一
	x=np.linalg.solve(A,B)  #解出方程系数
	new_row =row* x[0]+ x[1] #代入方程得到新解
	new_samples.append(new_row) 
	print(np.array(new_samples).T)

#3.归一化,normalize方法（多为行处理）
#有些情况每个样本的每个特征值具体的值并不重要，但是每个样本特征值的占比更加重要。
#所以归一化即是用每个样本的每个特征值除以该样本各个特征值绝对值的总和（行处理）
#变换后的样本矩阵，每个样本的特征值绝对值之和为1。
"""
normalized_data = normalize(X, norm='l2', axis=1)
X：输入的数据，可以是一个列表、数组或者任何类似于数组的数据结构。
norm：指定规范化的方式。常见的取值有：
	'l1'：将每个样本的特征向量规范化，使得向量的 L1 范数（即向量元素绝对值的和）为 1。
	'l2'：将每个样本的特征向量规范化，使得向量的 L2 范数（即向量元素的平方和的平方根）为 1。这是默认值。
	'max'：将每个样本的特征向量规范化，使得向量的最大值为 1。
axis：指定沿着哪个轴进行规范化。
	axis=1 (默认）表示沿着每个样本（每行）进行规范化，
	axis=0 表示沿着特征（每列）进行规范化。
"""
result3=sp.normalize(raw_sample,norm='l1')
print(result3)