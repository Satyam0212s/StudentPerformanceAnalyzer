import pandas as pd

from database.db_connect import (
    get_connection
)


def fetch_students():

    conn = get_connection()

    query = """
    SELECT *
    FROM students
    """

    df = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    return df