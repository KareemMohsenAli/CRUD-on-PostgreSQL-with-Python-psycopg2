import psycopg2
from connection import connectTodatabase
def delete():
    connect=connectTodatabase()
    cursor=connect.cursor()
    if connect:
        print("--------connected to database--------------")
        query_delete = 'delete from users where id= %s '
        personid=input("enter id of user to delete ")
        cursor.execute(query_delete,personid)
        connect.commit()
        print("data is deleted succesfully !")
        cursor.close()
        connect.close()
delete()
  