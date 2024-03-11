from math import sqrt


f = lambda x: x**2 + 4 * x + 5
a, b, l = -4, 6, 0.5
y0 = a + (3 - sqrt(5)) / 2 * (b - a)
z0 = a + b - y0
k = 2
y, z = y0, z0
print(f'y is {y}, z is {z}')
while True:
    print(f'k is {k}')
    print(f'f(y) is {f(y)}, f(z) is {f(z)}')
    if f(y) <= f(z):
        print('f(y) <= f(z)')
        b = z
        z = y
        y = a + b - z
        print(f'[a, b] is [{a}, {b}], y is {y}, z is {z}')
    else:
        print('f(y) > f(z)')
        a = y
        y = z
        z = a + b - y
        print(f'[a, b] is [{a}, {b}], y is {y}, z is {z}')
    if abs(b - a) < l:
        ans = (a + b) / 2
        break
    print('delta > l', '\n')
    k += 1

print('Answer is')
print(f'X is {ans}, f(x) = {f(ans)}')
print(f'N is {k}')
print(f'Interval is [{a}, {b}]')
print(f'Shod is {0.618 ** (k - 1)}')

