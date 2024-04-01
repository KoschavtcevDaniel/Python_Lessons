import cgi
import sqlite3
from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler
con = sqlite3.connect('db01.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS sightseeings'
            '(id INTEGER PRIMARY KEY,'
            'name VARCHAR2,'
            'country VARCHAR2)')
cur.execute('CREATE TABLE IF NOT EXISTS men'
            '(id INTEGER PRIMARY KEY,'
            'fio VARCHAR2,'
            'place_of_birth VARCHAR2)')
cur.execute('CREATE TABLE IF NOT EXISTS tourisms'
            '(id INTEGER PRIMARY KEY,'
            'id_obj INTEGER REFERENCES sightseeings(id),'
            'id_man INTEGER REFERENCES men(id),'
            'data DATE)')
var_list = [(1,1,1,"16-09-2023"),
            (2,2,1,"15-09-2021"),
            (3,2,2,"14-10-2020")]
sql='''INSERT INTO tourisms (id, id_obj, id_man, data) VALUES(?,?,?,?)'''
cur.executemany(sql,var_list)
var_list = [(1, "Everest", "China"),
            (2, "Syberia", "Russia")]
sql='''INSERT INTO sightseeings (id, name, country) VALUES (?,?,?)'''
cur.executemany(sql,var_list)
var_list =[(1,"Makarchuk Anton Pavlovich", "Russia"),
           (2, "Pavlova Alla Vladimirovna", "Russian Empire")]
sql='''INSERT INTO men (id, fio, place_of_birth) VALUES (?,?,?)'''
cur.executemany(sql,var_list)
cur.execute('SELECT * FROM men')
print(cur.fetchall())