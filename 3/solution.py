def part1():
    data = load_data()
    grid = parse_data(data)
    step = (3, 1)
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
