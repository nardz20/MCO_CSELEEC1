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
            is_quarter_increment = abs(grade * 4 - round(grade * 4)) < 1e-9
            if 1.00 <= grade <= 5.00 and is_quarter_increment:
                return grade
            print("Enter a grade from 1.00 to 5.00 in 0.25 increments.")
        except ValueError:
            print("Invalid grade. Enter a number, such as 1.75.")


def get_student_information():
    """Collect and return basic student information."""
    print("\nStudent Information")
    print("-" * 64)
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


def get_remark(gwa):
    """Return an example remark; institutions may use different rules."""
    if gwa <= 1.50:
        return "Excellent"
    elif gwa <= 2.50:
        return "Good Standing"
    elif gwa < 3.00:
        return "Needs Improvement"
    return "At Risk / Review Required"


def display_results(student, subjects, total_units, total_weighted_grades, gwa):
    """Display all results in organized console sections."""
    print("\n" + "=" * 64)
    print("                 STUDENT GRADE / GWA CALCULATOR")
    print("=" * 64)
    print("\nStudent Information")
    print("-" * 64)
    print(f"Name:       {student['name']}")
    print(f"Student ID: {student['student_id']}")
    print(f"Course:     {student['course']}")
    print(f"Year Level: {student['year_level']}")

    print("\nSubject Results")
    print("-" * 64)
    print(f"{'Subject':<28}{'Units':>8}{'Grade':>10}{'Weighted':>14}")
    print("-" * 64)
    for subject in subjects:
        print(
            f"{subject['name'][:27]:<28}"
            f"{subject['units']:>8}"
            f"{subject['grade']:>10.2f}"
            f"{subject['weighted_grade']:>14.2f}"
        )

    print("-" * 64)
    print(f"Total Units:            {total_units}")
    print(f"Total Weighted Grades:  {total_weighted_grades:.2f}")
    print(f"GWA:                    {gwa:.2f}")
    print(f"Remark:                 {get_remark(gwa)}")
    print("=" * 64)
    print("Note: Remarks are examples. Follow your school's official rules.")


def main():
    """Run the calculator from start to finish."""
    print("=" * 64)
    print("                 STUDENT GRADE / GWA CALCULATOR")
    print("=" * 64)
    student = get_student_information()
    subjects = get_subjects()
    total_units, total_weighted_grades, gwa = calculate_gwa(subjects)
    display_results(student, subjects, total_units, total_weighted_grades, gwa)


if __name__ == "__main__":
    main()
