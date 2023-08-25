import sqlite3

# Create a SQLite database and a users table
conn = sqlite3.connect("user_database.db")
cursor = conn.cursor()

# Create the users table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
""")

# Commit changes and close the connection
conn.commit()
conn.close()
