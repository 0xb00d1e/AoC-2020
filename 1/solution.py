def part1():
    data = set(load_data())

    for n in data:
        compliment = 2020 - n
        if compliment in data:
            print(f'Answer - part 1: {n*compliment}')
            break


def part2():
    data = set(load_data())

    for i, outer_num in enumerate(data):
        memory = set()
        current_sum = 2020 - outer_num
        for j, inner_num in enumerate(data, start=i+1):
            if (current_sum - inner_num) in memory:
                print(f'Answer - part 2: {(inner_num)*(outer_num)*(current_sum-inner_num)}')
                return
            memory.add(inner_num)



def load_data():
    with open('input') as f:
        data = f.read()
    return [int(l.strip()) for l in data.splitlines()]


if __name__ == '__main__':
    part1()
    part2()
