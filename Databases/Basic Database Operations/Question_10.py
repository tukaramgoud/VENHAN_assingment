"""10. Write a Python function `insert_student(name: str, grade: float)` that inserts a new
student into the `students` table using SQLite."""


import sqlite3
 
conn = sqlite3.connect('students.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    grade REAL
)
''')


insert_query = '''
INSERT INTO students (name, grade) VALUES (?, ?)
'''

# Define the data to be inserted
student_data = [
    ('John Doe', 85.5),
    ('Jane Smith', 90.2),
    ('Michael Johnson', 78.9)
]

cursor.executemany(insert_query, student_data)


conn.commit()

 
cursor.close()
conn.close()