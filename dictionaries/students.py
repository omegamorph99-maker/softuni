student_records = {}
checking_course = ''

while True:
    student_input = input().split(':')

    if len(student_input) == 1:
        checking_course = student_input[0]
        break

    student_name = student_input[0]
    student_id = student_input[1]
    student_course = student_input[2]

    student_records[student_name] = {student_id: student_course}

if '_' in checking_course:
    checking_course = checking_course.replace('_', ' ')

for student, record in student_records.items():
    for id, course in record.items():
        if course == checking_course:
            print(f'{student} - {id}')