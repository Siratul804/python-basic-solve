def calculate_grades(student_mark):
    if student_mark < 50:
        return "F"
    elif student_mark < 65:
        return "P"
    elif student_mark < 75:
        return "C"
    elif student_mark < 85:
        return "D"
    else:
        return "HD"

mark = float(input("Enter the student's mark (0–100): "))
grade = calculate_grades(mark)
print("Grade:", grade)
