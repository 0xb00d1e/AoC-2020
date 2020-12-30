import collections


def part1():
    adapters = load_data()
    adapters.sort()
    device_joltage = adapters[-1] + 3
    adapters.append(device_joltage)

    current_joltage = 0
    differences = []
    for adapter in adapters:
        possible_joltages = (current_joltage+1, current_joltage+2, current_joltage+3)
        for joltage in possible_joltages:
            if joltage == adapter:
                differences.append(adapter - current_joltage)
                current_joltage = adapter

    counted_collection = collections.Counter(differences)
    answer = counted_collection[1] * counted_collection[3]
    print(f'Answer - Part1: {answer}')


def load_data():
    with open('input') as f:
        data = f.read()
    return [int(l.strip()) for l in data.splitlines()]


if __name__ == '__main__':
    part1()
