students_log = {}

number_of_lines = int(input())
line = 0

while line < number_of_lines:
    line += 1
    student = input()
    grade = float(input())

    if student not in students_log.keys():
        students_log[student] = []

    students_log[student].append(grade)

for key in list(students_log.keys()):
    if sum(students_log[key]) / len(students_log[key]) < 4.50:
       del students_log[key]


for key in students_log.keys():
    average_gade = sum(students_log[key]) / len(students_log[key])
    print(f'{key} -> {average_gade:.2f}')