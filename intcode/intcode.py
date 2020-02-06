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
