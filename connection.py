import mysql.connector

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'use_pure': True,
    'port': 3306,
    'database': 'employees',
    'charset': 'utf8'
}


def get_emp_firstname():
    mydb = mysql.connector.connect(**config)
    print(mydb.connection_id)
    cur = mydb.cursor()
    que = "select first_name from employees;"
    cur.execute(que)
    result = cur.fetchall()
    return result



