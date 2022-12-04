import fileinput

data = open('input', 'r').read().splitlines()

def part_one(input):
    sum = 0
    for string in input:
        firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
        for letter in firstpart:
            if letter in secondpart:
                if letter.isupper():
                    sum += ord(letter) - ord('A') + 27
                else:
                    sum += ord(letter) - ord('a') + 1
                break
    print(sum)

def part_two(input):
    sum = 0
    for i in range(0, len(input) - 2, 3):
        for letter in data[i]:
            if letter in data[i + 1] and letter in data[i + 2]:
                if letter.isupper():
                    sum += ord(letter) - ord('A') + 27
                else:
                    sum += ord(letter) - ord('a') + 1
                break
    print(sum)

part_one(data)
part_two(data)