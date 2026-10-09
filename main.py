"""Student Grade / GWA Calculator — beginner-friendly console application."""

def get_student_information():
    """Collect and return basic student information."""
    print("\nStudent Information")
    print("-" * 48)
    return {
        "name": input("Student name: ").strip(),
        "student_id": input("Student ID: ").strip(),
        "course": input("Course/program: ").strip(),
        "year_level": input("Year level: ").strip()
    }


def get_subjects():
    """Collect multiple subjects with units and grades."""
    subjects = []
    number_of_subjects = int(input("\nHow many subjects? "))

    for number in range(1, number_of_subjects + 1):
        print(f"\nSubject {number}")
        name = input("Subject name: ").strip()
        units = int(input("Units: "))
        grade = float(input("Grade (1.00-5.00): "))
        subjects.append({
            "name": name,
            "units": units,
            "grade": grade
        })

    return subjects


def main():
    print("=" * 48)
    print("       STUDENT GRADE / GWA CALCULATOR")
    print("=" * 48)
    student = get_student_information()
    subjects = get_subjects()

    print("\nStudent details entered:")
    print(f"Name: {student['name']}")
    print(f"Student ID: {student['student_id']}")
    print(f"Course: {student['course']}")
    print(f"Year level: {student['year_level']}")

    print("\nSubjects entered:")
    for subject in subjects:
        print(f"{subject['name']} | Units: {subject['units']} | Grade: {subject['grade']:.2f}")


if __name__ == "__main__":
    main()
