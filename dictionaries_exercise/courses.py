courses = {}

while True:
    current_course = input().split(' : ')

    if current_course[0] == 'end':
        break

    course_name, student = current_course[0], current_course[1]

    if course_name not in courses.keys():
        courses[course_name] = []
    courses[course_name].append(student)


for key in courses.keys():
    print(f'{key}: {len(courses[key])}')
    for student in courses[key]:
        print(f'-- {student}')