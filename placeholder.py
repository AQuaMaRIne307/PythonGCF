import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
''')
conn.commit()

# Function to Insert Data
def insert_student(name, age, grade):
    cursor.execute('INSERT INTO students (name, age, grade) VALUES (?, ?, ?)', (name, age, grade))
    conn.commit()
    print("Student inserted successfully.")

# Function to Read Data
def fetch_students():
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Function to Update Data
def update_student(student_id, name, age, grade):
    cursor.execute('UPDATE students SET name = ?, age = ?, grade = ? WHERE id = ?', (name, age, grade, student_id))
    conn.commit()
    print("Student updated successfully.")

# Function to Delete Data
def delete_student(student_id):
    cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    print("Student deleted successfully.")

# --- Test the CRUD Operations ---

# Insert
insert_student('John Doe', 20, 'A')
insert_student('Jane Smith', 22, 'B')

# Read
print("\nAll Students:")
fetch_students()

# Update
update_student(1, 'John Wick', 21, 'A+')

# Read after Update
print("\nAfter Update:")
fetch_students()

# Delete
delete_student(2)

# Read after Delete
print("\nAfter Deletion:")
fetch_students()

# Close connection
conn.close()
