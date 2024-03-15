# Вводится сначала число N — количество слов в словаре
# Далее идет N строк со словами из словаря. Все слова состоят из маленьких и заглавных латинских букв. В каждом слове заглавная ровно одна буква — та, на которую попадает ударение. Слова в словаре расположены в алфавитном порядке. Если есть несколько возможностей расстановки ударения в одном и том же слове, то эти варианты в словаре идут в произвольном порядке.
# Далее идет упражнение, выполненное некоторым человеком. Текст состоит из слов, которые разделяются между собой ровно одним пробелом. Все слова состоят из маленьких и заглавных латинских букв (заглавными обозначены те буквы, над которыми поставлено ударение).
# Выведите количество ошибок в тексте.


with open('inp_str.txt', 'r') as file, open('test_inp.txt', 'r') as file_test:
    n = int(file.readline())
    items = []
    for i in range(n):
        tmp = file.readline().split()
        for el in tmp:
            tmp_w = [k for k in el if k.isupper()][0]
            items.append((el.lower(), tmp_w))
    items.sort()
    dictionary = dict(items)
    file.readline()
    test = []
    for string in file_test.readlines():
        test.extend(string.split())

    err = 0
    for el in test:
        if dictionary.get(el.lower(), False):
            word = [k for k in el if k.isupper()][0]
            if word != dictionary[el.lower()]:
                err += 1
                print(el, word, dictionary[el.lower()])

    print(f'Number of text errors {err}')
