
# =====================================
# STUDENT MANAGEMENT SYSTEM
# Main Application
# =====================================

from modules.student import (
    load_students,
    add_student,
    view_students,
    search_student,
    delete_student
)

from modules.grades import (
    calculate_grade,
    calculate_average
)

from modules.courses import (
    courses,
    display_courses,
    get_unique_courses
)


# Load existing student records
students = load_students()


# Welcome message
print("====================================")
print("       STUDENT MANAGEMENT SYSTEM")
print("====================================")
print("Welcome to the Student Management System!")


# Main menu
while True:

    print("\n========== MAIN MENU ==========")
    print("1. Register Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. View Courses")
    print("6. View Statistics")
    print("7. View Unique Courses")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    # Register student
    if choice == "1":

        add_student(students, courses)

    # View students
    elif choice == "2":

        view_students(students)

        for student in students:
            print("Grade:", calculate_grade(student["mark"]))

    # Search student
    elif choice == "3":

        search_student(students)

    # Delete student
    elif choice == "4":

        delete_student(students)

    # Display courses
    elif choice == "5":

        display_courses()

    # Display statistics
    elif choice == "6":

        total_students = len(students)

        if total_students > 0:

            marks = []

            for student in students:
                marks.append(student["mark"])

            average = calculate_average(marks)

            print("\n===== STUDENT STATISTICS =====")
            print("Total Students:", total_students)
            print("Average Marks:", round(average, 2))

            print("Highest Mark:", max(marks))
            print("Lowest Mark:", min(marks))

        else:
            print("No student records available.")

    # Display unique courses
    elif choice == "7":

        unique_courses = get_unique_courses(students)

        print("\n===== UNIQUE REGISTERED COURSES =====")

        if len(unique_courses) == 0:
            print("No courses registered yet.")

        else:
            for course in unique_courses:
                print(course)

    # Exit system
    elif choice == "8":

        print("\nThank you for using our system!")
        print("Goodbye!")
        break

    else:

        print("Invalid choice! Please try again.")
