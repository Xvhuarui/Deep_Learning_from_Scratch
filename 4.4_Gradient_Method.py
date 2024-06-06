import numpy as np


# 梯度计算
def numerical_gradient(f, x):  # f为函数，x为NumPy数组
    h = 1e-4
    grad = np.zeros_like(x)  # 生成和x形状相同的数组
    for idx in range(x.size):
        tmp_val = x[idx]
        # f(x+h)的计算
        x[idx] = tmp_val + h
        fxh1 = f(x)
        # f(x-h)的计算
        x[idx] = tmp_val - h
        fxh2 = f(x)
        grad[idx] = (fxh1 - fxh2) / (2 * h)
        x[idx] = tmp_val  # 还原值
    return grad


# 梯度下降法
def gradient_descent(f, init_x, lr=0.01, step_num=100):  # init_x为初始值，lr为学习率learning rate，step_num为梯度法的重复次数
    x = init_x
    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad
    return x
