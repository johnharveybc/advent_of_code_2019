MIN = 353096
MAX = 843212


def main():
    sol_1 = 0
    sol_2 = 0
    for i in range(MIN, MAX + 1):
        if is_only_increasing(i) and has_adjacent_repeats(i):
            sol_1 += 1
            if has_adjacent_double(i):
                sol_2 += 1

    print(f"The solution to part 1 is {sol_1}.")
    print(f"The solution to part 2 is {sol_2}.")


def is_only_increasing(number):
    digit_list = [int(d) for d in str(number)]
    return all([digit_list[i-1] <= digit_list[i] for i in range(1, len(digit_list))])


def has_adjacent_repeats(number):
    num_string = str(number)
    return any([num_string.count(c) > 1 for c in num_string])


def has_adjacent_double(number):
    num_string = str(number)
    return any([num_string.count(c) == 2 for c in num_string])


if __name__ == '__main__':
    main()
