import psycopg2
from connection import connectTodatabase
def insert():
    connect=connectTodatabase()
    cursor=connect.cursor()
    if connect:
        print("--------connected to database--------------")
        userName=input("Enter your name ")
        userage=input("Enter your age ")
        usergender=input("Enter your gender ")
        query_insert="""insert into users(name,age,gender)values(%s,%s,%s)"""
        record_info = (userName,userage,usergender)
        cursor.execute(query_insert, record_info)
        connect.commit()
        print("data inserted succesfully !")
        cursor.close()
        connect.close()
  
insert()