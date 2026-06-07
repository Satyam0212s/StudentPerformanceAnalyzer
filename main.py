from database.create_table import (
    create_students_table
)

from database.import_csv import (
    import_students
)

from database.fetch_data import (
    fetch_students
)


create_students_table()

import_students()

df = fetch_students()

print(df)