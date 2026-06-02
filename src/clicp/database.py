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
        CREATE TABLE IF NOT EXISTS Contest(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
                   
            name TEXT NOT NULL,
            platform TEXT NOT NULL,
            date TEXT,
                   
            UNIQUE(name, platform)
        )
    """)

    cursor.execute("""
       CREATE TABLE IF NOT EXISTS Problem(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
                   
            name TEXT NOT NULL,   
            rating INTEGER,
            contest_id INTEGER,
                   
            FOREIGN KEY(contest_id) REFERENCES Contest(id)
        )            
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Attempt(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
                   
            comment TEXT,
            attempted_at TEXT NOT NULL,
            time_until_idea INTEGER,
            total_time INTEGER,
            problem_id INTEGER NOT NULL,
                   
            resultType TEXT CHECK(
                resultType IN(
                    'solved',
                    'solved_with_help',
                    'unsolved'
                )       
            ),
                   
            errorType TEXT CHECK(
                errorType IN(
                    'no_idea',
                    'incomplete_idea',
                    'implementation',
                    'reading'
                )       
            ),
                   
            FOREIGN KEY(problem_id) REFERENCES Problem(id)
        )            
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Tag(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
                   
            name TEXT NOT NULL UNIQUE
        )            
    """)

    cursor.execute("""
       CREATE TABLE IF NOT EXISTS Problem_Tag(
            problem_id INTEGER,
            tag_id INTEGER,
                   
            PRIMARY KEY(problem_id, tag_id),
                   
            FOREIGN KEY(problem_id) REFERENCES Problem(id),
            FOREIGN KEY(tag_id) REFERENCES Tag(id)
        )            
    """)

    conn.commit()
    conn.close()
