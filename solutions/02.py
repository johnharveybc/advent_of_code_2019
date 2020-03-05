from intcode.intcode import IntCode


def main():
    input_file = '../inputs/02.txt'

    sol_1 = part_1(input_file)

    print(f"The solution to part 1 is {sol_1}.")

    sol_2 = part_2(input_file)

    print(f"The solution to part 2 is {sol_2}.")


def part_1(input_file):
    with open(input_file, 'r') as fh:
        registers = list(map(int, fh.readline().split(',')))

    registers[1] = 12
    registers[2] = 2

    intcode = IntCode(registers)

    intcode.run()

    return intcode.get_reg_val(0)


def part_2(input_file):
    with open(input_file, 'r') as fh:
        registers = list(map(int, fh.readline().split(',')))

    for i in range(100):
        registers[1] = i
        for j in range(100):
            registers[2] = j
            intcode = IntCode(registers)
            intcode.run()
            if intcode.get_reg_val(0) == 19690720:
                return 100*i + j


if __name__ == '__main__':
    main()
