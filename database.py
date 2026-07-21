import sqlite3

conn = sqlite3.connect("challenge.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    points INTEGER DEFAULT 0,
    streak INTEGER DEFAULT 0,
    current_day INTEGER DEFAULT 1,
    last_completed TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS challenges(
    day INTEGER PRIMARY KEY,
    text TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS journals(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    day INTEGER,
    journal TEXT,
    points INTEGER,
    date TEXT
)
""")

conn.commit()