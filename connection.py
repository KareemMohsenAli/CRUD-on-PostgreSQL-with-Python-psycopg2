import psycopg2
dbuser= 'kemo'
dbpassword = '12345'
dbname = 'project'

def connectTodatabase():
    try:
        connection = psycopg2.connect(user=dbuser,password=dbpassword,host='127.0.0.1',database=dbname, port='5432')
        connection.autocommit=1
        return  connection

    except (Exception, psycopg2.Error) as e:
        print(e)
        return None




    

