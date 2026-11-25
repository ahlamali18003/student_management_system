
# =====================================
# STUDENT MANAGEMENT SYSTEM
# Main Application
# =====================================

from modules.student import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student
)

students = []

courses = {
    "1": "Web Development",
    "2": "Python Programming",
    "3": "Database Management",
    "4": "Networking"
}


# Welcome message
print("====================================")
print("       STUDENT MANAGEMENT SYSTEM")
print("====================================")
print("Welcome to the Student Management System!")


# Main menu
while True:

    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")

    print("1. Register Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student(students, courses)

    elif choice == "2":
        view_students(students)

    elif choice == "3":
        search_student(students)

    elif choice == "4":
        update_student(students, courses)

    elif choice == "5":
        delete_student(students)

    elif choice == "6":
        print("Thank you for using our system!")
        break

    else:
        print("Invalid choice!")
