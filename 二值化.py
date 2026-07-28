"""
# 给出阈值，获取二值化器
bin = sp.Binarizer(threshold=阈值)
# 调用transform方法对原始样本矩阵进行一值化预处理操价
result= bin.transform(原始样本矩阵)
"""
#导入库
import numpy as np
import sklearn.preprocessing as sp
import matplotlib.pyplot as plt
from PIL import Image


#设定二值化器
# bin=sp.Binarizer(threshold=15)
# ary1=np.array([[11,15,21],[21,31,5],[22,12,33]])

# result=bin.transform(ary1)
# print(result)

#图片二值化
# 打开图像文件
lilith = Image.open('1.png')

# 转换为灰度图像
gray_image = lilith.convert('L')
#设定二值化器
bin1=sp.Binarizer(threshold=180)
result1=bin1.transform(gray_image) #需要二维数组才能处理
# print(result1)
plt.imshow(result1, cmap='gray')
plt.show()