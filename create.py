import psycopg2
from connection import connectTodatabase
def create():
    connect=connectTodatabase()
    cursor=connect.cursor()
    if connect:
        print("--------connected to database--------------")
        table_name = input("Enter the name of the table you want to create: ")
        column1_name = input("Enter the name of the first column: ")
        column1_type = input("Enter the data type for the first column: ")
        column2_name = input("Enter the name of the second column: ")
        column2_type = input("Enter the data type for the second column: ")

        cursor.execute(f"CREATE TABLE {table_name} ({column1_name} {column1_type}, {column2_name} {column2_type})")
        connect.commit()
        print("data inserted succesfully !")
        cursor.close()
        connect.close()
  
create()