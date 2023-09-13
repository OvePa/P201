import mysql.connector

conn = mysql.connector.connect(
    host="localhost", user="educative", password="secret", database="test"
)
cursor = conn.cursor()

cursor.execute("SELECT * FROM table_name")

# get a single row
row = cursor.fetchone()
print("printing the first row:")
print(row)

# disconnect from the database
conn.close()
