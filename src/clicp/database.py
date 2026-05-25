from pathlib import Path
import sqlite3

DATA_DIR = Path.home() / ".local" / "share" / "clicp"
DB_PATH = DATA_DIR / "clicp.db"

def createDataDir():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

def getConnection():
    return sqlite3.connect(DB_PATH)

def initializeDataBase():
    conn = getConnection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS problems (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        platform TEXT NOT NULL,
        problem TEXT NOT NULL,
        rating INTEGER,
        solved_at TEXT
    )
    """)

    conn.commit()
    conn.close()