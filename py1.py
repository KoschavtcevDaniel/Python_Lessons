s = input().rstrip('.').replace(' ', '').lower()
f_s = ''
e_s = ''
spec = ''
flag = 0
for el in s:
    if el not in s:
        continue
    if s.count(el) % 2 != 0:
        flag += 1
        if flag > 1:
            break
        spec = el * s.count(el)
        s = s.replace(el, '', s.count(el))
    else:
        f_s += el
        e_s += el
        s = s.replace(el, '', 2)
if flag > 1:
    print("NO Answer :( It's impossible")
else:
    print(f"He-he it's possible {(f_s + spec + e_s[::-1]).upper()}")

