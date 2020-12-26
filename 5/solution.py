def part1():
    input_data = load_data()
    binary_repr = convert_to_binary_repr(input_data)
    binary_repr.sort()
    print(binary_repr[-1])


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
