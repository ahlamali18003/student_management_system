
# courses.py

courses = {
    "1": "Web Development",
    "2": "Python Programming",
    "3": "Database Management",
    "4": "Networking",
    "5": "Computer Packages"
}


def display_courses():

    print("\n===== AVAILABLE COURSES =====")

    for key, value in courses.items():
        print(key + ". " + value)


def get_unique_courses(students):

    unique_courses = set()

    for student in students:
        unique_courses.add(student["course"])

    return unique_courses
