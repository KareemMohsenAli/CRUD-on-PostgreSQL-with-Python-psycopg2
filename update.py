import psycopg2
from connection import connectTodatabase
def update():
    connect=connectTodatabase()
    cursor=connect.cursor()
    if connect:
        print("--------connected to database--------------")
        userid=input('enter id of user u want to update ')
        userName=input("Enter the name you want to update ")
        userage=input("Enter the age you want to update ")
        usergender=input("Enter the gender you want to update ")
        query_pdate = "UPDATE users SET name=%s,age=%s,gender=%s WHERE id=%s"
        record_info = (userName,userage,usergender,userid)
        cursor.execute(query_pdate, record_info)
        connect.commit()
        print("data updated succesfully !")
        cursor.close()
        connect.close()
  
update()