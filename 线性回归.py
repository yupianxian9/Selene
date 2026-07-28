import numpy as np
import matplotlib.pyplot as plt

#matplotlib中文设置
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

#利用梯度下降求线性回归的斜率w1和截距w0

#设定x，y样本点
train_x=np.array([0.5,0.6,0.8,1.1,1.4])
train_y=np.array([5.0,5.5,6.0,6.8,7.0])
times= 1000	#循环次数
w0,w1=1,1 #初始化参数
lrate =0.01 #设置学习率

w0_list=[]
w1_list=[]
loss_list=[]
# 梯度下降
for i in range(1, times + 1):
    # 计算预测值
    y_pred = w0 + w1 * train_x
    
    # 计算损失函数（均方误差MSE）
    loss = np.mean((y_pred - train_y) ** 2)
    
    # 求损失函数关于w0与w1的偏导数
    do = np.sum(2 * (y_pred - train_y))
    d1 = np.sum(2 * (y_pred - train_y) * train_x)
    
    # 更新模型参数
    w0 -= lrate * do
    w1 -= lrate * d1

    #收集w0,w1,loss
    w0_list.append(w0)
    w1_list.append(w1)
    loss_list.append(loss)

    # 打印损失函数值
    if i % 100 == 0:
        print(f"Iteration {i}: w0 = {w0}, w1 = {w1}, Loss = {loss}")

# 绘制原始数据点
plt.scatter(train_x, train_y, color='pink', label='Original data')

# 绘制线性回归线
x_line = np.linspace(min(train_x), max(train_x), 100)
y_line = w0 + w1 * x_line
plt.plot(x_line, y_line, label='Linear regression')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression using Gradient Descent')
plt.legend()
plt.show()


#绘制w0,w1,loss变化图

times_list=[i for i in range(1,1001)]

#3行1列第一个图形,w0
plt.subplot(5, 1, 1)
plt.plot(times_list,w0_list,color='blue')
plt.title('w0')

#3行1列第二个图形,w1
plt.subplot(5, 1, 3)
plt.plot(times_list,w1_list,color='blue')
plt.title('w1')

#3行1列第二个图形,w1
plt.subplot(5, 1, 5)
plt.plot(times_list,loss_list,color='green')
plt.title('loss')

plt.show()

#找到w0和w1的坐标点

# 当你有两个或更多的一维数组时，np.meshgrid 可以生成一个坐标矩阵，
# 其中每个矩阵的行对应一个一维数组的所有元素，列对应另一个一维数组的所有元素。

# np.linspace 是 NumPy 库中的一个函数，用于在指定的区间内生成等间隔的数值。
w0_grid, w1_grid = np.meshgrid(np.linspace(min(w0_list), max(w0_list), 100), 
                               np.linspace(min(w1_list), max(w1_list), 100))

# 预测函数
def predict(w0, w1, x):
    return w0 + w1 * x

# 计算网格上的损失
loss_grid = np.zeros_like(w0_grid) #zeros_like用于创建一个与给定数组形状和类型相同、但所有元素都为零的新数组。
for i in range(w0_grid.shape[0]):
    for j in range(w0_grid.shape[1]):
        w0_val, w1_val = w0_grid[i, j], w1_grid[i, j]
        y_pred = predict(w0_val, w1_val, train_x)
        loss_grid[i, j] = np.mean((y_pred - train_y) ** 2)



# 创建一个新的画布
# figsize: 一个元组，指定画布的宽度和高度（英寸）。默认值通常是(6, 4)。
# dpi: 画布的分辨率，以每英寸点数（dots per inch）表示。
#facecolor为背景色
plt.figure(figsize=(10, 6), dpi=100,facecolor='lightgray')

#设置总标题及轴标题
plt.title('线性回归等高线图')
plt.xlabel('w0')
plt.ylabel('w1')

"""
plt.contour(X, Y, Z, levels=5)
plt.contourf(X, Y, Z, levels=5, cmap='jet')

X, Y: 这两个参数定义了网格的x和y坐标。
Z: 这是一个二维数组，其中包含了在X, Y网格点上计算出的函数值。
levels: 这个参数定义了等高线的数量和位置。可以是一个数字，表示等高线的数量，也可以是一个列表，指定具体的等高线值。
cmap: 这个参数定义了用于着色的颜色映射。
cmap参数用于指定颜色映射（colormap），它定义了数据值到颜色的映射规则。
'jet'是一个常用的颜色映射，它提供了一种从蓝色到红色的颜色渐变，中间通过绿色和黄色过渡。
'viridis': 从黄色到黑色
'plasma': 从黄色到红色
'inferno': 从黑色到黄色再到红色
'cividis': 从蓝色到绿色再到黄色
'gray': 灰度映射
"""

#contour函数用于绘制等高线图，它生成的是等高线的线条，而不是填充的区域。
cntr=plt.contour(w0_grid, w1_grid, loss_grid, levels=9)
plt.contourf(w0_grid, w1_grid, loss_grid, levels=9,cmap='jet')

#绘制网格线

# 添加定制的网格线plt.grid()
# b: 布尔值，指定是否绘制网格线，默认为 True。
# which: 字符串，可以是 'major', 'minor', 或 'both'，指定是绘制主刻度线、次刻度线，还是两者都绘制。
# axis: 字符串，可以是 'x', 'y', 或 'both'，指定是在 x 轴、y 轴还是两者都添加网格线。
# color: 字符串或颜色代码，指定网格线的颜色。
# linestyle: 字符串，指定网格线的样式，如 '-' 表示实线，'--' 表示虚线。
# linewidth: 数值，指定网格线的宽度。
plt.grid(True, which='both', axis='both', color='r', linestyle='--', linewidth=0.5)


# 给等高线添加标签
plt.clabel(cntr, inline=True, fontsize=8,fmt='%.3f' )


#绘制w0,w1变化的折线图
plt.plot(w0_list,w1_list,linestyle='-', color='r', marker='o', markersize=8)

# 添加图例
plt.legend()

# 显示图表
plt.show()

#保存图像
#plt.savefig("plot.png")
