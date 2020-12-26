import re


def part1():
    input_data = load_data()
    passports = parse_passports(input_data)
    valid_passports = find_valid_passports_1(passports)
    print(f'Answer - Part 1: {len(valid_passports)}')


def part2():
    input_data = load_data()
    passports = parse_passports(input_data)
    valid_passports = find_valid_passports_2(passports)
    print(f'Answer - Part 2: {len(valid_passports)}')


def find_valid_passports_1(passports):
    valid_passports = []
    required_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    for passport in passports:
        if all(field in passport for field in required_fields):
            valid_passports.append(passport)
    return valid_passports


def find_valid_passports_2(passports):
    valid_passports = []
    required_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    for passport in passports:
        if not all(field in passport for field in required_fields):
            continue

        byr = int(passport['byr'])
        iyr = int(passport['iyr'])
        eyr = int(passport['eyr'])
        if not number_between(byr, 1920, 2002):
            continue
        if not number_between(iyr, 2010, 2020):
            continue
        if not number_between(eyr, 2020, 2030):
            continue

        hgt = passport['hgt']
        if hgt.endswith('cm'):
            if not number_between(int(hgt[:-2]), 150, 193):
                continue
        elif hgt.endswith('in'):
            if not number_between(int(hgt[:-2]), 59, 76):
                continue
        if not (hgt.endswith('cm') or hgt.endswith('in')):
            continue

        hcl = passport['hcl']
        if not re.match(r'#[0-9a-f]{6}$', hcl):
            continue

        if passport['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            continue

        if not re.match(r'[0-9]{9}$', passport['pid']):
            continue

        valid_passports.append(passport)
    return valid_passports


def number_between(num, x, y):
    return x <= num <= y


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
    part2()
