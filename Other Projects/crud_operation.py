import mysql.connector
from mysql.connector import Error

def delete_data():
        try:
                conn = mysql.connector.connect(host='localhost',port='33060',database='details',user='root',password='sagar')
                cursor = conn.cursor()
                sql = """Delete from details where id = %s"""
                uid = int(input("Id :- "))
                cursor.execute(sql,(uid,))
                conn.commit()
                print(cursor.rowcount," Row Deleted")
        except Error as e:
                print("Error :- ",e)
        finally:
                if(conn.is_connected()):
                        cursor.close()
                        conn.close()

def update_data():
        try:
                conn = mysql.connector.connect(host='localhost',port='33060',database='details',user='root',password='sagar')
                cursor = conn.cursor()
                sql = """update details set name = %s where id = %s"""
                name=input("Name :- ")
                uid=int(input("Id :- "))
                cursor.execute(sql,(name,uid,))
                conn.commit()
                print(cursor.rowcount," Row Updated")
        except Error as e:
                print("Error :-",e)
        finally:
                if(conn.is_connected()):
                        cursor.close()
                        conn.close()

def select_data():
        try:
                conn = mysql.connector.connect(host='localhost',port='33060',database='details',user='root',password='sagar')
                cursor = conn.cursor()
                sql = """select * from details"""
                cursor.execute(sql)
                record = cursor.fetchall()
                print("Table Records :- ",record)
        except Error as e:
                print("Error :- ",e)
        finally:
                if(conn.is_connected()):
                        cursor.close()
                        conn.close()

def insert_data():
        try:
                conn = mysql.connector.connect(host='localhost',port='33060',database='details',user='root',password='sagar')
                cursor = conn.cursor()
                sql = """insert into details values(%s,%s)"""
                uid = int(input("Id :- "))
                name = input("Name :- ")
                cursor.execute(sql,(uid,name,))
                conn.commit()
                print(cursor.rowcount," Row Inserted")
        except Error as e:
                print("Error :- " ,e)
        finally:
                if(conn.is_connected()):
                        cursor.close()
                        conn.close()
print("-----MySQL Operations-----")
print("1 . View The Data ")
print("2 . Insert The Data ")
print("3. Update The Data ")
print("4. Delete The Data ")
while True:
        choice = int(input("Which Operation :- "))
        if choice == 1:
                select_data()
        elif choice == 2:
                insert_data()
        elif choice == 3:
                update_data()
        elif choice == 4:
                delete_data()
        else:
                break

