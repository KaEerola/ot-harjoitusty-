import sqlite3

def init_db():
    conn = sqlite3.connect("golf.db")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS rounds (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course TEXT NOT NULL,
            score INTEGER NOT NULL,
            date TEXT NOT NULL,
            user INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()