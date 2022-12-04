import fileinput

input = open('input', 'r').read().splitlines()

options = {'X': 1, 'Y': 2, 'Z': 3}
win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
lose = {'A': 'Z', 'B': 'X', 'C': 'Y'}
tie = {'A': 'X', 'B': 'Y', 'C': 'Z'}

#a, x = rock b, y = paper c, z = cissor x = lose y = draw z = win
def part_one(input):
    score = 0
    for plays in input:
        if plays[2] == lose[plays[0]]:
            score += options[plays[2]]
        elif plays[2] == tie[plays[0]]:
            score += 3 + options[plays[2]]
        else:
            score += 6 + options[plays[2]]
    return score

def part_two(input):
    score = 0
    for plays in input:
        if plays[2] == 'X':
            score += options[lose[plays[0]]]
        elif plays[2] == 'Y':
            score += 3 + options[tie[plays[0]]]
        else:
            score += 6 + options[win[plays[0]]]
    return score

print(part_one(input))
print(part_two(input))