import fileinput

data = open('input.txt', 'r').read()

def part_one(data, marker_lenght):
    for i, letter in enumerate(data):
        marker = []
        marker.append(letter)
        for j in range(1, marker_lenght):
            marker.append(data[i + j])
        if len(marker) == len(set(marker)):
            return i + j + 1
            
print(part_one(data, 4))