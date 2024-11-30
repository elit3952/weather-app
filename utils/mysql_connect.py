import mysql.connector



def mysql_connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="weather"
    )