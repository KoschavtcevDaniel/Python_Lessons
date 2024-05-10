# import csv
#
# df = csv.reader('csv/15 - 1.csv', delimiter=',')
# c = 0
#
# for row in df:
#     print(row)

#Найти количество людей, фамилии которых начинаются с заданной буквы, которые прошли тест меньше, чем за заданное время. Вывести их список

import csv
dc = {'дн': lambda x: x * 24 * 60 * 60, 'час': lambda x: x * 60 * 60, 'ч': lambda x: x * 60 * 60, 'мин': lambda x: x * 60, 'сек': lambda x: x}


def its_time_to_stop(t):
    if tm == '':
        return 10e+10
    tmp = [g.split(' ') for g in t.split('. ')]
    res = 0
    for rw in tmp:
        res += dc.get(rw[1].strip('., '), 0)(int(rw[0]))
    return res


with open("csv/15 - 2.csv", encoding='utf-8') as file:
    file_reader = csv.reader(file, delimiter=",")
    c = 0
    # Считывание данных из CSV файла
    temp = []
    for row in file_reader:
        if c == 0:
            col = row
            c += 1
        else:
            temp.append(row)

    val = [[0 for _ in range(len(temp))] for _ in range(len(temp))]
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            val[j][i] = temp[i][j]

    base = dict(zip(col, val))
    print(base)

    w, time = input(), int(input())
    lst = set()
    cnt = 0
    for name, tm in zip(base['Фамилия'], base['Затраченное время']):
        fl = 0
        if name[0].lower() == w.lower():
            fl += 1
        if its_time_to_stop(tm) < time:
            fl += 1
        if fl > 1:
            cnt += 1
            lst.add(name)
    print(f'Всего {cnt} чел:')
    print(*lst, sep='\n')
