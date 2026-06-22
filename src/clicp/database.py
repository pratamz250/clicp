from pathlib import Path
import sqlite3
import typer

DATA_DIR = Path.home() / ".local" / "share" / "clicp"
DB_PATH = DATA_DIR / "clicp.db"

def create_data_dir():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

def get_connection():
    create_data_dir()

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")

    return conn

def initialize_data_base():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Platform(
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            UNIQUE(name)           
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Contest(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
                   
            name TEXT NOT NULL,
            date TEXT,
            platform_id INTEGER NOT NULL,
                   
            UNIQUE(name, platform_id),
                   
            FOREIGN KEY(platform_id) REFERENCES Platform(id)
        )
    """)

    cursor.execute("""
       CREATE TABLE IF NOT EXISTS Problem(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
                   
            name TEXT NOT NULL,   
            rating INTEGER CHECK(rating >= 0),
            contest_id INTEGER,
            platform_id INTEGER NOT NULL,
                   
            UNIQUE(name, platform_id),

            FOREIGN KEY(contest_id) REFERENCES Contest(id),
            FOREIGN KEY(platform_id) REFERENCES Platform(id)
        )            
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Attempt(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
                   
            comment TEXT,
            attempted_at TEXT NOT NULL,
            time_until_idea INTEGER CHECK(time_until_idea >= 0),
            total_time INTEGER CHECK(total_time >= 0),
            problem_id INTEGER NOT NULL,
                   
            result_type TEXT CHECK(
                result_type IN(
                    'solved',
                    'solved_with_help',
                    'unsolved'
                )       
            ),
                   
            error_type TEXT CHECK(
                error_type IN(
                    'no_idea',
                    'incomplete_idea',
                    'implementation',
                    'reading'
                )       
            ),
                   
            FOREIGN KEY(problem_id) REFERENCES Problem(id) ON DELETE CASCADE
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
                   
            FOREIGN KEY(problem_id) REFERENCES Problem(id) ON DELETE CASCADE,
            FOREIGN KEY(tag_id) REFERENCES Tag(id) ON DELETE CASCADE
        )            
    """)

    conn.commit()
    conn.close()

def delete_data():
    confirm = typer.confirm(
        "Are you sure you want to delete all data? This can't be undone.",
        default=True
    )

    if not confirm:
        typer.echo("Operation canceled.")
        return 
    elif DB_PATH.exists():
        DB_PATH.unlink()
        print("Database deleted.")

def add_problem_db(
        name: str, 
        platform_name: str,
        rating: int | None = None, 
        contest_name: str | None = None
        ):
    conn = get_connection()
    cursor = conn.cursor()

    #Get platform id
    cursor.execute("""
        SELECT Platform.id
        FROM Platform     
        WHERE Platform.name == ?;
    """, (platform_name,))

    result = cursor.fetchone()

    if result is None:
        conn.close()
        raise ValueError(f"Platform {platform_name} not found.")

    platform_id = result[0]

    #Check if user want to add a problem with a contest and get it's id
    contest_id = None

    if contest_name is not None:
        cursor.execute("""
            SELECT Contest.id
            FROM Contest
            WHERE Contest.name == ? AND Contest.platform_id = ?;
        """, (contest_name, platform_id))

        result = cursor.fetchone()

        if result is None:
            conn.close()
            raise ValueError(f"Contest {contest_name} not found.")

        contest_id = result[0]

    #Executes problem insertion
    cursor.execute("""
        INSERT INTO Problem(name, rating, contest_id, platform_id) 
        VALUES (?, ?, ?, ?);            
    """, (name, rating, contest_id, platform_id))

    conn.commit()
    conn.close()

def add_platform_db(name):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO Platform(name)
            VALUES (?)            
        """, (name,))

        conn.commit()
    
    except sqlite3.IntegrityError:
        raise ValueError(f"Platform {name} already exists.")

    finally:
        conn.close()

def add_contest_db(
        name: str,
        date: 
)