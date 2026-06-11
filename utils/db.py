import sqlite3

DB_NAME = "database/water_leakage.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        report_id TEXT,
        reporter_name TEXT,
        location TEXT,
        issue_type TEXT,
        description TEXT,
        severity TEXT,
        image_path TEXT,
        status TEXT,
        date_reported TEXT
    )
    """)

    conn.commit()
    conn.close()