cursor.execute("CREATE TABLE student (name VARCHAR(255), resource VARCHAR(255))")
data = "INSERT INTO student (name, resources) VALUES (%s, %s)"
data_insert = [
    ("John", "Coursera"),
    ("Alice", "Udemy"),
    ("Michael", "Educative"),
    ("Addison", "Coursera"),
    ("Joe", "Educative"),
]
cursor.executemany(data, data_insert)
conn.commit()


cursor.execute("SELECT*FROM student")
all_data = cursor.fetchall()
for i in all_data:
    print(i)


data = "SELECT * FROM student WHERE resource = 'Educative'"
cursor.execute(data)
all_data = cursor.fetchall()
for i in all_data:
    print(i)


cursor = conn.cursor()
data = "DELETE FROM student WHERE resource = 'Coursera'"
cursor.execute(data)
conn.commit()
