import os
import sqlite3
os.environ["CONDA_DLL_SEARCH_MODIFICATION_ENABLE"] = "1"

import sqlite3 as sl 
from sqlite3 import Error
#from models import Horse

conn = sqlite3.connect('my_db.db')

# before starting app import sql file to the db
# c = conn.cursor()
# c.execute("create database if not exists my_db")
# conn.database = "my_db"

filename = 'my_db.db'

conn = sl.connect(filename)
conn.execute("PRAGMA foreign_keys = 1")
c = conn.cursor()

owners = """
        CREATE TABLE IF NOT EXISTS owners (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            );
        """

auctions = """
            CREATE TABLE IF NOT EXISTS auctions (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                date TEXT NOT NULL
            );
        """

horses = """
            CREATE TABLE IF NOT EXISTS horses (
                id INTEGER PRIMARY KEY,
                lot TEXT NOT NULL,
                dob TEXT NOT NULL,
                sex TEXT NOT NULL,
                dam TEXT NOT NULL,
                sire TEXT NOT NULL,
                price REAL NOT NULL,
                owner_id INTEGER NOT NULL,
                FOREIGN KEY (owner_id) REFERENCES owners(id)
            );
        """

horse_auction = """
        CREATE TABLE IF NOT EXISTS horse_auction (
                id INTEGER PRIMARY KEY,
                horse_id INTEGER NOT NULL,
                auction_id INTEGER NOT NULL,
                FOREIGN KEY (horse_id) REFERENCES horses(id),
                FOREIGN KEY (auction_id) REFERENCES auctions(id)
            );
        """


shows = """
            CREATE TABLE IF NOT EXISTS shows (
                id INTEGER PRIMARY KEY,
                date TEXT NOT NULL,
                auction_id NOT NULL,
                FOREIGN KEY (auction_id) REFERENCES auction(id)
            );
        """

cards = """
            CREATE TABLE IF NOT EXISTS cards (
                id INTEGER PRIMARY KEY,
                horse_id INTEGER NOT NULL,
                show_id INTEGER NOT NULL,
                FOREIGN KEY (horse_id) REFERENCES horses(id),
                FOREIGN KEY (show_id) REFERENCES shows(id)
            );
        """

statuses = """
            CREATE TABLE IF NOT EXISTS statuses (
                id INTEGER PRIMARY KEY,
                desc TEXT NOT NULL
            );
        """

customers = """
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            );
        """

requests = """
            CREATE TABLE IF NOT EXISTS requests (
                id INTEGER PRIMARY KEY,
                card_id INTEGER NOT NULL,
                customer_id INTEGER NOT NULL,
                status_id INTEGER NOT NULL,
                created TEXT NOT NULL,
                FOREIGN KEY (card_id) REFERENCES customers(id),
                FOREIGN KEY (customer_id) REFERENCES customers(id),
                FOREIGN KEY (status_id) REFERENCES statuses(id)

            );
        """




tables = [owners, auctions, horses, horse_auction, shows, cards, statuses, customers, requests]

# create all tables in sqlite3
for table in tables:
    c.execute(table)

# insert data for new table

# c.execute("INSERT INTO owners (name) VALUES ('stadnina 1')")
# c.execute("INSERT INTO owners (name) VALUES ('stadnina 2')")
# c.execute("INSERT INTO owners (name) VALUES ('stadnina 3')")

# c.execute("INSERT INTO customers (name) VALUES ('Customer 1')")
# c.execute("INSERT INTO customers (name) VALUES ('Customer 2')")
# c.execute("INSERT INTO customers (name) VALUES ('Customer 3')")
# c.execute("INSERT INTO customers (name) VALUES ('Customer 4')")
# c.execute("INSERT INTO customers (name) VALUES ('Customer 5')")
# c.execute("INSERT INTO customers (name) VALUES ('Customer 6')")
# c.execute("INSERT INTO customers (name) VALUES ('Customer 7')")
# c.execute("INSERT INTO customers (name) VALUES ('Customer 8')")
# c.execute("INSERT INTO customers (name) VALUES ('Customer 9')")

# c.execute("INSERT INTO auctions (name, date) VALUES ('Auction 1', '01/07/2021')")
# c.execute("INSERT INTO auctions (name, date) VALUES ('Auction 2', '03/08/2021')")
# c.execute("INSERT INTO auctions (name, date) VALUES ('Auction 3', '05/09/2021')")
# c.execute("INSERT INTO auctions (name, date) VALUES ('Auction 4', '11/10/2021')")
# c.execute("INSERT INTO auctions (name, date) VALUES ('Auction 5', '15/11/2021')")


# c.execute("INSERT INTO horses (lot,dob,sex,dam,sire,price,owner_id) VALUES ('312','17/05/2009','f','panda','sancho',510000,2)")
# c.execute("INSERT INTO horses (lot,dob,sex,dam,sire,price,owner_id) VALUES ('351','17/05/2009','m','bongo','mongo',550000,2)")
# c.execute("INSERT INTO horses (lot,dob,sex,dam,sire,price,owner_id) VALUES ('452','17/05/2009','f','maria','luigi',470000,2)")
# c.execute("INSERT INTO horses (lot,dob,sex,dam,sire,price,owner_id) VALUES ('752','17/05/2009','m','trampa','donald',780000,2)")
# c.execute("INSERT INTO horses (lot,dob,sex,dam,sire,price,owner_id) VALUES ('652','17/05/2009','f','angela','merkel',510000,2)")

'''create record in shows table and records in cards table (show-horse)'''

# c.execute("""INSERT INTO shows (date, auction_id) VALUES ('12/08/2021',1)""")
# c.execute("""INSERT INTO cards (horse_id, show_id) VALUES (1,1)""")
# c.execute("""INSERT INTO cards (horse_id, show_id) VALUES (3,1)""")

# c.execute("""INSERT INTO shows (date, auction_id) VALUES ('13/08/2021',1)""")
# c.execute("""INSERT INTO cards (horse_id, show_id) VALUES (2,2)""")
# c.execute("""INSERT INTO cards (horse_id, show_id) VALUES (4,2)""")

# c.execute("""INSERT INTO shows (date, auction_id) VALUES ('14/08/2021',1)""")
# c.execute("""INSERT INTO cards (horse_id, show_id) VALUES (1,3)""")
# c.execute("""INSERT INTO cards (horse_id, show_id) VALUES (2,3)""")
# c.execute("""INSERT INTO cards (horse_id, show_id) VALUES (3,3)""")

# c.execute("""INSERT INTO statuses (desc) VALUES ('Requested')""")
# c.execute("""INSERT INTO statuses (desc) VALUES ('Completed')""")

""""new customer and new requests"""

# c.execute("""INSERT INTO customers (name) VALUES ('Michael Owen')""")

# c.execute("""INSERT INTO requests (card_id, customer_id, status_id, created) VALUES (5,1,1,'14/08/2021')""")
# c.execute("""INSERT INTO requests (card_id, customer_id, status_id, created) VALUES (6,1,1,'14/08/2021')""")
# c.execute("""INSERT INTO requests (card_id, customer_id, status_id, created) VALUES (7,1,1,'14/08/2021')""")

# c.execute("""UPDATE requests SET status_id = 2 WHERE customer_id = 1""")

#c.execute("UPDATE auctions SET name='Auction 3' WHERE id=3" )

#c.execute("""DELETE FROM statuses WHERE id=2""")

def insert_customer(customer):

    import os
    os.environ["CONDA_DLL_SEARCH_MODIFICATION_ENABLE"] = "1"
    import sqlite3
    filename = 'my_db.db'
    conn = sqlite3.connect(filename)
    c = conn.cursor()

    with conn:
        c.execute("INSERT INTO customers (name) VALUES (:customer_name)", {'customer_name': customer.name})
    conn.close()

def insert_owner(owner):

    import os
    os.environ["CONDA_DLL_SEARCH_MODIFICATION_ENABLE"] = "1"
    import sqlite3
    filename = 'my_db.db'
    conn = sqlite3.connect(filename)
    c = conn.cursor()

    with conn:
        c.execute("INSERT INTO owners (name) VALUES (:owner_name)", {'owner_name': owner.name})
    conn.close()

def insert_auction(auction):

    import os
    os.environ["CONDA_DLL_SEARCH_MODIFICATION_ENABLE"] = "1"
    import sqlite3
    filename = 'my_db.db'
    conn = sqlite3.connect(filename)
    c = conn.cursor()

    with conn:
        c.execute("INSERT INTO auctions (name, date) VALUES (:auction_name, :date)", {'auction_name': auction.name, 'date': auction.date})
    conn.commit()
    conn.close()

def insert_horse(horse):
    import os
    os.environ["CONDA_DLL_SEARCH_MODIFICATION_ENABLE"] = "1"
    import sqlite3 as sl
    filename = 'my_db.db'
    conn = sl.connect(filename)
    c = conn.cursor()
    #open_conn()
    add_horse = "INSERT INTO horses (lot, dob, sex, dam, sire, price, owner_id) VALUES (:lot, :dob, :sex, :dam, :sire, :price, :owner_id)"
    with conn:
        c.execute(add_horse, {'lot': horse.lot, 'dob': horse.dob, 'sex': horse.sex, 'dam': horse.dam, 'sire': horse.sire, 'price': horse.price, 'owner_id': horse.owner_id})
    conn.close()

def show_customers():
    import os
    os.environ["CONDA_DLL_SEARCH_MODIFICATION_ENABLE"] = "1"
    import sqlite3 as sl
    filename = 'my_db.db'
    conn = sl.connect(filename)
    c = conn.cursor()
    #open_conn()
    all_customers = "SELECT * FROM customers;"
    
    with conn:
        c.execute(all_customers)
        rows = c.fetchall()
        print(rows)
        return rows
    conn.close()

def show_auctions():
    import os
    os.environ["CONDA_DLL_SEARCH_MODIFICATION_ENABLE"] = "1"
    import sqlite3 as sl
    filename = 'my_db.db'
    conn = sl.connect(filename)
    c = conn.cursor()
    #open_conn()
    all_auctions = "SELECT * FROM auctions;"
    
    with conn:
        c.execute(all_auctions)
        rows = c.fetchall()
        print(rows)
        return rows

def select_customer(customer_id):
    import os
    os.environ["CONDA_DLL_SEARCH_MODIFICATION_ENABLE"] = "1"
    import sqlite3 as sl
    filename = 'my_db.db'
    conn = sl.connect(filename)
    c = conn.cursor()
    #open_conn()
    select_customer = "SELECT * FROM customers WHERE id=:id"

    with conn:
        c.execute(select_customer,{'id':customer_id})
        rows = c.fetchall()
        print(rows)
        return rows
    conn.close()

def select_customer2(customer_name):
    '''return list with single tuple with selected customer by name'''
    import os
    os.environ["CONDA_DLL_SEARCH_MODIFICATION_ENABLE"] = "1"
    import sqlite3 as sl
    filename = 'my_db.db'
    conn = sl.connect(filename)
    c = conn.cursor()
    #open_conn()
    select_customer = "SELECT * FROM customers WHERE name=:name"

    with conn:
        c.execute(select_customer,{'name':customer_name})
        rows = c.fetchall()
        print(rows)
        return rows

# def create_connection(db_file):
#     """return connection object or None"""

#     conn = None
#     try:
#         conn = sl.connect(db_file)
#         return conn
#     except Error as e:
#         print(e)

#     return conn

# def create_table(conn, create_table_sql):
#     """create table from create_table_sql statement"""

#     try:
#         c = conn.cursor()
#         c.execute(create_table_sql)
#     except Error as e:
#         print(e)

# def create_schema():
#     database = 'schema2.db'

#     customers = """
#             CREATE TABLE IF NOT EXISTS customers (
#                 id INTEGER PRIMARY KEY,
#                 name TEXT NOT NULL
#             );
#         """

#     cards = """
#             CREATE TABLE IF NOT EXISTS cards (
#                 id INTEGER PRIMARY KEY,
#                 status TEXT NOT NULL,
#                 created TEXT NOT NULL,
#                 customer_id INTEGER NOT NULL,
#                 FOREIGN KEY (customer_id) REFERENCES customers(id)
#             );
#         """

#     owners = """
#             CREATE TABLE IF NOT EXISTS owners (
#                 id INTEGER PRIMARY KEY,
#                 name TEXT NOT NULL
#             );
#         """

#     horses = """
#             CREATE TABLE IF NOT EXISTS horses (
#                 id INTEGER PRIMARY KEY,
#                 lot TEXT NOT NULL,
#                 dob TEXT NOT NULL,
#                 sex TEXT NOT NULL,
#                 dam TEXT NOT NULL,
#                 sire TEXT NOT NULL,
#                 price REAL NOT NULL,
#                 owner_id INTEGER NOT NULL,
#                 FOREIGN KEY (owner_id) REFERENCES owners(id)
#             );
#         """

#     requests = """
#             CREATE TABLE IF NOT EXISTS requests (
#                 id INTEGER PRIMARY KEY,
#                 horse_id INTEGER NOT NULL,
#                 card_id INTEGER NOT NULL,
#                 FOREIGN KEY (horse_id) REFERENCES horses(id)
#                 FOREIGN KEY (card_id) REFERENCES cards(id)
#             );
#         """

#     auctions = """
#             CREATE TABLE IF NOT EXISTS auctions (
#                 id INTEGER PRIMARY KEY,
#                 name TEXT NOT NULL,
#                 date TEXT NOT NULL,
#                 horse_id INTEGER NOT NULL,
#                 FOREIGN KEY (horse_id) REFERENCES horses(id)
#             );
#         """

#     shows = """
#             CREATE TABLE IF NOT EXISTS shows (
#                 id INTEGER PRIMARY KEY,
#                 date TEXT NOT NULL,
#                 auction_id NOT NULL,
#                 FOREIGN KEY (auction_id) REFERENCES auction(id)
#             );
#         """

#     # list with create table statements
#     tables = [customers, cards, owners, horses, requests, auctions, shows]

#     # create_connection
#     conn = create_connection(database)

#     # create_tables
#     if conn is not None:
#         for table in tables:
#             create_table(conn, table)

#     else:
#         print("Error! cannot create the database connection")


#c.execute("INSERT INTO owners (name) VALUES('stadnina1')")

# c.execute("""
#             CREATE TABLE IF NOT EXISTS test (
#                 lot TEXT,
#                 dob TEXT,
#                 sex TEXT,
#                 dam TEXT,
#                 sire TEXT,
#                 price REAL
#             )
#             """)
conn.commit()
conn.close()