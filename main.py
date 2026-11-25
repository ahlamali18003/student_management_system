"""
Student Management System - Main Application Entry Point
Developer: Ahlam Ali
Institution: Kenya Coast National Polytechnic
"""

import sys

# Attempt to import your root entry files or module functions.
# Adjust the imports below if your functions inside login.py, dashboard.py,
# or modules/ have specific function names.
try:
    import login
except ImportError:
    login = None

try:
    import dashboard
except ImportError:
    dashboard = None


def display_menu():
    print("\n" + "=" * 45)
    print("       STUDENT MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Register Student")
    print("2. View Registered Students")
    print("3. Search Student")
    print("4. Delete Student Record")
    print("5. View Available Courses")
    print("6. Calculate Grades")
    print("7. Display Student Statistics")
    print("8. Display Unique Courses")
    print("0. Exit")
    print("=" * 45)


def run_cli_menu():
    while True:
        display_menu()
        choice = input("Enter your choice (0-8): ").strip()

        if choice == "1":
            print("\n[Register Student] -> Connect your modules/ register function here.")
        elif choice == "2":
            print("\n[View Registered Students] -> Connect your modules/ view function here.")
        elif choice == "3":
            print("\n[Search Student] -> Connect your modules/ search function here.")
        elif choice == "4":
            print("\n[Delete Student Record] -> Connect your modules/ delete function here.")
        elif choice == "5":
            print("\n[View Available Courses] -> Connect your modules/ courses function here.")
        elif choice == "6":
            print("\n[Calculate Grades] -> Connect your modules/ grades function here.")
        elif choice == "7":
            print("\n[Display Student Statistics] -> Connect your modules/ statistics function here.")
        elif choice == "8":
            print("\n[Display Unique Courses] -> Connect your modules/ unique courses function here.")
        elif choice == "0":
            print("Exiting Student Management System. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number between 0 and 8.")


def main():
    # If login.py has a main() or login() function, launch it first
    if login is not None:
        if hasattr(login, "main"):
            login.main()
            return
        elif hasattr(login, "login"):
            if not login.login():
                print("Authentication failed. Exiting.")
                return

    # Next, hand off to dashboard.py if it defines a main() or dashboard() function
    if dashboard is not None:
        if hasattr(dashboard, "main"):
            dashboard.main()
            return
        elif hasattr(dashboard, "dashboard"):
            dashboard.dashboard()
            return

    # Fallback: Run the built-in interactive CLI menu
    run_cli_menu()


if __name__ == "__main__":
    main()
