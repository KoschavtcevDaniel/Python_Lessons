import sqlite3
conn=sqlite3.connect("real_estate_agency.db")
cursor=conn.cursor()
cursor.execute("select id, first_name from Clients")
clients=cursor.fetchall()
rendered_clients=""
for client in clients:
    rendered_clients += f"""
        <option value="{client[0]}">{client[1]}</option>""" + "\n"

cursor.execute("select id, house from Realty")
objects = cursor.fetchall()
rendered_object=""
for object in objects:
    rendered_object += f"""
        <option value="{object[0]}">{object[1]}</option>""" + "\n"
conn.close()
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="UTF-8">
            <title></title>
        </head>
        <body style = "background-color: #ffe5b4">""")
print(
    f"""<h1>Clients</h1>
 <form action ="/cgi-bin/main.py">
  Client id <select name = "client_id">
    {rendered_clients}
  </select>
  Object id <select name = "object_id">
  {rendered_object}
  </select>
  Date <input type ="date" name ="date">
  Payment <input type ="number" name ="payment">
  <input type ="submit">
 </form></body></html>"""
)