import numpy as np
A = np.array([[56.0, 0.0, 4.4, 68.0],
[1.2, 104.0, 52.0, 8.0],
[1.8, 135.0, 99.0, 0.9]])
print(A)
cal = A.sum(axis=0)
print(cal)
#不确定矩阵纬度的时候，会调用reshape
#广播会让计算过程中的矩阵拓展
percentage = 100 * A/cal.reshape(1,4)
print(percentage)