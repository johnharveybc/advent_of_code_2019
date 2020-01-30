import math


def main():
    input_file = '../inputs/01.txt'

    with open(input_file, 'r') as fh:
        part_1 = 0
        part_2 = 0

        for line in fh:
            part_1 += fuel_required(line)
            part_2 += total_fuel_required(line)

    print(f"The solution to part 1 is {part_1}.")
    print(f"The solution to part 2 is {part_2}.")


def fuel_required(fuel):
    return int(math.floor(float(fuel) / 3 - 2))


def total_fuel_required(fuel):
    total_fuel = 0

    while True:
        fuel = fuel_required(fuel)
        if fuel > 0:
            total_fuel += fuel
        else:
            break

    return total_fuel


if __name__ == '__main__':
    main()
