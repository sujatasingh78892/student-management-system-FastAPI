print("Program started:")
from fastapi import FastAPI
import sqlite3

app = FastAPI()

# Database Connection
conn = sqlite3.connect("students.db", check_same_thread=False)
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    course TEXT,
    age INTEGER
)
""")
conn.commit()

# Home API
@app.get("/")
def home():
    return {"message": "Student Management System"}

# Add Student
@app.post("/students")
def add_student(student: dict):
    cursor.execute(
        "INSERT INTO students(name, course, age) VALUES (?, ?, ?)",
        (student["name"], student["course"], student["age"])
    )
    conn.commit()
    return {"message": "Student added"}

# Get All Students
@app.get("/students")
def get_students():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    return data