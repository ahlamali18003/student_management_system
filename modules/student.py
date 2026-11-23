
# student.py

import json
import os

FILE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "students.json"
)


def load_students():

    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_students(students):

    with open(FILE_PATH, "w") as file:
        json.dump(students, file, indent=4)


def add_student(students, courses):

    print("\n===== REGISTER STUDENT =====")

    name = input("Enter student name: ").strip()
    admission = input("Enter admission number: ").strip()

    if not name or not admission:
        print("Name and admission number are required!")
        return

    for student in students:

        if student["admission"] == admission:
            print("Admission number already exists!")
            return

    print("\nAvailable Courses:")

    for key, value in courses.items():
        print(key, value)

    course_choice = input("Choose course number: ")

    if course_choice not in courses:
        print("Invalid course selection!")
        return

    try:
        mark = float(input("Enter student marks: "))

        if mark < 0 or mark > 100:
            print("Marks must be between 0 and 100!")
            return

    except ValueError:
        print("Please enter a valid number!")
        return

    student = {
        "name": name,
        "admission": admission,
        "course": courses[course_choice],
        "mark": mark
    }

    students.append(student)

    save_students(students)

    print("Student registered successfully!")


def view_students(students):

    print("\n REGISTERED STUDENTS")

    if len(students) == 0:
        print("No students registered.")

    else:

        for student in students:

            print("\nName:", student["name"])
            print("Admission:", student["admission"])
            print("Course:", student["course"])
            print("Marks:", student["mark"])


def search_student(students):

    admission = input("Enter admission number: ").strip()

    for student in students:

        if student["admission"] == admission:

            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Course:", student["course"])
            print("Marks:", student["mark"])
            return

    print("Student not found!")


def delete_student(students):

    admission = input("Enter admission number to delete: ").strip()

    for student in students:

        if student["admission"] == admission:

            students.remove(student)

            save_students(students)

            print("Student deleted successfully!")
            return

    print("Student not found!")
