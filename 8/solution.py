def part1():
    input_data = load_data()
    boot_code = parse_instructions(input_data)
    answer = execute_till_loop(boot_code)
    print(f'Answer - Part1: {answer}')


def execute_till_loop(boot_code):
    already_executed = []
    instruction_pointer = 0
    accumulator = 0

    while True:
        instruction = boot_code[instruction_pointer][0]
        argument = boot_code[instruction_pointer][1]
        
        if instruction_pointer in already_executed:
            return accumulator

        if instruction == 'acc':
            accumulator += argument
            already_executed.append(instruction_pointer)
            instruction_pointer += 1
        elif instruction == 'nop':
            already_executed.append(instruction_pointer)
            instruction_pointer += 1
        elif instruction == 'jmp':
            already_executed.append(instruction_pointer)
            instruction_pointer += argument
        else:
            print(f'Unrecognized instruction at line {instruction_pointer}')
            break


def parse_instructions(input_data):
    boot_code = []
    for line in input_data:
        line_split = line.split(' ')
        boot_code.append((line_split[0], int(line_split[1])))
    return boot_code


def load_data():
    with open('input') as f:
        data = f.read()
    return [l.strip() for l in data.splitlines()]


if __name__ == '__main__':
    part1()
