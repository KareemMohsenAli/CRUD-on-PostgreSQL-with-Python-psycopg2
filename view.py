import psycopg2
from connection import connectTodatabase
def view():
    connect=connectTodatabase()
    cursor=connect.cursor()
    if connect:
        print("--------connected to database--------------")
        # cursor.execute(query_insert, record_info)
        # execute the SQL query to retrieve the data
        cursor.execute("SELECT * FROM users;")
        # fetch all the rows from the result set
        rows = cursor.fetchall()
        # display the data to the user
        for row in rows:
            print(row)

        connect.commit()
        cursor.close()
        connect.close()
view()
   