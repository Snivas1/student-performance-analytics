
def calculate_total(marks):
    """Calculate total marks."""
    return sum(marks)


def calculate_average(marks):
    """Calculate average marks."""
    return sum(marks) / len(marks)


def calculate_grade(average):
    """Assign a grade based on average marks."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def calculate_result(marks):
    """Pass if every subject mark is at least 40."""
    if all(mark >= 40 for mark in marks):
        return "Pass"
    return "Fail"
