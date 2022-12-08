import fileinput

data = open('input.txt', 'r').read()

def part_one(data, marker_lenght):
    for i in range(len(data)):
        if i + marker_lenght < len(data):
            marker = data[i:i + marker_lenght]
            if len(marker) == len(set(marker)):
                return i + marker_lenght
        else:
            return 'Not found'
print(part_one(data, 14))