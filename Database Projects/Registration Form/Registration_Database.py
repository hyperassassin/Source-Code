import sqlite3

con = sqlite3.connect("register_database.db")
cursor = con.cursor()
print("Database created and connected successfully")
try:
    table_query = '''CREATE TABLE register(form TEXT , name TEXT
                                  , course TEXT , sem TEXT , gender TEXT , email TEXT
                                  , address TEXT , contact TEXT);'''
    cursor.execute(table_query)
    con.commit()
    print("Table is created")
    con.close()
except sqlite3.Error as error:
    print("Error is :- " , error)
