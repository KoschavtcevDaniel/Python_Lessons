from sympy import sympify, solve, symbols, diff, Symbol
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
symb = ['x', 'y']


def f(a, b):
    return func.subs('x', a).subs('y', b)


with open('m_inp.txt', 'r') as file:
    func = sympify(file.readline().strip())
    tmp = file.readline().split()
    t0, t1 = float(tmp[0]), float(tmp[1])
    tmp = file.readline().split()
    eps1, eps2, m = float(tmp[0]), float(tmp[1]), int(tmp[2])

    print('–'*20, '\nYour task:\n')
    print(f'Function - {func} on ({t0},{t1}) where eps1 is {eps1}, eps2 is {eps2}, M is {m}\n')
    print("–"*20, '\n')

    gradient = [diff(func, el) for el in symb]
    print(f'Gradient: x is {gradient[0]}, y is {gradient[1]}')
    # tmp = [Symbol('x') - Symbol('t') * gradient[0], Symbol('x') - Symbol('t') * gradient[1]]
    # phi = func.subs('x', tmp[0]).subs('y', tmp[1])
    # print(f'phi is {phi}')
    # diff_phi = diff(phi, 't')
    # t_sym = solve(diff_phi, 't')[0]
    # t_sym = ((gradient[0])**2 + (gradient[1])**2)/(4*(gradient[0])**2 + 2*(gradient[0]*gradient[1]) + 2*(gradient[1])**2)
    t_sym = ((gradient[0])**2 + (gradient[1])**2)/(10*gradient[0]**2 - 2*gradient[0]*gradient[1] + 2*gradient[1]**2)

    k = 0
    print(f'Start')
    flag = 0
    while True:
        print(f'Step k = {k}\n', '–'*10)
        grad_calc = [el.subs('x', t0).subs('y', t1) for el in gradient]
        print(f'Calculated gradient is: ({grad_calc[0]}, {grad_calc[1]})')
        norm = sqrt(grad_calc[0]**2 + grad_calc[1]**2)
        print(f'Norm is {norm}, {norm} and {eps1}')
        if norm < eps1 or k >= m:
            ans = (t0, t1)
            break

        t = t_sym.subs('x', t0).subs('y', t1)
        print(f't is {t}')
        t0_n, t1_n = (t0 - t * grad_calc[0]), (t1 - t*grad_calc[1])
        print(f'x{k+1} is ({t0_n}, {t1_n})')
        print(f'norm(x1 - x0) = {sqrt((t0 - t0_n)**2 + (t1 - t1_n)**2)} and {eps2}')
        if sqrt((t0 - t0_n)**2 + (t1 - t1_n)**2) < eps2 and abs(f(t0, t1) - f(t0_n, t1_n)) < eps2:
            flag += 1
            if flag > 1:
                ans = (t0_n, t1_n)
                break
        k += 1
        t0, t1 = t0_n, t1_n
        print('–'*10, '\n')


print('–'*20, '\nAnswer is:\n')
print(f'x* is {ans}, f(x*) = {f(ans[0], ans[1])}')
print(f'Step is {k}')
print('\n', '–'*20)

x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
fnc = 5*x**2 + y**2 - x*y + x

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, fnc, label='Plot')
plt.show()