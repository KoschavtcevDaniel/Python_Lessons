import sqlite3 as sql


class CreateDataBase(object):
    def __init__(self, database_file):
        self._connection = sql.connect(database_file)

    def __del__(self):
        self._connection.close()

    def create_table(self, table_name, table_columns):
        self._connection.cursor().execute(
            f""" create table if not exists {table_name} (
            {', '.join(table_columns)}); """)

    def insert_data(self, table_name, table_columns, data):
        pass


connection = sql.connect('real_estate_agency.db')
cursor = connection.cursor()
cursor.execute(
    """create table if not exists Clients (
        id INTEGER PRIMARY KEY,
        first_name VARCHAR(30) not null,
        last_name VARCHAR(30) not null,
        passport VARCHAR(30) not null,
        ownership VARCHAR(300) not null);""")

cursor.execute(
    """create table if not exists Realty (
        id INTEGER PRIMARY KEY,
        object VARCHAR(30) not null,
        status VARCHAR(100));""")

cursor.execute(
    """create table if not exists Contracts (
        contract INTEGER PRIMARY KEY,
        client_id INTEGER not null,
        object_id INTEGER not null,
        date DATETIME not null,
        payment FLOAT not null,
        foreign key (client_id) references Clients (id),
        foreign key (object_id) references Realty (id));""")

cursor.execute(
    """create table if not exists RealtyPayment (
        id INTEGER primary key,
        date DATETIME not null,
        contract Integer not null,
        foreign key (contract) references Contracts (contract))""")

connection.commit()
cursor.close()
connection.close()
