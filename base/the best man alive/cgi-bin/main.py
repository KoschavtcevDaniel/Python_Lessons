# f = open('input1.txt','r')
# set=set()
# for i in f.readline().split():
#     set.add(i)
# print(len(set))

# f = open('input2.txt','r')
# for line in f.readlines():
#     sum=0
#     for i in line.split():
#         while(" " in i):
#             i = i.strip()
#         sum+=int(i)
#     print(sum,sep='\n')

# for i in reversed(open('input4.txt','r').readlines()):
#     print(i,sep='')

# count_strings = 0
# count_letters = 0
# words=[]
# f = open('input5.txt','r')
# for line in f.readlines():
#     for i in line.split():
#         while not(i.isalpha()):
#             for j in i:
#                 if not(j.isalpha()):
#                     i = i.replace(j,"")
#         words.append(i)
#         for k in i:
#             count_letters+=1
#     count_strings+=1
# print(count_strings)
# print(len(words))
# print(count_letters)

# f = open('input6.txt','r')
# info = f.read()
# for i in reversed(info):
#     print(i,end="")

# import re
# a=input()
# first_word = re.findall(r'^\w+', a)
# print(first_word)

# import re
# a=input()
# last_word = re.findall(r'\w+$', a)
# print(last_word)

# import re
# for i in range(0,3):
#     a = input()
#     words=[]
#     words=re.findall(r'\bкот[^\w]',a)
#     if(len(words)!=0):
#         print(a)

# import re
# for i in range(0,3):
#     a=input()
#     words=[]
#     words=re.findall(r'кот',a)
#     if(len(words)>=2):
#         print(a)

# import re
# pat = re.compile(r'[AEYTOPHKXCBM][0-9]{3}[AEYTOPHKXCBM]{2}[0-9]{2,3}')
# for i in range(0,5):
#     a=input()
#     print(re.match(pat,a))
#
# N=int(input())
# a=input().split()
# for i in range(0,len(a)):
#     if(not(a[i].isalpha())):
#         a[i].strip(',')
#         a.pop(i)
# print(a)
# my_dict=dict()
# my_dict.update({a[0]:a[1:]})
# print(my_dict)

import cgi
import sqlite3
from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler
form = cgi.FieldStorage()
text1 = form.getfirst("id_obj","не задано")
text2 = form.getfirst("id_name", "не задано")
text3 = form.getfirst("data","не задано")
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
    <html>
    <head>
        <meta charset="cp1251">
        <title>Обработка мест</title>
    </head>
    <body>""")
print("<h1>Обработка мест</h1>")
print("<p>place: {}</p>".format(text1))
print("<p>Чувачок: {}</p>".format(text2))
print("<p>Дата: {}</p>".format(text3))
print("""</body> </html>""")