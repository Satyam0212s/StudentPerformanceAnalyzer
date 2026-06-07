import pandas as pd

from database.db_connect import get_connection


def import_students():

    df = pd.read_csv(
        "data/students.csv"
    )

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students"
    )

    for _, row in df.iterrows():

        cursor.execute(
            """
            INSERT INTO students
            VALUES (?,?,?,?,?,?,?)
            """,
            (
                int(row["student_id"]),
                row["name"],
                int(row["math"]),
                int(row["physics"]),
                int(row["chemistry"]),
                int(row["english"]),
                int(row["computer"])
            )
        )

    conn.commit()

    cursor.close()
    conn.close()

    print("CSV Imported Successfully!")