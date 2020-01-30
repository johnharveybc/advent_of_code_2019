class IntCode:
    def __init__(self, input_file):
        self.current_addr = 0
        with open(input_file, 'r') as fh:
            reg_vals = list(map(int, fh.readline().split(',')))
            reg_addrs = list(range(len(reg_vals)))
            self.registers = dict(zip(reg_addrs, reg_vals))

    def set_reg_val(self, addr, val):
        self.registers[addr] = val

    def get_reg_val(self, addr):
        return self.registers[addr]

    def run_intcode(self):
        while True:
            if self.registers[self.current_addr] == 1:
                addr_1 = self.get_reg_val(self.current_addr + 1)
                addr_2 = self.get_reg_val(self.current_addr + 2)
                addr_3 = self.get_reg_val(self.current_addr + 3)
                self.set_reg_val(addr_3,
                                 self.get_reg_val(addr_1) + self.get_reg_val(addr_2)
                                 )
                self.current_addr += 4
            elif self.registers[self.current_addr] == 2:
                addr_1 = self.get_reg_val(self.current_addr + 1)
                addr_2 = self.get_reg_val(self.current_addr + 2)
                addr_3 = self.get_reg_val(self.current_addr + 3)
                self.set_reg_val(addr_3,
                                 self.get_reg_val(addr_1) * self.get_reg_val(addr_2)
                                 )
                self.current_addr += 4
            elif self.registers[self.current_addr] == 99:
                break
            else:
                # something went very wrong
                break


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

    intcode.run_intcode()

    return intcode.get_reg_val(0)


def part_2(input_file):
    for i in range(100):
        for j in range(100):
            intcode = IntCode(input_file)
            intcode.set_reg_val(1, i)
            intcode.set_reg_val(2, j)
            intcode.run_intcode()
            if intcode.get_reg_val(0) == 19690720:
                return 100*i + j


if __name__ == '__main__':
    main()
