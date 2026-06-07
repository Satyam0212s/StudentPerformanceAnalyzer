from database.db_connect import get_connection


def create_students_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (

        student_id INTEGER PRIMARY KEY,
        name TEXT,

        math INTEGER,
        physics INTEGER,
        chemistry INTEGER,
        english INTEGER,
        computer INTEGER

    )
    """)

    conn.commit()

    cursor.close()
    conn.close()

    print("Table Created Successfully!")