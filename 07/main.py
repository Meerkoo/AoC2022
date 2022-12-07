import fileinput

data = open('input', 'r').read().splitlines()

files = []
sizes = []

for line in data:
    command = line.split(' ')
    if command[0] == '$':
        if command[1] == 'cd':
            if command[2] == '..':
                sizes.append(files.pop())
                if files:
                    files[-1] += sizes[-1]
            else :
                files.append(0)
    if command[0].isdigit():
        files[-1] += int(command[0])

while files:
    sizes.append(files.pop())
    if files:
        files[-1] += sizes[-1]


print(sum(s for s in sizes if s <= 100000))

space_required = max(sizes) - 40000000
print(min(s for s in sizes if s >= space_required))
