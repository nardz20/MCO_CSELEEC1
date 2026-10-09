"""Student Grade / GWA Calculator — beginner-friendly console application."""

def get_non_empty_text(prompt):
    """Ask until the user enters non-empty text."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def get_positive_integer(prompt):
    """Ask until the user enters a positive whole number."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_grade(prompt):
    """Accept grades from 1.00 to 5.00 in 0.25 increments."""
    while True:
        try:
            grade = float(input(prompt))
            if 1.00 <= grade <= 5.00 and abs(grade * 4 - round(grade * 4)) < 1e-9:
                return grade
            print("Enter a grade from 1.00 to 5.00 in 0.25 increments.")
        except ValueError:
            print("Invalid grade. Enter a number, such as 1.75.")


def get_student_information():
    """Collect and return basic student information."""
    print("\nStudent Information")
    print("-" * 48)
    return {
        "name": get_non_empty_text("Student name: "),
        "student_id": get_non_empty_text("Student ID: "),
        "course": get_non_empty_text("Course/program: "),
        "year_level": get_positive_integer("Year level: ")
    }


def get_subjects():
    """Collect multiple subjects with validated units and grades."""
    subjects = []
    number_of_subjects = get_positive_integer("\nHow many subjects? ")

    for number in range(1, number_of_subjects + 1):
        print(f"\nSubject {number}")
        name = get_non_empty_text("Subject name: ")
        units = get_positive_integer("Units: ")
        grade = get_grade("Grade (1.00-5.00): ")
        subjects.append({
            "name": name,
            "units": units,
            "grade": grade,
            "weighted_grade": calculate_weighted_grade(grade, units)
        })

    return subjects


def calculate_weighted_grade(grade, units):
    """Calculate the weighted grade for one subject."""
    return grade * units


def calculate_gwa(subjects):
    """Return total units, total weighted grades, and GWA."""
    total_units = 0
    total_weighted_grades = 0

    for subject in subjects:
        total_units += subject["units"]
        total_weighted_grades += subject["weighted_grade"]

    gwa = total_weighted_grades / total_units
    return total_units, total_weighted_grades, gwa


def main():
    print("=" * 48)
    print("       STUDENT GRADE / GWA CALCULATOR")
    print("=" * 48)
    student = get_student_information()
    subjects = get_subjects()
    total_units, total_weighted_grades, gwa = calculate_gwa(subjects)

    print("\nStudent details entered:")
    print(f"Name: {student['name']}")
    print(f"Student ID: {student['student_id']}")
    print(f"Course: {student['course']}")
    print(f"Year level: {student['year_level']}")

    print("\nSubjects entered:")
    for subject in subjects:
        print(
            f"{subject['name']} | Units: {subject['units']} | "
            f"Grade: {subject['grade']:.2f} | "
            f"Weighted grade: {subject['weighted_grade']:.2f}"
        )

    print(f"\nTotal units: {total_units}")
    print(f"Total weighted grades: {total_weighted_grades:.2f}")
    print(f"GWA: {gwa:.2f}")


if __name__ == "__main__":
    main()
