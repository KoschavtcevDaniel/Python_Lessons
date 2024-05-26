import sqlite3
import xml.dom.minidom


con = sqlite3.connect('real_estate_agency.db')
cur = con.cursor()
# cur.execute(
#     """create table if not exists Clients (
#         id INTEGER PRIMARY KEY,
#         first_name VARCHAR(30) not null,
#         last_name VARCHAR(30) not null,
#         passport VARCHAR(30) not null);""")
#
# cur.execute(
#     """create table if not exists Realty(
#         id INTEGER PRIMARY KEY,
#         house VARCHAR(30) not null,
#         status VARCHAR(100));""")
#
# cur.execute(
#     """create table if not exists Contracts (
#         contract INTEGER PRIMARY KEY,
#         client_id INTEGER not null,
#         object_id INTEGER not null,
#         date DATETIME not null,
#         payment FLOAT not null,
#         foreign key (client_id) references Clients (id),
#         foreign key (object_id) references Realty (id));""")
#
# var_list = [("Daniil", "Koshch", "0364123456"),
#             ("Andrei", "Kormiltcev", "0356691587"),
#             ("Anton", "Barsov", "0706154646"),
#             ("Marya", "Klarnet", "1306649255"),
#             ("Anna", "Zemelko", "0609135648")]
# sql = '''INSERT INTO Clients (first_name, last_name, passport) VALUES(?,?,?)'''
# cur.executemany(sql, var_list)
#
# var_list = [("st. Krasnay, 94", "Good"),
#             ("st. Barkof, 102/1", "Bad"),
#             ("st. Valisku, 456", "Good")]
# sql = '''INSERT INTO Realty (house, status) VALUES (?,?)'''
# cur.executemany(sql, var_list)
#
# var_list = [(0, 0, "2025-04-07", 2000000),
#             (1, 2, "2021-05-07", 3000000),
#             (2, 1, "2023-03-07", 2500000)]
# sql = '''INSERT INTO Contracts (client_id, object_id, date, payment) VALUES (?,?,?,?)'''
# cur.executemany(sql, var_list)

cur.execute('SELECT * FROM Clients')
clients = cur.fetchall()
print(clients)
keys = ["id", "first_name", "last_name", "passport"]
clients = list(map(lambda x: dict((keys[i], val) for i, val in enumerate(x)), clients))

cur.execute('SELECT * FROM Realty')
realty = cur.fetchall()
print(realty)
keys = ["id", "house", "status"]
realty = list(map(lambda x: dict((keys[i], val) for i, val in enumerate(x)), realty))

cur.execute('SELECT * FROM Contracts')
contracts = cur.fetchall()
print(contracts)
keys = ["contract", "client_id", "object_id", 'date', "payment"]
contracts = list(map(lambda x: dict((keys[i], val) for i, val in enumerate(x)), contracts))


doc = xml.dom.minidom.Document()    # Создаем XML-документ
root = doc.createElement('Clients')     # Создаем корневой элемент
doc.appendChild(root)
for row in clients:
    record = doc.createElement('Client')
    root.appendChild(record)

    for key, value in row.items():
        element = doc.createElement(key)
        element.appendChild(doc.createTextNode(str(value)))
        record.appendChild(element)

with open('Clients.xml', 'w') as f:
    f.write(doc.toprettyxml())

doc = xml.dom.minidom.Document()
root = doc.createElement('Realty')
doc.appendChild(root)
for row in realty:
    record = doc.createElement('Realty_object')
    root.appendChild(record)

    for key, value in row.items():
        element = doc.createElement(key)
        element.appendChild(doc.createTextNode(str(value)))
        record.appendChild(element)

with open('Realty.xml', 'w') as f:
    f.write(doc.toprettyxml())


doc = xml.dom.minidom.Document()
root = doc.createElement('Contracts')
doc.appendChild(root)
for row in contracts:
    record = doc.createElement('Contract')
    root.appendChild(record)

    for key, value in row.items():
        element = doc.createElement(key)
        element.appendChild(doc.createTextNode(str(value)))
        record.appendChild(element)

with open('Contracts.xml', 'w') as f:
    f.write(doc.toprettyxml())


con.commit()
cur.close()

con = sqlite3.connect('new_database.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS Clients_new')
cur.execute('DROP TABLE IF EXISTS Realty_new')
cur.execute('DROP TABLE IF EXISTS Contracts_new')

cur.execute('CREATE TABLE IF NOT EXISTS Clients_new'
            '(id INTEGER PRIMARY KEY,'
            "first_name VARCHAR(30) not null,"
            "last_name VARCHAR(30) not null,"
            "passport VARCHAR(30) not null)")
cur.execute('CREATE TABLE IF NOT EXISTS Realty_new'
            '(id INTEGER PRIMARY KEY,'
            "house VARCHAR(30) not null,"
            "status VARCHAR(100))")
cur.execute('CREATE TABLE IF NOT EXISTS Contracts_new'
            '(contract INTEGER PRIMARY KEY,'
            'client_id INTEGER not null,'
            'object_id INTEGER not null,'
            'date DATETIME not null,'
            'payment FLOAT not null,'
            'foreign key (client_id) references Clients (id),'
            'foreign key (object_id) references Realty (id))')

xml_file = 'Clients.xml'
doc = xml.dom.minidom.parse(xml_file)
users = doc.getElementsByTagName('Client')

for user in users:
    user_id = user.getElementsByTagName('id')[0].childNodes[0].data
    f_name = user.getElementsByTagName('first_name')[0].childNodes[0].data
    l_name = user.getElementsByTagName('last_name')[0].childNodes[0].data
    pas = user.getElementsByTagName('passport')[0].childNodes[0].data
    var_list = [(user_id, f_name, l_name, pas)]
    sql = '''INSERT INTO Clients_new (id, first_name, last_name, passport) VALUES(?, ?, ?, ?)'''
    cur.executemany(sql, var_list)
cur.execute('SELECT * FROM Clients_new')
clients = cur.fetchall()
print(clients)

xml_file = 'Realty.xml'
doc = xml.dom.minidom.parse(xml_file)
users = doc.getElementsByTagName('Realty_object')

for user in users:
    user_id = user.getElementsByTagName('id')[0].childNodes[0].data
    house = user.getElementsByTagName('house')[0].childNodes[0].data
    status = user.getElementsByTagName('status')[0].childNodes[0].data
    var_list = [(user_id, house, status)]
    sql = '''INSERT INTO Realty_new (id, house, status) VALUES(?, ?, ?)'''
    cur.executemany(sql, var_list)
cur.execute('SELECT * FROM Realty_new')
clients = cur.fetchall()
print(clients)

xml_file = 'Contracts.xml'
doc = xml.dom.minidom.parse(xml_file)
users = doc.getElementsByTagName('Contract')

for user in users:
    contract = user.getElementsByTagName('contract')[0].childNodes[0].data
    c_id = user.getElementsByTagName('client_id')[0].childNodes[0].data
    ob_id = user.getElementsByTagName('object_id')[0].childNodes[0].data
    date = user.getElementsByTagName('date')[0].childNodes[0].data
    payment = user.getElementsByTagName('payment')[0].childNodes[0].data
    var_list = [(contract, c_id, ob_id, date, payment)]
    sql = '''INSERT INTO Contracts_new (contract, client_id, object_id, date, payment) VALUES(?, ?, ?, ?, ?)'''
    cur.executemany(sql, var_list)
cur.execute('SELECT * FROM Contracts_new')
clients = cur.fetchall()
print(clients)

con.commit()
con.close()
