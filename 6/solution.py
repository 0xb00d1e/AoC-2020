def part1():
    input_data = load_data()
    parsed_answers = parse_answers(input_data)
    answer = sum(len(sub) for sub in parsed_answers)
    print(f'Answer - Part 1: {answer}')


def parse_answers(input_data):
    parsed = []
    for answers in input_data.split('\n\n'):
        parsed.append(set(''.join(answer for answer in answers.split('\n'))))
    return parsed


def load_data():
    with open('input') as f:
        data = f.read()
    return data


if __name__ == '__main__':
    part1()
