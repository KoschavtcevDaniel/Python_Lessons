def fibonacci(tmp):
    t1, t2 = 1, 1
    mass = [t1, t2]
    while True:
        mass.append(t1+t2)
        t1, t2 = t2, t1+t2
        if t1+t2 > tmp:
            mass.append(t1+t2)
            break
    return mass


f = lambda x: x**2 + 4 * x + 5
a, b, l, eps = -4, 6, 0.5, 0.01
n = 2
tm = (b - a) / l
fib = fibonacci(tm)
p = len(fib) - 1
print(f'fib for K is {tm} is {fib}')
print(f'Length fibonacci {p}')
k = 0
while True:
    print(f'\n Step {k}')
    y = a + fib[p - 2 - k] / fib[p - k] * (b - a)
    z = a + fib[p - 1 - k] / fib[p - k] * (b - a)
    print(f'y is {y}, z is {z}')
    if f(y) <= f(z):
        b = z
    else:
        a = y
    print(f'f(y) = {f(y)} and f(z) = {f(z)} on [{a}, {b}]')
    if k == p - 3:
        print('\n!!!Warning!!!')
        z = y + eps
        print(f'y is {y}, z is {z}')
        print(f'f(y) = {f(y)} and f(z) = {f(z)}')
        if f(y) <= f(z):
            b = z
        else:
            a = y
        print(f'Otrezok [{a}, {b}]')
    if abs(b - a) < l:
        ans = (b + a) / 2
        break
    k += 1

print('\n------------ANSWER--------------\n')
print(f'x is {ans} and f(x) is {f(ans)}')
print(f'Otrezok [{a}, {b}]')
print(f'Step is {k + 1}')
print(f'R(N) = {1 / fib[p]}')
print('\n------------------------------------')

