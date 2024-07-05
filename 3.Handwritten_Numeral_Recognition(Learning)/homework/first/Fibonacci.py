"""
a = 1
b = 1
for i in range(18):
    c = a + b
    a = b
    b = c
    if i >= 13:
        print(c)
"""

"""
def f(n,index):
    if index == 1 or index == 2:
        return 1

n = list()
n.append(1)
n.append(1)
for i in range(20):
    if i<2:
        continue
    else:
        temp = n[i-1]+n[i-2]
        n.append(temp)
print(n)
"""

# 终止条件
# f(0) = 1,f(1) = 1
# 方程
# f(n) = f(n-1) + f(n-2)


def f(n):  # 定义fibonacci函数
    if n == 1 or n == 0:  # 定义终止条件
        return 1
    return f(n-1) + f(n-2)  # 定义方程


temp = list()  # 创建列表
for i in range(20):  # 循环加入列表
    if i < 15:  # 从15开始加入
        continue
    temp.append(f(i))
print(temp)  # 输出
