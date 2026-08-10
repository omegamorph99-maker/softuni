crops = input().split(" & ")
command = input()

while command != "Collect!":
    command = command.split()
    initial_command = command[0]

    if initial_command == "Plant":
        crop = command[1]
        if crop not in crops:
            crops.insert(0, crop)
    elif initial_command == "Transplant":
        crop = command[1]
        if crop in crops:
            crops.remove(crop)
            crops.append(crop)
    elif initial_command == "Replace":
        crop_index = int(command[1])
        second_crop_index = int(command[2])
        if crop_index in range(len(crops)) and second_crop_index in range(len(crops)):
            crops[crop_index], crops[second_crop_index] = crops[second_crop_index], crops[crop_index]
    elif initial_command == "Uproot":
        crop = command[1]
        if crop in crops:
            crops.remove(crop)

    command = input()


print(' | '.join(crops))