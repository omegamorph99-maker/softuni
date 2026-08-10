initial_lessons = input().split(', ')

command = input().split(':')

while len(command) > 1:

    initial_command = command[0]

    if command[0] == 'Add':
        lesson_title = command[1]
        if lesson_title not in initial_lessons:
            initial_lessons.append(lesson_title)

    elif command[0] == 'Insert':
        lesson_title = command[1]
        index = int(command[2])
        if lesson_title not in initial_lessons:
            initial_lessons.insert(index, lesson_title)

    elif command[0] == 'Remove':
        lesson_title = command[1]
        if lesson_title in initial_lessons:
            initial_lessons.remove(lesson_title)
            if f'{lesson_title}-Exercise' in initial_lessons:
                initial_lessons.remove(f'{lesson_title}-Exercise')

    elif command[0] == 'Swap':
        lesson_title = command[1]
        another_lesson_title = command[2]
        if lesson_title in initial_lessons and another_lesson_title in initial_lessons:
            lesson_title_index = initial_lessons.index(lesson_title)
            another_lesson_title_index = initial_lessons.index(another_lesson_title)

            initial_lessons[lesson_title_index], initial_lessons[another_lesson_title_index] = initial_lessons[another_lesson_title_index], initial_lessons[lesson_title_index]

        if f'{lesson_title}-Exercise' in initial_lessons and f'{another_lesson_title}-Exercise' in initial_lessons:
            initial_lessons[lesson_title_index +1], initial_lessons[another_lesson_title_index +1] = initial_lessons[
                another_lesson_title_index +1], initial_lessons[lesson_title_index +1]
        elif f'{lesson_title}-Exercise' in initial_lessons:
            initial_lessons.insert(another_lesson_title_index+1,f'{lesson_title}-Exercise')
            initial_lessons.pop(lesson_title_index+2)
        elif f'{another_lesson_title}-Exercise' in initial_lessons:
            initial_lessons.insert(lesson_title_index+1, f'{another_lesson_title}-Exercise')
            initial_lessons.pop(another_lesson_title_index+2)
    elif command[0] == 'Exercise':
        lesson_title = command[1]
        if lesson_title not in initial_lessons:
            initial_lessons.append(lesson_title)
            initial_lessons.append(f'{lesson_title}-Exercise')
        elif lesson_title in initial_lessons and f'{lesson_title}-Exercise' not in initial_lessons:
            lesson_title_index = initial_lessons.index(lesson_title)
            initial_lessons.insert(lesson_title_index+1, f'{lesson_title}-Exercise')

    command = input().split(':')


for index, lesson_title in enumerate(initial_lessons):
    print(f'{index+1}.{lesson_title}')