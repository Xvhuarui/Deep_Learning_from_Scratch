import numpy as np
import matplotlib.pylab as plt


def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c)  # 溢出对策
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


x = np.arange(-5.0, 5.0, 0.1)
y = softmax(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
