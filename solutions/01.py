import math


def main():
    input_file = '../inputs/01.txt'

    with open(input_file, 'r') as fh:
        part_1 = 0

        for line in fh:
            part_1 += fuel_required(line)

    print(f"The solution to part 1 is {part_1}.")


def fuel_required(fuel):
    return int(math.floor(float(fuel) / 3 - 2))


if __name__ == '__main__':
    main()
