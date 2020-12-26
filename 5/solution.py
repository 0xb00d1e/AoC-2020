def part1():
    input_data = load_data()
    binary_repr = convert_to_binary_repr(input_data)
    binary_repr.sort()
    print(f'Answer - Part 1: {binary_repr[-1]}')


def part2():
    input_data = load_data()
    binary_repr = convert_to_binary_repr(input_data)
    binary_repr.sort()

    for i in range(0, len(binary_repr)):
        try:
            if binary_repr[i+1] - binary_repr[i] != 1:
                print(f'Answer - Part 2: {binary_repr[i+1] - 1}')
                break
        except IndexError:
            break


def convert_to_binary_repr(input_data):
    return [
        int(
            line.replace('F', '0')
            .replace('B', '1')
            .replace('L', '0')
            .replace('R', '1')
        , 2)
        for line in input_data
    ]


def load_data():
    with open('input') as f:
        data = f.read()
    return [l.strip() for l in data.splitlines()]


if __name__ == '__main__':
    part1()
    part2()
