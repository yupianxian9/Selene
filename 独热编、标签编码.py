"""
独热编码（One-Hot Encoding）是一种处理分类数据的常用方法，它将分类变量转换为一系列二进制特征向量。
每个分类值都被表示为一个二进制向量，该向量中只有一个元素为1，其余元素为0，这个1表示该特征的存在
独热编码的原理是将分类变量（或称为离散特征、无序特征）转换为一种适合机器学习算法处理的格式。
这样做的目的是为了让机器学习算法能够理解分类数据的结构，并且能够根据每个类别的特征进行预测
"""
"""
#法一
# 创建一个独热编码器
# sparse: 是否使用紧缩格式(稀疏矩阵),True为稀疏矩阵，False为密集矩阵
OHE = sp.OneHotEncoder(sparse =True,dtype=int)
# 对原始样本矩阵进行处理，返回独热编码后的样本矩阵。
result = OHE.fit_transform('原始样本矩阵')

#法二
OHE = sp.OneHotEncoder(sparse =True,dtype=int)
# 对原始样本矩阵进行训练，得到编码字典
encode_dict = OHE.fit(原始样本矩阵)
# 调用encode_dict字典的transform方法 对数据样本矩阵进行独热编码
result = encode_dict.transform(原始样本矩阵)
"""
import numpy as np
import sklearn.preprocessing as sp
samples=np.array([[2,3,5],
				[3,6,9],
				[2,6,5]])

OHE = sp.OneHotEncoder(dtype=int)
result = OHE.fit_transform(samples)
print(result)


"""标签编码（Label Encoding）是将分类特征的每个类别映射到一个唯一的整数。
这种方法在处理有序分类数据时非常有用，因为整数映射可以保留类别之间的顺序关系。
然而，对于无序的分类数据，使用标签编码可能会导致模型错误地认为不同的整数代表实际数值上的差异，这可能会影响模型的性能。"""
"""
# 创建 LabelEncoder 实例
LE = sp.LabelEncoder()

# 训练数据
data = ['low', 'medium', 'high', 'medium', 'low']

# 计算类别映射
LE.fit(data)

# 转换数据
encoded_data = LE.transform(data)

#根据标签编码的结果矩阵反査字典 得到原始數据矩阵
samples = LE.inverse_transform(result)
"""

samples1=np.array(['鼠','牛','虎','牛','龙','虎'])
LE = sp.LabelEncoder()
LE.fit(samples1)
encoded_data = LE.transform(samples1)
print(encoded_data)