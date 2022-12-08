import fileinput

data = open('input.txt', 'r').read().splitlines()


trees = [[x[i] for x in data] for i in range(len(data[0]))]
vertical = [[x[i] for x in trees] for i in range(len(trees[0]))]

def part_one():
    visible = 0
    for y in range(len(trees)):
        for x in range(len(trees[0])):
            tree = trees[y][x]
            left = any(i >= tree for i in trees[y][:x])
            right = any(i >= tree for i in trees[y][x + 1:])
            up = any(i >= tree for i in vertical[x][:y])
            down = any(i >= tree for i in vertical[x][y + 1:])
            if not all((left, right, down, up)):
                visible += 1
    print(visible)

def part_two():
    score = []
    for y in range(len(trees)):
        for x in range(len(trees[0])):
            tree = trees[y][x]
            up, right, down, left = 0, 0, 0, 0
            for i in reversed(trees[y][:x]):
                left += 1
                if i >= tree:
                    break
            for i in trees[y][x + 1:]:
                right += 1
                if i >= tree:
                    break
            for i in reversed(vertical[x][:y]):
                up += 1
                if i >= tree:
                    break
            for i in vertical[x][y + 1:]:
                down += 1
                if i >= tree:
                    break
            score.append(right * left * up * down)
    print(max(score))

part_one()
part_two()