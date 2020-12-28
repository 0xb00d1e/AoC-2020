def part1():
    input_data = load_data()
    boot_code = parse_instructions(input_data)
    return_status, return_value = emulate(boot_code)
    if return_status == 1:
        print(f'Answer - Part1: {return_value}')


def part2():
    input_data = load_data()
    boot_code = parse_instructions(input_data)

    for instruction_pointer, line in enumerate(boot_code):
        copy_of_boot_code = boot_code.copy()
        instruction, argument = copy_of_boot_code[instruction_pointer]

        if instruction == 'jmp':
            copy_of_boot_code[instruction_pointer] = ('nop', 0)
        elif instruction == 'nop':
            copy_of_boot_code[instruction_pointer] = ('jmp', argument)

        return_status, return_value = emulate(copy_of_boot_code)
        if return_status == 0:
            print(f'Answer - Part2: {return_value}')
            break


def emulate(boot_code):
    already_emulated = []
    instruction_pointer = 0
    accumulator = 0

    while True:
        try:
            instruction, argument = boot_code[instruction_pointer]

            if instruction_pointer in already_emulated:
                return (1, accumulator)

            if instruction == 'acc':
                accumulator += argument
                already_emulated.append(instruction_pointer)
                instruction_pointer += 1
            elif instruction == 'nop':
                already_emulated.append(instruction_pointer)
                instruction_pointer += 1
            elif instruction == 'jmp':
                already_emulated.append(instruction_pointer)
                instruction_pointer += argument
            else:
                return(-1, accumulator)
        except IndexError:
            if instruction_pointer == len(boot_code):
                return(0, accumulator)
            return(-2, accumulator)


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
    part2()
