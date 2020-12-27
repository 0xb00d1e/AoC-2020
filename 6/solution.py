def part1():
    input_data = load_data()
    parsed_answers = parse_answers_1(input_data)
    answer = sum(len(sub) for sub in parsed_answers)
    print(f'Answer - Part 1: {answer}')


def part2():
    input_data = load_data()
    parsed_answers = parse_answers_2(input_data)
    accumulator = 0
    for answers in parsed_answers:
        intersection = set.intersection(*answers)
        accumulator += len(intersection)
    print(f'Answer - Part 2: {accumulator}')


def parse_answers_1(input_data):
    parsed = []
    for answers in input_data.split('\n\n'):
        parsed.append(set(''.join(answer for answer in answers.split('\n'))))
    return parsed


def parse_answers_2(input_data):
    parsed = []
    for answers in input_data.split('\n\n'):
        parsed.append([set(answer) for answer in answers.split('\n') if answer])
    return parsed


def load_data():
    with open('input') as f:
        data = f.read()
    return data


if __name__ == '__main__':
    part1()
    part2()
