
import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import subprocess
import sys


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__" and "--authenticated" not in sys.argv:
    login_path = os.path.join(BASE_DIR, "login.py")
    subprocess.Popen([sys.executable, login_path], cwd=BASE_DIR)
    sys.exit(0)

# ------------------ SETTINGS ------------------

BG = "#111318"
SIDEBAR = "#191D25"
CARD = "#202631"
GOLD = "#D4AF37"
WHITE = "#FFFFFF"
MUTED = "#AAB0BC"
GREEN = "#35B779"
RED = "#E45B5B"

DATA_DIR = os.path.join(BASE_DIR, "data")
FILE_PATH = os.path.join(DATA_DIR, "students.json")

COURSES = [
    "Web Development",
    "Python Programming",
    "Database Management",
    "Networking",
    "Computer Packages"
]


# ------------------ DATA FUNCTIONS ------------------

def load_students():
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w") as file:
            json.dump([], file)

    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_students():
    with open(FILE_PATH, "w") as file:
        json.dump(students, file, indent=4)


students = load_students()


def calculate_average():
    if not students:
        return 0

    return sum(float(s.get("mark", 0)) for s in students) / len(students)


def calculate_grade(mark):
    mark = float(mark)

    if mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    return "F"


# ------------------ MAIN WINDOW ------------------

root = tk.Tk()
root.title("Student Management System")
root.geometry("1200x720")
root.minsize(1000, 650)
root.configure(bg=BG)

current_page = "Dashboard"


# ------------------ STYLING ------------------

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Treeview",
    background=CARD,
    foreground=WHITE,
    fieldbackground=CARD,
    rowheight=35,
    borderwidth=0
)

style.configure(
    "Treeview.Heading",
    background=SIDEBAR,
    foreground=GOLD,
    font=("Arial", 10, "bold"),
    relief="flat"
)

style.map(
    "Treeview",
    background=[("selected", GOLD)],
    foreground=[("selected", BG)]
)


# ------------------ MAIN LAYOUT ------------------

sidebar = tk.Frame(root, bg=SIDEBAR, width=220)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

main = tk.Frame(root, bg=BG)
main.pack(side="right", fill="both", expand=True)


# ------------------ SIDEBAR ------------------

logo = tk.Label(
    sidebar,
    text="STUDENT\nMANAGEMENT",
    bg=SIDEBAR,
    fg=GOLD,
    font=("Arial", 17, "bold"),
    pady=30
)
logo.pack()

tk.Label(
    sidebar,
    text="MAIN MENU",
    bg=SIDEBAR,
    fg=MUTED,
    font=("Arial", 9, "bold")
).pack(anchor="w", padx=20, pady=(15, 10))


def sidebar_button(text, command):
    btn = tk.Button(
        sidebar,
        text=text,
        command=command,
        bg=SIDEBAR,
        fg=WHITE,
        activebackground=GOLD,
        activeforeground=BG,
        font=("Arial", 11),
        bd=0,
        anchor="w",
        padx=25,
        pady=13,
        cursor="hand2"
    )
    btn.pack(fill="x", padx=8, pady=3)
    return btn


# ------------------ HEADER ------------------

header = tk.Frame(main, bg=BG, height=80)
header.pack(fill="x", padx=30, pady=20)
header.pack_propagate(False)

page_title = tk.Label(
    header,
    text="Dashboard",
    bg=BG,
    fg=WHITE,
    font=("Arial", 23, "bold")
)
page_title.pack(side="left")

tk.Label(
    header,
    text="STUDENT ADMINISTRATION",
    bg=BG,
    fg=GOLD,
    font=("Arial", 10, "bold")
).pack(side="right", padx=10)


# ------------------ CONTENT AREA ------------------

content = tk.Frame(main, bg=BG)
content.pack(fill="both", expand=True, padx=30, pady=5)


def clear_content():
    for widget in content.winfo_children():
        widget.destroy()


def change_page(title):
    global current_page
    current_page = title
    page_title.config(text=title)


# ------------------ DASHBOARD ------------------

def show_dashboard():
    change_page("Dashboard")
    clear_content()

    # Statistics cards
    cards_frame = tk.Frame(content, bg=BG)
    cards_frame.pack(fill="x", pady=10)

    total = len(students)
    average = calculate_average()
    course_count = len(set(s.get("course", "") for s in students if s.get("course")))

    statistics = [
        ("TOTAL STUDENTS", str(total)),
        ("AVAILABLE COURSES", str(course_count)),
        ("AVERAGE MARKS", f"{average:.1f}%")
    ]

    for title, value in statistics:
        card = tk.Frame(cards_frame, bg=CARD, padx=20, pady=20)
        card.pack(side="left", fill="both", expand=True, padx=7)

        tk.Label(
            card,
            text=title,
            bg=CARD,
            fg=MUTED,
            font=("Arial", 10, "bold")
        ).pack(anchor="w")

        tk.Label(
            card,
            text=value,
            bg=CARD,
            fg=GOLD,
            font=("Arial", 25, "bold")
        ).pack(anchor="w", pady=10)

    # Recent students
    tk.Label(
        content,
        text="RECENT STUDENTS",
        bg=BG,
        fg=WHITE,
        font=("Arial", 14, "bold")
    ).pack(anchor="w", pady=(25, 12))

    columns = ("Admission", "Name", "Course", "Mark", "Grade")

    table = ttk.Treeview(
        content,
        columns=columns,
        show="headings",
        height=8
    )

    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=140, anchor="center")

    table.pack(fill="x")

    for student in students[-8:]:
        mark = float(student.get("mark", 0))
        table.insert(
            "",
            "end",
            values=(
                student.get("admission", ""),
                student.get("name", ""),
                student.get("course", ""),
                mark,
                calculate_grade(mark)
            )
        )

    # Performance chart
    tk.Label(
        content,
        text="STUDENT PERFORMANCE",
        bg=BG,
        fg=WHITE,
        font=("Arial", 14, "bold")
    ).pack(anchor="w", pady=(20, 8))

    chart = tk.Canvas(
        content,
        height=130,
        bg=CARD,
        highlightthickness=0
    )
    chart.pack(fill="x")

    chart_width = 700
    chart.create_line(30, 105, chart_width, 105, fill=MUTED)

    if students:
        bar_width = min(45, (chart_width - 60) // len(students))
        for index, student in enumerate(students):
            mark = max(0, min(100, float(student.get("mark", 0))))
            x = 40 + index * bar_width
            bar_height = mark * 0.8

            chart.create_rectangle(
                x, 105 - bar_height,
                x + bar_width - 8, 105,
                fill=GOLD,
                outline=""
            )
            chart.create_text(
                x + (bar_width - 8) / 2,
                115,
                text=str(index + 1),
                fill=WHITE,
                font=("Arial", 8)
            )
    else:
        chart.create_text(
            350, 60,
            text="No student marks available yet",
            fill=MUTED,
            font=("Arial", 11)
        )


# ------------------ STUDENT FORM ------------------

def student_form(existing=None):
    editing = existing is not None

    form = tk.Toplevel(root)
    form.title("Edit Student" if editing else "Register Student")
    form.geometry("430x480")
    form.configure(bg=BG)
    form.resizable(False, False)
    form.transient(root)
    form.grab_set()

    tk.Label(
        form,
        text="EDIT STUDENT" if editing else "REGISTER STUDENT",
        bg=BG,
        fg=GOLD,
        font=("Arial", 18, "bold")
    ).pack(pady=20)

    fields = {}

    for label in ["Student Name", "Admission Number"]:
        tk.Label(
            form,
            text=label,
            bg=BG,
            fg=WHITE,
            font=("Arial", 10)
        ).pack(anchor="w", padx=40)

        entry = tk.Entry(
            form,
            bg=CARD,
            fg=WHITE,
            insertbackground=WHITE,
            font=("Arial", 11),
            bd=0
        )
        entry.pack(fill="x", padx=40, pady=(5, 15), ipady=8)
        fields[label] = entry

    tk.Label(
        form,
        text="Course",
        bg=BG,
        fg=WHITE
    ).pack(anchor="w", padx=40)

    course_var = tk.StringVar()
    course_box = ttk.Combobox(
        form,
        textvariable=course_var,
        values=COURSES,
        state="readonly"
    )
    course_box.pack(fill="x", padx=40, pady=(5, 15), ipady=5)

    tk.Label(
        form,
        text="Marks (0 - 100)",
        bg=BG,
        fg=WHITE
    ).pack(anchor="w", padx=40)

    mark_entry = tk.Entry(
        form,
        bg=CARD,
        fg=WHITE,
        insertbackground=WHITE,
        font=("Arial", 11),
        bd=0
    )
    mark_entry.pack(fill="x", padx=40, pady=(5, 15), ipady=8)

    if editing:
        fields["Student Name"].insert(0, existing.get("name", ""))
        fields["Admission Number"].insert(0, existing.get("admission", ""))
        course_var.set(existing.get("course", ""))
        mark_entry.insert(0, str(existing.get("mark", "")))

    def save_form():
        name = fields["Student Name"].get().strip()
        admission = fields["Admission Number"].get().strip()
        course = course_var.get()
        mark_text = mark_entry.get().strip()

        if not name or not admission or not course or not mark_text:
            messagebox.showerror("Missing Information", "Please fill in all fields.")
            return

        try:
            mark = float(mark_text)
            if not 0 <= mark <= 100:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Marks", "Enter a mark between 0 and 100.")
            return

        for student in students:
            if student.get("admission") == admission and student is not existing:
                messagebox.showerror("Duplicate", "Admission number already exists.")
                return

        record = {
            "name": name,
            "admission": admission,
            "course": course,
            "mark": mark
        }

        if editing:
            existing.update(record)
        else:
            students.append(record)

        save_students()
        form.destroy()
        show_students()
        messagebox.showinfo("Success", "Student information saved successfully!")

    tk.Button(
        form,
        text="SAVE STUDENT",
        command=save_form,
        bg=GOLD,
        fg=BG,
        font=("Arial", 11, "bold"),
        bd=0,
        cursor="hand2",
        pady=12
    ).pack(fill="x", padx=40, pady=15)


# ------------------ STUDENT RECORDS ------------------

def show_students():
    change_page("Student Records")
    clear_content()

    toolbar = tk.Frame(content, bg=BG)
    toolbar.pack(fill="x", pady=10)

    search_var = tk.StringVar()

    search_entry = tk.Entry(
        toolbar,
        textvariable=search_var,
        bg=CARD,
        fg=WHITE,
        insertbackground=WHITE,
        font=("Arial", 11),
        bd=0
    )
    search_entry.pack(side="left", fill="x", expand=True, ipady=10)

    def action_button(text, command):
        tk.Button(
            toolbar,
            text=text,
            command=command,
            bg=GOLD,
            fg=BG,
            font=("Arial", 9, "bold"),
            bd=0,
            padx=12,
            pady=10,
            cursor="hand2"
        ).pack(side="left", padx=5)

    table_frame = tk.Frame(content, bg=BG)
    table_frame.pack(fill="both", expand=True, pady=15)

    columns = ("Admission", "Name", "Course", "Mark", "Grade")
    table = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings"
    )

    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=140, anchor="center")

    table.pack(fill="both", expand=True)

    def refresh_table(*args):
        table.delete(*table.get_children())
        query = search_var.get().lower()

        for student in students:
            if query in str(student.get("name", "")).lower() or \
               query in str(student.get("admission", "")).lower():
                mark = float(student.get("mark", 0))
                table.insert(
                    "",
                    "end",
                    values=(
                        student.get("admission", ""),
                        student.get("name", ""),
                        student.get("course", ""),
                        mark,
                        calculate_grade(mark)
                    )
                )

    def selected_student():
        selection = table.selection()
        if not selection:
            messagebox.showwarning("Select Student", "Please select a student first.")
            return None

        admission = table.item(selection[0], "values")[0]
        return next(
            (s for s in students if s.get("admission") == admission),
            None
        )

    def edit_selected():
        student = selected_student()
        if student:
            student_form(student)

    def delete_selected():
        student = selected_student()
        if student and messagebox.askyesno(
            "Confirm Delete",
            f"Delete {student.get('name')}?"
        ):
            students.remove(student)
            save_students()
            refresh_table()
            messagebox.showinfo("Deleted", "Student deleted successfully.")

    action_button("ADD STUDENT", lambda: student_form())
    action_button("EDIT", edit_selected)
    action_button("DELETE", delete_selected)

    search_var.trace_add("write", refresh_table)
    refresh_table()


# ------------------ NAVIGATION ------------------

sidebar_button("▣   Dashboard", show_dashboard)
sidebar_button("＋   Register Student", lambda: student_form())
sidebar_button("▤   Student Records", show_students)



def logout():
    if messagebox.askyesno(
        "Logout",
        "Are you sure you want to log out?"
    ):
        import subprocess
        import sys

        login_path = os.path.join(BASE_DIR, "login.py")

        if not os.path.exists(login_path):
            messagebox.showerror(
                "Error",
                "login.py could not be found."
            )
            return

        try:
            subprocess.Popen(
                [sys.executable, login_path],
                cwd=BASE_DIR
            )
            root.destroy()

        except Exception as error:
            messagebox.showerror(
                "Logout Error",
                str(error)
            )



tk.Button(
    sidebar,
    text="↪   Logout",
    command=logout,
    bg=SIDEBAR,
    fg=RED,
    activebackground=RED,
    activeforeground=WHITE,
    font=("Arial", 11),
    bd=0,
    anchor="w",
    padx=25,
    pady=15,
    cursor="hand2"
).pack(side="bottom", fill="x", padx=8, pady=15)


# ------------------ START APPLICATION ------------------

show_dashboard()
root.mainloop()
