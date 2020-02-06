from intcode.intcode import IntCode


def main():
    input_file = '../inputs/05.txt'
    intcode = IntCode(input_file, [1])
    intcode.run()
    intcode = IntCode(input_file, [5])
    intcode.run()


if __name__ == '__main__':
    main()
