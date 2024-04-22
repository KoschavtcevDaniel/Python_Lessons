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


connection = sql.connect('insurance_company.db')
cursor = connection.cursor()
cursor.execute(
    """create table if not exists Clients (
        id INTEGER PRIMARY KEY,
        first_name VARCHAR(30) not null,
        last_name VARCHAR(30) not null,
        passport VARCHAR(30) not null);""")

cursor.execute(
    """create table if not exists Insurance_Objects (
        id INTEGER PRIMARY KEY,
        object VARCHAR(30) not null,
        description VARCHAR(300));""")

cursor.execute(
    """create table if not exists Contracts (
        contracts_№ INTEGER PRIMARY KEY,
        client_id INTEGER not null,
        object_id INTEGER not null,
        contract_date DATETIME not null,
        insurance_payment FLOAT not null,
        foreign key (client_id) references Clients (id),
        foreign key (object_id) references Insurance_Objects (id));""")

cursor.execute(
    """create table if not exists Insurance_Payments (
        id INTEGER primary key,
        date DATETIME not null,
        contracts_№ Integer not null,
        foreign key (contracts_№) references Contracts (contracts_№))""")

connection.commit()
cursor.close()
connection.close()
