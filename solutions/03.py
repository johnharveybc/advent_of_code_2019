DIRECTIONS = {'U': (0, 1),
              'R': (1, 0),
              'D': (0, -1),
              'L': (-1, 0),
              }


def main():
    input_file = '../inputs/03.txt'
    wires = []
    with open(input_file, 'r') as fh:
        for line in fh:
            wire = wire_from_steps(line.split(','))
            wires.append(wire)

    intersections = set.intersection(*map(set, wires))

    sol_1 = min([sum(map(abs, intersection)) for intersection in intersections])

    print(f"The solution to part 1 is {sol_1}.")


def wire_from_steps(steps):
    position = (0, 0)
    wire = []
    for step in steps:
        distance = int(step[1:])
        direction = DIRECTIONS.get(step[0])
        for _ in range(distance):
            position = tuple(map(sum, zip(position, direction)))
            wire.append(position)
    return wire

if __name__ == '__main__':
    main()
