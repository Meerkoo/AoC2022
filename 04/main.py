import fileinput

data = open('input', 'r').read().splitlines()

def part_one(input):
    sum = 0
    for line in input:
        firstpair, secondpair = line.split(',')
        min1, max1 = tuple(map(int, firstpair.split('-')))
        min2, max2 = tuple(map(int, secondpair.split('-')))
        firstelf = []
        secondelf = []
        for i in range(max1 - min1 + 1):
            firstelf.append(i + min1)
        for i in range(max2 - min2 + 1):
            secondelf.append(i + min2)
        if set(firstelf).issubset(set(secondelf)) or set(secondelf).issubset(set(firstelf)):
            sum += 1
    print(sum)

def part_two(input):
    sum = 0
    for line in input:
        firstpair, secondpair = line.split(',')
        min1, max1 = tuple(map(int, firstpair.split('-')))
        min2, max2 = tuple(map(int, secondpair.split('-')))
        firstelf = []
        secondelf = []
        for i in range(max1 - min1 + 1):
            firstelf.append(i + min1)
        for i in range(max2 - min2 + 1):
            secondelf.append(i + min2)
        for number in firstelf:
            if number in secondelf:
                sum += 1
                break
    print(sum)

part_one(data)
part_two(data)