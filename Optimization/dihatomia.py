import matplotlib.pyplot as plt
import numpy as np


a, b, eps, l = -4, 6, 0.2, 0.5
x_val = np.arange(a, b, eps)
y_val = x_val ** 2 + 4 * x_val + 5
k = 0
f = lambda x: x ** 2 + 4 * x + 5
while True:
    y = (a + b - eps) / 2
    z = (a + b + eps) / 2
    f1 = f(y)
    f2 = f(z)
    if f1 <= f2:
        b = z
    else:
        a = y
    if abs(b - a) < l:
        x = (a + b) / 2
        break
    else:
        k += 1

print('Answer is')
print(f'X is {x}, f(x) = {f(x)}')
print(f'N is {2 * (k + 1)}')
print(f'Interval is [{a}, {b}]')
print(f'Shod is {1 / 2 ** (2 * (k + 1))}')

plt.plot(x_val, y_val)
plt.scatter(x, f(x), c='red')
plt.xlabel('OX')
plt.ylabel("OY")
plt.show()