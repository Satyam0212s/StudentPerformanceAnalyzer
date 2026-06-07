import sqlite3

def get_connection():

    conn = sqlite3.connect(
        "student_performance.db"
    )

    return conn