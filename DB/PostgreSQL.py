import psycopg2

string = "postgresql://educative@localhost/test?password=secret"
conn = psycopg2.connect(string)
cursor = conn.cursor()

# execute a query
cursor.execute("SELECT * FROM table_name;")
row = cursor.fetchone()
print(row)
# close your cursor and connection
cursor.close()
conn.close()
