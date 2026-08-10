number_of_electrons = int(input())

shell_count = 1
electrons_in_shell = []

while number_of_electrons > 0:
    current_electrons = 2 * shell_count ** 2
    if number_of_electrons >= current_electrons:
        electrons_in_shell.append(current_electrons)
    else:
        electrons_in_shell.append(number_of_electrons)

    number_of_electrons -= current_electrons
    shell_count += 1

print(electrons_in_shell)