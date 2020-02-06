class IntCode:
    def __init__(self, input_file, inputs=None):
        self._addr = 0
        self._input_addr = 0

        if inputs is None:
            self._inputs = []
        else:
            self._inputs = inputs

        with open(input_file, 'r') as fh:
            reg_vals = list(map(int, fh.readline().split(',')))
            reg_addrs = list(range(len(reg_vals)))
            self.regs = dict(zip(reg_addrs, reg_vals))

    def run(self):
        while True:
            opcode = self._get_opcode()
            modes = self._get_modes()

            if opcode == 1:
                self._add(modes)
            elif opcode == 2:
                self._mul(modes)
            elif opcode == 3:
                self._inp(modes)
            elif opcode == 4:
                self._out(modes)
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
        return self.get_reg_val(self._addr) % 100

    def _get_modes(self):
        opcode = self.get_reg_val(self._addr)
        return [int(d) for d in f'{opcode:05d}'[2::-1]]

    def _add(self, modes):
        param_1 = self._get_param(self._addr + 1, modes[0])
        param_2 = self._get_param(self._addr + 2, modes[1])
        write_addr = self._get_write_addr(self._addr + 3)
        self.set_reg_val(write_addr, param_1 + param_2)
        self._addr += 4

    def _mul(self, modes):
        param_1 = self._get_param(self._addr + 1, modes[0])
        param_2 = self._get_param(self._addr + 2, modes[1])
        write_addr = self._get_write_addr(self._addr + 3)
        self.set_reg_val(write_addr, param_1 * param_2)
        self._addr += 4

    def _inp(self, modes):
        param_1 = self._inputs[self._input_addr]
        write_addr = self._get_write_addr(self._addr + 1)
        self.set_reg_val(write_addr, param_1)
        self._addr += 2

    def _out(self, modes):
        output = self._get_param(self._addr + 1, modes[0])
        print(f"Outputting a value! The value is {output}!")
        self._addr += 2

    def _get_param(self, addr, mode):
        if mode == 1:
            return self.regs[addr]
        elif mode == 0:
            addr = self.regs[addr]
            return self.regs[addr]

    def _get_write_addr(self, addr):
        return self.regs[addr]
