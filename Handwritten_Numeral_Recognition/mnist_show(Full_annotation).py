# coding: utf-8
# 该代码为下载mnist数字数据集并测试是否下载成功
import sys, os  # 用于访问文件夹 sys：System os：Operation System
sys.path.append(os.pardir)  # 为了导入父目录的文件而进行的设定
# sys.path：是一个列表list,它里面包含了已经添加到系统的环境变量路径。当我们要添加自己的引用模块搜索目录时，可以通过列表list的append()方法。
# os.pardir：返回当前目录的父目录
import numpy as np
from dataset.mnist import load_mnist  # 从父文件夹dataset中的mnist.py导入load_mnist()函数
from PIL import Image  # 从PIL库导入Image类，PIL是Python Imaging Library的缩写，它是Python中用于图像处理的一个强大的库。


def img_show(img):  # 定义img_show()函数
    pil_img = Image.fromarray(np.uint8(img))  # 可以实现将numpy数组的图像数据转换为PIL用的数据对象
    # uint8是专门用于存储各种图像的（包括RGB，灰度图像等），范围是从0–255，大于255的值会被截断。
    pil_img.show()  # 显示图像

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)  # （训练图像， 训练标签），（测试图像，测试标签）
# 开始下载mnist数据集，分为训练集和测试集：flatten设置是否展开输入图像变为一维数组；normalize设置是否将输入图像正规化为0.0~1.0的值。

img = x_train[0]  # 第一张训练图像测试
label = t_train[0]  # 第一张训练标签测试
print(label)  # 5

print(img.shape)  # (784,)  # 由于flatten为True所以将输入图像保存为28X28=784个元素构成的一维数组。img_shape默认读入三通道数。
img = img.reshape(28, 28)  # 把图像的形状变为原来的尺寸
print(img.shape)  # (28, 28)

img_show(img)  # 显示第一张训练图像
