def part1():
    input_data = load_data()
    invalid_number = find_invalid_number(input_data)
    print(f'Answer - Part1: {invalid_number}')


def part2():
    input_data = load_data()
    invalid_number = find_invalid_number(input_data)
    numbers = find_numbers_in_sum(input_data, invalid_number)
    numbers.sort()
    print(f'Answer - Part2: {numbers[0] + numbers[-1]}')


def find_numbers_in_sum(input_data, invalid_number):
    for i, outer_value in enumerate(input_data):
        for j, inner_value in enumerate(input_data, start=1):
            window = input_data[i:j]
            if sum(window) == invalid_number:
                return window


def find_invalid_number(input_data):
    for i, value in enumerate(input_data):
        if i < 25:
            continue
        previous_slice = input_data[i-25:i]
        if not any_two_sum_to(previous_slice, value):
            return value


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
    part2()
