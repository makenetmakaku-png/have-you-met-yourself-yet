import sqlite3

conn = sqlite3.connect("challenge.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY,
name TEXT,
points INTEGER DEFAULT 0,
streak INTEGER DEFAULT 0
)
""")

conn.commit()