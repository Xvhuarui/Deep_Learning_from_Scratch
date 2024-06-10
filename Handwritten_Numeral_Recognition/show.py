import sys, os
import numpy as np
from PIL import Image

sys.path.append(os.pardir)  # 将父目录的路径添加到sys.path中。这可能是因为你希望在当前脚本或程序中导入父目录中的模块，而默认情况下Python不会在父目录中查找模块。
from dataset.mnist import load_mnist  # load_mnist函数以“(训练图像 ,训练标签 )，(测试图像，测试标签 )”的形式返回读入的MNIST数据。

# 第一次调用会花费几分钟 ……
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True,normalize=False)
# flatten=True: 表示是否将图像展平为一维数组。如果为True，每个图像将从28x28的矩阵变为长度为784的一维数组。
# normalize=False: 表示是否对图像进行归一化处理。如果为True，图像的像素值将被缩放到0到1之间。
# “one_hot_label=False”第3个参数one_hot_label设置是否将标签保存为one-hot表示（one-hot representation）。
# one-hot表示是仅正确解标签为1，其余皆为0的数组，如[0,0,1,0,0,0,0,0,0,0]这样。当one_hot_label为False时，只是像7、2这样简单保存正确解标签；
# 当one_hot_label为True时，标签则保存为one-hot表示。未设定则默认将标签以非独热编码（non-one-hot-label）的形式返回。

# 输出各个数据的形状，利用上一节3层神经网络的实现进行理解输入数据各个维度的要求。
print(x_train.shape)  # (60000, 784)
print(t_train.shape)  # (60000,)
print(x_test.shape)  # (10000, 784)
print(t_test.shape)  # (10000,)


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


img = x_train[0]
label = t_train[0]
print(label)  # 5
print(img.shape)  # (784,)
img = img.reshape(28, 28)  # 把图像的形状变成原来的尺寸
print(img.shape)  # (28, 28)
img_show(img)
# 要注意的是，flatten=True时读入的图像是以一列（一维）NumPy数组的形式保存的。
# 因此，显示图像时，需要把它变为原来的28像素 × 28像素的形状。
# 可以通过reshape()方法的参数指定期望的形状，更改NumPy数组的形状。
# 此外，还需要把保存为NumPy数组的图像数据转换为PIL用的数据对象，这个转换处理由Image.fromarray()来完成。
