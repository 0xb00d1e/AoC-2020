import re
from collections import defaultdict


def part1():
    input_data = load_data()
    rules = parse_rules(input_data)
    count = 0
    for bag in rules.keys():
        if count_of_gold(bag, rules):
            count += 1
    print(f'Answer - Part 1: {count}')


def part2():
    input_data = load_data()
    rules = parse_rules(input_data)
    count = count_of_inner_bags(rules, 'shiny gold')
    print(f'Answer - Part 2: {count}')


def count_of_gold(bag, rules):
    count = 0
    inner_bags = rules[bag]
    if not inner_bags:
        return count
    for inner_bag in inner_bags:
        if inner_bag['bag_color'] == 'shiny gold':
            count += 1
        count += count_of_gold(inner_bag['bag_color'], rules)
    return count


def count_of_inner_bags(rules, bag):
    count = 0
    inner_bags = rules[bag]
    if not inner_bags:
        return count
    for inner_bag in inner_bags:
        current_count = inner_bag['count']
        count += current_count
        nested_bag_count = count_of_inner_bags(rules, inner_bag['bag_color'])
        count += (nested_bag_count * current_count)
    return count

def parse_rules(input_data):
    rules = defaultdict(list)
    for line in input_data:
        line = line.rstrip('.')
        line_split = line.split(' contain ')
        outer_bag = line_split[0].split(' bags')[0]
        inner_bags = line_split[1].split(', ')

        if inner_bags[0] == 'no other bags':
            rules[outer_bag] = []
            continue
        for inner_bag in inner_bags:
            matches = re.match(r'(?P<count>\d+)\s(?P<bag_color>.*?)\sbags?', inner_bag)
            rules[outer_bag].append(
                {
                    'count': int(matches.group('count')),
                    'bag_color': matches.group('bag_color')
                }
            )
    return rules


def load_data():
    with open('input') as f:
        input_data = f.read()
    return [l.strip() for l in input_data.splitlines()]


if __name__ == '__main__':
    part1()
    part2()
