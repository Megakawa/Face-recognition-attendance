# Vị trí import package
from mysql.connector import MySQLConnection, Error
db_config = {
        'host': 'localhost',
        'database': 'doan',
        'user': 'root',
        'password': '12345'
    }
def ExecuteNonQuery(query):
    """ Kết nối MySQL bằng module MySQLConnection """
    # Biến lưu trữ kết nối
    conn = None
    data = 0
    try:
        conn = MySQLConnection(**db_config)
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            data = 1
    except Error as error:
        print(error)
    return data
def ExecuteQuery(query):
    """ Kết nối MySQL bằng module MySQLConnection """
    # Biến lưu trữ kết nối
    conn = None
    data = []
    try:
        conn = MySQLConnection(**db_config)
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(query)
            row = cursor.fetchone()
            while row is not None:
               data.append(row)
               row = cursor.fetchone()
    except Error as error:
        print(error)
    return data