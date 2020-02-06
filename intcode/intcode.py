class IntCode:
    def __init__(self, input_file):
        self._addr = 0
        with open(input_file, 'r') as fh:
            reg_vals = list(map(int, fh.readline().split(',')))
            reg_addrs = list(range(len(reg_vals)))
            self.regs = dict(zip(reg_addrs, reg_vals))

    def run(self):
        while True:
            opcode = self._get_opcode()
            if opcode == 1:
                self._add()
            elif opcode == 2:
                self._mul()
            elif opcode == 99:
                break
            else:
                # something has gone badly wrong
                break

    def set_reg_val(self, addr, val):
        self.regs[addr] = val

    def get_reg_val(self, addr):
        return self.regs[addr]

    def _get_opcode(self):
        return self.get_reg_val(self._addr)

    def _add(self):
        param_1 = self._get_param(self._addr + 1)
        param_2 = self._get_param(self._addr + 2)
        write_addr = self._get_write_addr(self._addr + 3)
        self.set_reg_val(write_addr, param_1 + param_2)
        self._addr += 4

    def _mul(self):
        param_1 = self._get_param(self._addr + 1)
        param_2 = self._get_param(self._addr + 2)
        write_addr = self._get_write_addr(self._addr + 3)
        self.set_reg_val(write_addr, param_1 * param_2)
        self._addr += 4

    def _get_param(self, addr):
        addr = self.regs[addr]
        return self.regs[addr]

    def _get_write_addr(self, addr):
        return self.regs[addr]
