# General format
# dialect+driver://username:password@host:port/database
import sqlalchemy as sal
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://educative:secret@localhost:5432/test")
conn = engine.connect()
cursor = conn_sql.cursor()
print(engine)
# execute a query
cursor.execute("SELECT * FROM table_name;")
row = cursor.fetchone()
print(row)
# close your cursor and connection
cursor.close()
conn.close()
