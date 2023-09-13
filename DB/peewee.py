import pymysql
from peewee import *

conn = pymysql.connect(host="localhost", user="educative", password="secret")
conn.cursor().execute("CREATE DATABASE test")
conn.close()
## for mySQL we use MySQLDatabase class to connect
conn_db = MySQLDatabase(
    "test", host="localhost", port=5432, user="educative", password="secret"
)
conn_db.connect()
