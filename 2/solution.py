import re


def part1():
    data = set(load_data())
    policies = parse_policies_1(data)
    valid_policies = find_valid_policies_1(policies)
    print(f'Answer - Part 1: {len(valid_policies)}')


def find_valid_policies_1(policies):
    valid_policies = []
    for policy in policies:
        character_count = policy['password'].count(policy['character'])
        if (character_count >= policy['min_occurrences']) and (character_count <= policy['max_occurrences']):
            valid_policies.append(policy)
    return valid_policies


def parse_policies_1(data):
    policies = []
    pattern = re.compile(r'(?P<min_occurrences>\d+)-(?P<max_occurrences>\d+)\s(?P<character>\w):\s(?P<password>.*)')
    for line in data:
        policy = {}
        matches = re.match(pattern, line)
        policy['min_occurrences'] = int(matches.group('min_occurrences'))
        policy['max_occurrences'] = int(matches.group('max_occurrences'))
        policy['character'] = matches.group('character')
        policy['password'] = matches.group('password')
        policies.append(policy)
    return policies


def part2():
    data = set(load_data())
    policies = parse_policies_2(data)
    valid_policies = find_valid_policies_2(policies)
    print(f'Answer - Part 2: {len(valid_policies)}')


def find_valid_policies_2(policies):
    valid_policies = []
    for policy in policies:
        character = policy['character']
        password = policy['password']
        position_1 = policy['position_1']
        position_2 = policy['position_2']
        if (password[position_1] == character) ^ (password[position_2] == character):
            valid_policies.append(policy)
    return valid_policies


def parse_policies_2(data):
    policies = []
    pattern = re.compile(r'(?P<position_1>\d+)-(?P<position_2>\d+)\s(?P<character>\w):\s(?P<password>.*)')
    for line in data:
        policy = {}
        matches = re.match(pattern, line)
        policy['position_1'] = int(matches.group('position_1')) - 1
        policy['position_2'] = int(matches.group('position_2')) - 1
        policy['character'] = matches.group('character')
        policy['password'] = matches.group('password')
        policies.append(policy)
    return policies


def load_data():
    with open('input') as f:
        data = f.read()
    return [l.strip() for l in data.splitlines()]


if __name__ == '__main__':
    part1()
    part2()
