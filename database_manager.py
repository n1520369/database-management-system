import sqlite3

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
id INTEGER PRIMARY KEY,
name TEXT,
department TEXT,
salary REAL
)
""")

cursor.execute("""
INSERT INTO employees(name, department, salary)
VALUES('John', 'IT', 60000)
""")

conn.commit()

cursor.execute("SELECT * FROM employees")

records = cursor.fetchall()

for row in records:
    print(row)

conn.close()
