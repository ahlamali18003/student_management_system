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
    print("\n===== REGISTER NEW STUDENT =====")

    name = input("Enter student name: ").strip()
    admission = input("Enter admission number: ").strip()

    if not name or not admission:
        print("Please fill in all required details!")
        return

    for student in students:
        if student["admission"] == admission:
            print("Admission number already exists!")
            return

    print("\nAVAILABLE COURSES")
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
        print("Please enter valid marks!")
        return

    student = {
        "name": name,
        "admission": admission,
        "course": courses[course_choice],
        "mark": mark
    }
    students.append(student)
    save_students(students)
    print("\nStudent registered successfully!")


def view_students(students):
    print("\n===== STUDENT RECORDS =====")
    if len(students) == 0:
        print("No students registered yet.")
        return

    for student in students:
        print("\n-------------------------")
        print("Name:", student["name"])
        print("Admission:", student["admission"])
        print("Course:", student["course"])
        print("Marks:", student["mark"])
        print("-------------------------")


def search_student(students):
    admission = input("Enter admission number to search: ")
    for student in students:
        if student["admission"] == admission:
            print("\n===== STUDENT FOUND =====")
            print("Name:", student["name"])
            print("Admission:", student["admission"])
            print("Course:", student["course"])
            print("Marks:", student["mark"])
            return
    print("Student not found!")


def update_student(students, courses):
    admission = input("Enter admission number to update: ")
    for student in students:
        if student["admission"] == admission:
            print("\nStudent found!")
            print("1. Update Name")
            print("2. Update Course")
            print("3. Update Marks")
            choice = input("Choose what to update: ")

            if choice == "1":
                new_name = input("Enter new name: ").strip()
                if new_name:
                    student["name"] = new_name
                    print("Name updated successfully!")
                else:
                    print("Name cannot be empty!")

            elif choice == "2":
                for key, value in courses.items():
                    print(key, value)
                course_choice = input("Choose new course: ")
                if course_choice in courses:
                    student["course"] = courses[course_choice]
                    print("Course updated successfully!")
                else:
                    print("Invalid course!")

            elif choice == "3":
                try:
                    new_mark = float(input("Enter new marks: "))
                    if 0 <= new_mark <= 100:
                        student["mark"] = new_mark
                        print("Marks updated successfully!")
                    else:
                        print("Marks must be between 0 and 100!")
                except ValueError:
                    print("Please enter valid marks!")
            else:
                print("Invalid selection!")
            return
    print("Student not found!")


def delete_student(students):
    admission = input("Enter admission number to delete: ")
    for student in students:
        if student["admission"] == admission:
            confirm = input("Are you sure you want to delete? (yes/no): ").lower()
            if confirm == "yes":
                students.remove(student)
                save_students(students)
                print("Student deleted successfully!")
            else:
                print("Deletion cancelled.")
            return
    print("Student not found!")
