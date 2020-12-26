import re


def part1():
    data = set(load_data())
    policies = parse_policies(data)
    valid_policies = find_valid_policies(policies)
    print(f'Answer - Part 1: {len(valid_policies)}')


def find_valid_policies(policies):
    valid_policies = []
    for policy in policies:
        character_count = policy['password'].count(policy['character'])
        if (character_count >= policy['min_occurrences']) and (character_count <= policy['max_occurrences']):
            valid_policies.append(policy)
    return valid_policies


def parse_policies(data):
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


def load_data():
    with open('input') as f:
        data = f.read()
    return [l.strip() for l in data.splitlines()]


if __name__ == '__main__':
    part1()
