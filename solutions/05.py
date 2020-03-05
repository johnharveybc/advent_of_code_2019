from intcode.intcode import IntCode


def main():
    input_file = '../inputs/05.txt'

    with open(input_file, 'r') as fh:
        registers = list(map(int, fh.readline().split(',')))

    intcode = IntCode(registers, [1])
    while True:
        output = intcode.run()
        if output != 0:
            part_1 = output
            break
    intcode = IntCode(registers, [5])
    part_2 = intcode.run()
    print(f"The solution to part 1 is {part_1}.")
    print(f"The solution to part 2 is {part_2}.")


if __name__ == '__main__':
    main()
