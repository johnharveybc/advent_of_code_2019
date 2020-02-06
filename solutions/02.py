from intcode.intcode import IntCode


def main():
    input_file = '../inputs/02.txt'

    sol_1 = part_1(input_file)

    print(f"The solution to part 1 is {sol_1}.")

    sol_2 = part_2(input_file)

    print(f"The solution to part 2 is {sol_2}.")


def part_1(input_file):
    intcode = IntCode(input_file)

    intcode.set_reg_val(1, 12)
    intcode.set_reg_val(2, 2)

    intcode.run()

    return intcode.get_reg_val(0)


def part_2(input_file):
    for i in range(100):
        for j in range(100):
            intcode = IntCode(input_file)
            intcode.set_reg_val(1, i)
            intcode.set_reg_val(2, j)
            intcode.run()
            if intcode.get_reg_val(0) == 19690720:
                return 100*i + j


if __name__ == '__main__':
    main()
