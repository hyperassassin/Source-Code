import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()
print("Connection and Database Created Successfully")

try:
    table_query = '''CREATE TABLE details(name TEXT , roll INTEGER ,
                                    course TEXT , age INTEGER , dob TEXT);'''
    cursor.execute(table_query)
    conn.commit()
    print("Table is Created")
    cursor.close()

except sqlite3.Error as error:
    print("Error is :- " , error)
