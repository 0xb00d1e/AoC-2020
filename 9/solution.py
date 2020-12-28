def part1():
    input_data = load_data()

    for i, value in enumerate(input_data):
        if i < 25:
            continue
        previous_slice = input_data[i-25:i]
        if not any_two_sum_to(previous_slice, value):
            print(f'Answer - Part1: {value}')
            break


def any_two_sum_to(numbers, value):
    for number in numbers:
        compliment = value - number
        if compliment in numbers:
            return True
    return False


def load_data():
    with open('input') as f:
        data = f.read()
    return [int(l.strip()) for l in data.splitlines()]


if __name__ == '__main__':
    part1()
