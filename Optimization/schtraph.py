from sympy import sympify, solve, symbols, diff, Symbol, Eq
from math import sqrt, inf
symb = [Symbol('x'), Symbol('y')]
rk = [1, 2, 10, 100, 1000, 10e+10]


def f1(a, b):
    return func1.subs('x', a).subs('y', b)


def f2(a, b):
    return func2.subs('x', a).subs('y', b)


with open('m_inp.txt', 'r') as file:
    func1 = sympify(file.readline().strip())
    func2 = sympify(file.readline().strip())
    eps = float(file.readline())

    print('–'*20, '\nYour task:\n')
    print(f'F Function is {func1}, G function is {func2}, where eps is {eps}\n')
    print("–"*20, '\n')
    t = Symbol('t')
    p = t/2 * (func2 ** 2)
    func = sympify(func1 + p)

    print(f'Func is {func}')

    gradient = [diff(func, el) for el in symb]
    print(f'Gradient: x is {gradient[0]}, y is {gradient[1]}')
    res = solve((gradient[0], gradient[1]), ('x', 'y'))
    print(f'X is {res[symb[0]]}, Y is {res[symb[1]]}')

    k = 0
    print(f'Start')
    flag = 0
    mass = []
    while k <= len(rk):
        print(f'Step k = {k}\n', '–'*10)
        x, y = res[Symbol('x')].subs(Symbol('t'), rk[k]), res[Symbol('y')].subs(Symbol('t'), rk[k])
        print(f'x is {x}, y is {y}')
        t1 = p.subs([('x', x), ('y', y), ('t', rk[k])])
        print(f'P(x,y, rk) is {p}')
        print(f'P(x, y, rk) is {float(t1)}')
        f_t = func1.subs('x', x).subs('y', y) + t1
        if k == len(rk)-1:
            mass.append([k, inf, x, y, t1, f_t])
        else:
            mass.append([k, rk[k], x, y, t1, f_t])
        if t1 < eps:
            print(f'HERE!!!! {t1} and {eps}')
            ans = (x, y)
            break
        k += 1
        print('–'*10, '\n')


print('\n', '–'*20, '\nAnswer is:\n', '–'*20, '\n')
print('–'*70)
print('  k'.ljust(8),  '  rk'.ljust(10), '    x'.ljust(10), '    y'.ljust(10), ' P(x,y,r) ', " F(x,y,r)", sep=' |', end='  |\n')
print('–'*70)

for i in range(len(mass)):
    for j in range(len(mass[i])):
        print(str(round(float(mass[i][j]), 4)).ljust(7), end='  |  ')
    print()
print('–'*70)
print(f'Answer is ({ans[0]}, {ans[1]})')
