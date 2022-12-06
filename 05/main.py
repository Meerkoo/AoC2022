import fileinput

data = open('input.txt', 'r').read().splitlines()

stacks = []

for i in range(1, len(data[0]) - 1, 4):
    stack = []
    for j, line in enumerate(data):
        if j == 8:
            break
        if line[i] != ' ':
            stack.insert(0, line[i])
    stacks.append(stack)

moves = data[10:]

def part_one():
    for move in moves:
        a = move.split(' ')
        a.remove('move')
        a.remove('from')
        a.remove('to')
        a = list(map(int, a))
        for i in range(a[0]):
            container = stacks[a[1] - 1].pop()
            stacks[a[2] - 1].append(container)

    for stack in stacks:
        print(stack.pop())

def part_two():
    for move in moves:
            a = move.split(' ')
            a.remove('move')
            a.remove('from')
            a.remove('to')
            a = list(map(int, a))
    
            containers = []
            for i in range(a[0]):
                container = stacks[a[1] - 1].pop()
                containers.insert(0, container)
            stacks[a[2] - 1].extend(containers)
    
    for stack in stacks:
        print(stack.pop())