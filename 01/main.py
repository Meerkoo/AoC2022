import fileinput

calories = open('input', 'r').read().splitlines()

elf_calories = []
total_calories = 0

for x in calories:
    if x == '':
        elf_calories.append(total_calories)
        total_calories = 0
    else:
        total_calories += int(x)

print(max(elf_calories))

sum_top = 0
for i in range(3):
    sum_top += int(max(elf_calories))
    elf_calories.remove(max(elf_calories))

print(sum_top)