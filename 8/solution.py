def part1():
    input_data = load_data()
    boot_code = parse_instructions(input_data)
    return_status, return_value = emulate(boot_code)
    if return_status == 1:
        print(f'Answer - Part1: {return_value}')


def emulate(boot_code):
    already_emulated = []
    instruction_pointer = 0
    accumulator = 0

    while True:
        try:
            instruction = boot_code[instruction_pointer][0]
            argument = boot_code[instruction_pointer][1]

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
