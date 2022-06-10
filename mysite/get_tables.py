import sqlite3 as lite
from prettytable import from_db_cursor

path = 'db.sqlite3'

conn = lite.connect(path)
cur = conn.cursor()
cur.execute("SELECT * FROM news_news")
tables = from_db_cursor(cur)

print(tables)
