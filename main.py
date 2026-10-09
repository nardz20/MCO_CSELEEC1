"""Student Grade / GWA Calculator — beginner-friendly console application."""

def get_student_information():
    """Collect and return basic student information."""
    print("\nStudent Information")
    print("-" * 48)
    student = {
        "name": input("Student name: ").strip(),
        "student_id": input("Student ID: ").strip(),
        "course": input("Course/program: ").strip(),
        "year_level": input("Year level: ").strip()
    }
    return student


def main():
    print("=" * 48)
    print("       STUDENT GRADE / GWA CALCULATOR")
    print("=" * 48)
    student = get_student_information()
    print("\nStudent details entered:")
    print(f"Name: {student['name']}")
    print(f"Student ID: {student['student_id']}")
    print(f"Course: {student['course']}")
    print(f"Year level: {student['year_level']}")


if __name__ == "__main__":
    main()
