import cgi
import sqlite3
import xml.dom.minidom

form = cgi.FieldStorage()
text1 = form.getfirst("first_name", "")
text2 = form.getfirst("last_name", "")
text3 = form.getfirst("passport", "")
text4 = form.getfirst("house", "")
text5 = form.getfirst("status", "")
text6 = form.getfirst("client_id", 0)
text7 = form.getfirst("object_id", 0)
text8 = form.getfirst("date", "1111-11-11")
text9 = form.getfirst("payment", 0)
con = sqlite3.connect('real_estate_agency.db')
cur = con.cursor()

if text1 != "" or text2 != "" or text3 != "":
    var_list = [(text1, text2, text3)]
    sql = '''INSERT INTO Clients (first_name, last_name, passport) VALUES(?,?,?)'''
    cur.executemany(sql, var_list)
    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="cp1251">
            <title>client</title>
        </head>
        <body style = "background-color: #ffe5b4">""")
    print("<h1>Client</h1>")
    print("<p>First_name: {}</p>".format(text1))
    print("<p>Last_name: {}</p>".format(text2))
    print("<p>Passport: {}</p>".format(text3))
    print("""</body> </html>""")
    cur.execute('SELECT * FROM clients')
    print(cur.fetchall())

if text4 != "" or text5 != "":
    var_list = [(text4, text5)]
    sql = '''INSERT INTO Realty(house, status) VALUES(?,?)'''
    cur.executemany(sql, var_list)
    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="cp1251">
            <title>realty</title>
        </head>
        <body style = "background-color: #ffe5b4">""")
    print("<h1>Realty</h1>")
    print("<p>Object: {}</p>".format(text4))
    print("<p>Status: {}</p>".format(text5))
    print("""</body> </html>""")
    cur.execute('SELECT * FROM Realty')
    print(cur.fetchall())

if text6 != 0 or text7 != 0 or text8 != "1111-11-11" or text9 != 0:
    var_list = [(text6, text7, text8, text9)]
    sql = '''INSERT INTO Contracts (client_id, object_id, date, payment) VALUES(?,?,?,?)'''
    cur.executemany(sql, var_list)
    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="cp1251">
            <title>contract</title>
        </head>
        <body style = "background-color: #ffe5b4">""")
    print("<h1>Contracts</h1>")
    print("<p>Client_id: {}</p>".format(text6))
    print("<p>Object_id: {}</p>".format(text7))
    print("<p>Date: {}</p>".format(text8))
    print("<p>Payment: {}</p>".format(text9))
    print("""</body> </html>""")
    cur.execute('SELECT * FROM Contracts')
    print(cur.fetchall())
con.commit()
cur.close()
con.close()


