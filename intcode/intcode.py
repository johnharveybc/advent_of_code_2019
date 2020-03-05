class IntCode:
    def __init__(self, registers, inputs=None):
        self._addr = 0
        self._input_addr = 0
        self._run = True

        if inputs is None:
            self._inputs = []
        else:
            self._inputs = inputs

        register_addresses = list(range(len(registers)))
        self._registers = dict(zip(register_addresses, registers))

    def run(self):
        self._run = True

        while self._run:
            opcode = self._get_opcode()
            modes = self._get_modes()

            if opcode == 1:
                self._add(modes)
            elif opcode == 2:
                self._mul(modes)
            elif opcode == 3:
                self._inp(modes)
            elif opcode == 4:
                output = self._out(modes)
                return output
            elif opcode == 5:
                self._jeq(modes)
            elif opcode == 6:
                self._jnq(modes)
            elif opcode == 7:
                self._slt(modes)
            elif opcode == 8:
                self._seq(modes)
            elif opcode == 99:
                break
            else:
                # something has gone badly wrong
                break

    def set_reg_val(self, addr, val):
        self._registers[addr] = val

    def get_reg_val(self, addr):
        return self._registers[addr]

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
        self._addr += 2
        self._run = False
        return output

    def _jeq(self, modes):
        param_1 = self._get_param(self._addr + 1, modes[0])
        param_2 = self._get_param(self._addr + 2, modes[1])
        if param_1:
            self._addr = param_2
        else:
            self._addr += 3

    def _jnq(self, modes):
        param_1 = self._get_param(self._addr + 1, modes[0])
        param_2 = self._get_param(self._addr + 2, modes[1])
        if param_1 == 0:
            self._addr = param_2
        else:
            self._addr += 3

    def _slt(self, modes):
        param_1 = self._get_param(self._addr + 1, modes[0])
        param_2 = self._get_param(self._addr + 2, modes[1])
        write_addr = self._get_write_addr(self._addr + 3)
        if param_1 < param_2:
            self.set_reg_val(write_addr, 1)
        else:
            self.set_reg_val(write_addr, 0)
        self._addr += 4

    def _seq(self, modes):
        param_1 = self._get_param(self._addr + 1, modes[0])
        param_2 = self._get_param(self._addr + 2, modes[1])
        write_addr = self._get_write_addr(self._addr + 3)
        if param_1 == param_2:
            self.set_reg_val(write_addr, 1)
        else:
            self.set_reg_val(write_addr, 0)
        self._addr += 4

    def _get_param(self, addr, mode):
        if mode == 1:
            return self._registers[addr]
        elif mode == 0:
            addr = self._registers[addr]
            return self._registers[addr]

    def _get_write_addr(self, addr):
        return self._registers[addr]
