students_data = {
    "goudu":97,
    "siri":89,
    "kiran":76,
    "ramu":85,
    "sandeep":76,
    "lakshmi":64,
    "manju":58,
    "divya":46,
    "anil":33,
    "chetu":21,
}
students_grades = {}
for student in (students_data):
    marks = students_data[student]
    if marks>90:
        students_grades[student] = "A+"
    elif marks>80:
        students_grades[student] = "A"
    elif marks>70:
        students_grades[student] = "B+"
    elif marks>60:
        students_grades[student] = "B"
    elif marks>50:
        students_grades[student] = "C"
    elif marks>40:
        students_grades[student] = "D"
    else:
        students_grades[student] = "E"
print(students_grades)
