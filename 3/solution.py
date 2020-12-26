import functools


def part1():
    data = load_data()
    grid = parse_data(data)
    i = 1
    tree_count = 0
    width = len(data[0])

    while True:
        try:
            if grid[((3*i) % width, 1*i)] == '#':
                tree_count += 1
        except KeyError:
            break
        i += 1
    print(f'Answer - Part 1: {tree_count}')


def part2():
    data = load_data()
    grid = parse_data(data)
    steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    tree_counts = []
    width = len(data[0])

    for step in steps:
        tree_count = 0
        i = 1
        while True:
            try:
                if grid[((step[0]*i) % width, step[1]*i)] == '#':
                    tree_count += 1
            except KeyError:
                break
            i += 1
        tree_counts.append(tree_count)
    
    product = functools.reduce(lambda x,y: x*y, tree_counts)
    print(f'Answer - Part 2: {product}')


def parse_data(data):
    grid = {}
    for y, row in enumerate(data):
        for x, value in enumerate(row):
            grid[(x, y)] = value
    return grid


def load_data():
    with open('input') as f:
        data = f.read()
    return [l.strip() for l in data.splitlines()]


if __name__ == '__main__':
    part1()
    part2()
