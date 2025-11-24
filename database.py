import sqlite3


def connect_db():
    """Create a connection to the SQLite database file."""
    return sqlite3.connect("gym.db")


def setup_database():
    """Create tables and seed initial data if not exist."""
    conn = connect_db()
    cur = conn.cursor()

    # Members table
    cur.execute(
        """CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            gender TEXT,
            phone TEXT,
            email TEXT,
            join_date TEXT,
            plan TEXT,
            expiry_date TEXT
        )"""
    )

    # Trainers table
    cur.execute(
        """CREATE TABLE IF NOT EXISTS trainers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            specialty TEXT,
            phone TEXT
        )"""
    )

    # Membership plans
    cur.execute(
        """CREATE TABLE IF NOT EXISTS memberships (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            duration_months INTEGER,
            price REAL
        )"""
    )

    # Attendance table
    cur.execute(
        """CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            FOREIGN KEY (member_id) REFERENCES members(id)
        )"""
    )

    # Payments table
    cur.execute(
        """CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL,
            method TEXT,
            notes TEXT,
            FOREIGN KEY (member_id) REFERENCES members(id)
        )"""
    )

    # Seed some default membership plans if table empty
    cur.execute("SELECT COUNT(*) FROM memberships")
    count = cur.fetchone()[0]
    if count == 0:
        plans = [
            ("Monthly", 1, 1000.0),
            ("Quarterly", 3, 2500.0),
            ("Yearly", 12, 8000.0),
        ]
        cur.executemany(
            "INSERT INTO memberships (name, duration_months, price) VALUES (?, ?, ?)",
            plans,
        )

    conn.commit()
    conn.close()
