def part1():
    input_data = load_data()
    passports = parse_passports(input_data)
    valid_passports = find_valid_passports(passports)
    print(f'Answer - Part 1: {len(valid_passports)}')


def find_valid_passports(passports):
    valid_passports = []
    required_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    for passport in passports:
        if all(field in passport for field in required_fields):
            valid_passports.append(passport)
    return valid_passports


def parse_passports(input_data):
    parsed = []
    for line in input_data.split('\n\n'):
        obj = {}
        for pair in line.replace('\n', ' ').strip().split():
            pair_split = pair.split(':')
            obj[pair_split[0]] = pair_split[1]
        parsed.append(obj)
    return parsed


def load_data():
    with open('input') as f:
        data = f.read()
    return data


if __name__ == '__main__':
    part1()
