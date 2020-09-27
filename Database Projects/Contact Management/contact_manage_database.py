import sqlite3

con = sqlite3.connect("contact.db")
cursor = con.cursor()
print("Database created and connected successfully")
try:
    table_query = '''CREATE TABLE contact(fname TEXT , lname TEXT , email TEXT
                                    ,contact TEXT , address TEXT);'''
    cursor.execute(table_query)
    con.commit()
    print("Table is Created")
    con.close()
except sqlite3.Error as error:
    print("Error is :- ",error)
    
