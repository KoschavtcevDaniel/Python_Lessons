import sqlite3
import xml.dom.minidom


con = sqlite3.connect('db01.db')
cur = con.cursor()
# cur.execute('CREATE TABLE IF NOT EXISTS clients'
#             '(id INTEGER PRIMARY KEY,'
#             'fullname VARCHAR2,'
#             'tel VARCHAR2)')
# cur.execute('CREATE TABLE IF NOT EXISTS trainers'
#             '(id INTEGER PRIMARY KEY,'
#             'fullname VARCHAR2,'
#             'tel VARCHAR2,'
#             'point INTEGER)')
# cur.execute('CREATE TABLE IF NOT EXISTS trainings'
#             '(id INTEGER PRIMARY KEY,'
#             'date DATE,'
#             'client_id INTEGER REFERENCES clients(id),'
#             'trainer_id INTEGER REFERENCES trainers(id))')
# var_list = [("Gaivoronskiy Oleg", "88005557575"),
#             ("Korito Obiknovennoe", "89575542375"),
#             ("Daynigga Yakov", "88888888888")]
# sql = '''INSERT INTO clients (fullname, tel) VALUES(?,?)'''
# cur.executemany(sql, var_list)
# var_list = [("Bragin Sergei", "84004446565", 4),
#             ("Airat Gaziev", "83221992321", 5),
#             ("Wan Darkholm", "83003336363", 3)]
# sql = '''INSERT INTO trainers (fullname, tel, point) VALUES (?,?,?)'''
# cur.executemany(sql, var_list)
# var_list = [("2024-04-07", 1, 2),
#             ("2024-05-07", 2, 1),
#             ("2024-03-07", 3, 3)]
# sql = '''INSERT INTO trainings (date, client_id, trainer_id) VALUES (?,?,?)'''
# cur.executemany(sql, var_list)
cur.execute('SELECT * FROM clients')
clients = cur.fetchall()
keys = ["id", 'fullname', 'tel']
clients = list(map(lambda x: dict((keys[i], v) for i, v in enumerate(x)), clients))
cur.execute('SELECT * FROM trainers')
trainers = cur.fetchall()
keys = ["id", 'fullname', 'tel', 'point']
trainers = list(map(lambda x: dict((keys[i], v) for i, v in enumerate(x)), trainers))
cur.execute('SELECT * FROM trainings')
trainings = cur.fetchall()
keys = ["id", 'date', 'client_id', 'trainer_id']
trainings = list(map(lambda x: dict((keys[i], v) for i, v in enumerate(x)), trainings))

# Создаем XML-документ
doc = xml.dom.minidom.Document()
# Создаем корневой элемент
root = doc.createElement('clients')
doc.appendChild(root)
for row in clients:
    record = doc.createElement('client')
    root.appendChild(record)

    for key, value in row.items():
        element = doc.createElement(key)
        element.appendChild(doc.createTextNode(str(value)))
        record.appendChild(element)

with open('clients.xml', 'w') as f:
    f.write(doc.toprettyxml())

# Создаем XML-документ
doc = xml.dom.minidom.Document()
# Создаем корневой элемент
root = doc.createElement('trainers')
doc.appendChild(root)
for row in trainers:
    record = doc.createElement('trainer')
    root.appendChild(record)

    for key, value in row.items():
        element = doc.createElement(key)
        element.appendChild(doc.createTextNode(str(value)))
        record.appendChild(element)

with open('trainers.xml', 'w') as f:
    f.write(doc.toprettyxml())

# Создаем XML-документ
doc = xml.dom.minidom.Document()
# Создаем корневой элемент
root = doc.createElement('trainings')
doc.appendChild(root)
for row in trainings:
    record = doc.createElement('training')
    root.appendChild(record)

    for key, value in row.items():
        element = doc.createElement(key)
        element.appendChild(doc.createTextNode(str(value)))
        record.appendChild(element)

with open('trainings.xml', 'w') as f:
    f.write(doc.toprettyxml())

con.commit()
cur.close()

con = sqlite3.connect('db01.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS clients2')
cur.execute('DROP TABLE IF EXISTS trainers2')
cur.execute('DROP TABLE IF EXISTS trainings2')
cur.execute('CREATE TABLE IF NOT EXISTS clients2'
            '(id INTEGER PRIMARY KEY,'
            'fullname VARCHAR2,'
            'tel VARCHAR2)')
cur.execute('CREATE TABLE IF NOT EXISTS trainers2'
            '(id INTEGER PRIMARY KEY,'
            'fullname VARCHAR2,'
            'tel VARCHAR2,'
            'point INTEGER)')
cur.execute('CREATE TABLE IF NOT EXISTS trainings2'
            '(id INTEGER PRIMARY KEY,'
            'date DATE,'
            'client_id INTEGER REFERENCES clients2(id),'
            'trainer_id INTEGER REFERENCES trainers2(id))')

xml_file = 'clients.xml'
doc = xml.dom.minidom.parse(xml_file)
users = doc.getElementsByTagName('client')

for user in users:
    user_id = user.getElementsByTagName('id')[0].childNodes[0].data
    name = user.getElementsByTagName('fullname')[0].childNodes[0].data
    tel = user.getElementsByTagName('tel')[0].childNodes[0].data
    var_list = [(user_id, name, tel)]
    sql = '''INSERT INTO clients2 (id, fullname, tel) VALUES(?, ?, ?)'''
    cur.executemany(sql, var_list)
cur.execute('SELECT * FROM clients2')
clients = cur.fetchall()
print(clients)

xml_file = 'trainers.xml'
doc = xml.dom.minidom.parse(xml_file)
users = doc.getElementsByTagName('trainer')

for user in users:
    user_id = user.getElementsByTagName('id')[0].childNodes[0].data
    name = user.getElementsByTagName('fullname')[0].childNodes[0].data
    tel = user.getElementsByTagName('tel')[0].childNodes[0].data
    point = user.getElementsByTagName('point')[0].childNodes[0].data
    var_list = [(user_id, name, tel, point)]
    sql = '''INSERT INTO trainers2 (id, fullname, tel, point) VALUES(?, ?, ?, ?)'''
    cur.executemany(sql, var_list)
cur.execute('SELECT * FROM trainers2')
clients = cur.fetchall()
print(clients)

xml_file = 'trainings.xml'
doc = xml.dom.minidom.parse(xml_file)
users = doc.getElementsByTagName('training')

for user in users:
    user_id = user.getElementsByTagName('id')[0].childNodes[0].data
    date = user.getElementsByTagName('date')[0].childNodes[0].data
    c_id = user.getElementsByTagName('client_id')[0].childNodes[0].data
    t_id = user.getElementsByTagName('trainer_id')[0].childNodes[0].data
    var_list = [(user_id, date, c_id, t_id)]
    sql = '''INSERT INTO trainings2 (id, date, client_id, trainer_id) VALUES(?, ?, ?, ?)'''
    cur.executemany(sql, var_list)
cur.execute('SELECT * FROM trainings2')
clients = cur.fetchall()
print(clients)

con.commit()
con.close()