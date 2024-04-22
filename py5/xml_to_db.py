import sqlite3
import xml.dom.minidom

conn = sqlite3.connect('real_estate_agency.db')
cursor = conn.cursor()
xml_file = 'table.xml'
doc = xml.dom.minidom.parse(xml_file)
clients = doc.getElementsByTagName('record')

for client in clients:
    client_id = int(client.getElementsByTagName('id')[0].firstChild.nodeValue)
    first_name = client.getElementsByTagName('first_name')[0].childNodes[0].data
    last_name = client.getElementsByTagName('last_name')[0].childNodes[0].data
    passport = client.getElementsByTagName('passport')[0].childNodes[0].data
    ownership = client.getElementsByTagName('ownership')[0].childNodes[0].data
    cursor.execute("insert into Clients (id, first_name, last_name, passport, ownership) values (?, ?, ?, ?, ?)",
                   (client_id, first_name, last_name, passport))
conn.commit()
conn.close()