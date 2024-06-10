# coding: utf-8
# 此代码为对测试图像的推理过程
import sys, os
sys.path.append(os.pardir)
import numpy as np
import pickle
from dataset.mnist import load_mnist
from common.functions import sigmoid, softmax


def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test


def init_network():  # 读入保存在pickle文件sample_weight.pkl中的学习到的权重参数。这个文件中以字典变量的形式保存权重和偏置参数。
    with open("sample_weight.pkl", 'rb') as f:  # rb：以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
        network = pickle.load(f)  # 反序列化后的Python对象。 .dump()：将Python对象序列化并写入到文件对象。
    return network


def predict(network, x):  # 预测函数的定义
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y


x, t = get_data()
network = init_network()
# batch_size = 100 批数量
accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network, x[i])
    p = np.argmax(y)  # 获取概率最高的元素的索引
    if p == t[i]:
        accuracy_cnt += 1
# for i in range(0, len(x), batch_size):  批处理代码
#     x_batch = x[i:i+batch_size]
#     y_batch = predict(network, x_batch)
#     p = np.argmax(y_batch,axis=1) 没有参数axis默认将数组展平。为0是在列中比较选出最大的行索引，为1是在行中比较选出最大的列索引。
#     accuracy_cnt += np.sum(p == t[i:i+batch_size])

print("Accuracy:" + str(float(accuracy_cnt) / len(x)))  # 比较神经网络所预测的答案和正确解标签，将回答正确的概率作为识别精度。
