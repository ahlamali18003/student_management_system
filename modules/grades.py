def calculate_grade(mark):
    if mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    return "F"


def calculate_average(marks):
    if len(marks) == 0:
        return 0
    return sum(marks) / len(marks)
