from const import OpeCode, Register


class CPU:
    def __init__(self):
        self.pc = 0
        self.ir = None
        self.flag = None
        self.reg = [0 for i in range(8)]
        self.ram = [0 for i in range(256)]
        self.program = []

    
    def __load_program(self, program):
        self.program = program

    
    def execute(self, program):
        self.__load_program(program)

        while True:
            self.ir = self.program[self.pc]
            self.pc += 1

            ope = self.__get_ope()

            if ope == OpeCode.MOV:
                reg1 = self.__get_first_reg()
                reg2 = self.__get_second_reg()
                self.reg[reg1] = self.reg[reg2]
                self.reg[reg1] = self.__in_16bit(self.reg[reg1])
            elif ope == OpeCode.ADD:
                reg1 = self.__get_first_reg()
                reg2 = self.__get_second_reg()
                self.reg[reg1] += self.reg[reg2]
                self.reg[reg1] = self.__in_16bit(self.reg[reg1])
            elif ope == OpeCode.SUB:
                reg1 = self.__get_first_reg()
                reg2 = self.__get_second_reg()
                self.reg[reg1] -= self.reg[reg2]
                self.reg[reg1] = self.__in_16bit(self.reg[reg1])
            elif ope == OpeCode.AND:
                reg1 = self.__get_first_reg()
                reg2 = self.__get_second_reg()
                self.reg[reg1] &= self.reg[reg2]
            elif ope == OpeCode.OR:
                reg1 = self.__get_first_reg()
                reg2 = self.__get_second_reg()
                self.reg[reg1] |= self.reg[reg2]
            elif ope == OpeCode.SL:
                reg = self.__get_first_reg()
                self.reg[reg] <<= 1
                self.reg[reg] = self.__in_16bit(self.reg[reg])
            elif ope == OpeCode.SR:
                reg = self.__get_first_reg()
                self.reg[reg] >>= 1
            elif ope == OpeCode.SRA:
                reg = self.__get_first_reg()
                self.reg[reg] = (self.reg[reg] & 0b1000000000000000) | (self.reg[reg] >> 1)
            elif ope == OpeCode.LDL:
                reg = self.__get_first_reg()
                value = self.__get_value()
                self.reg[reg] &= 0b1111111100000000
                self.reg[reg] |= value
            elif ope == OpeCode.LDH:
                reg = self.__get_first_reg()
                value = self.__get_value()
                self.reg[reg] &= 0b11111111
                self.reg[reg] |= (value << 8)
            elif ope == OpeCode.CMP:
                reg1 = self.__get_first_reg()
                reg2 = self.__get_second_reg()
                self.flag = int(self.reg[reg1] == self.reg[reg2])
            elif ope == OpeCode.JE:
                addr = self.__get_value()
                self.pc = addr if self.flag == 1 else self.pc
            elif ope == OpeCode.JMP:
                addr = self.__get_value()
                self.pc = addr
            elif ope == OpeCode.LD:
                reg = self.__get_first_reg()
                addr = self.__get_value()
                self.reg[reg] = self.ram[addr]
            elif ope == OpeCode.ST:
                reg = self.__get_first_reg()
                addr = self.__get_value()
                self.ram[addr] = self.reg[reg]
            elif ope == OpeCode.HLT:
                break

        print("result: %d" % self.ram[64])


    # get factor from mnemonic
    def __get_ope(self):
        return self.ir >> 11


    def __get_first_reg(self):
        return (self.ir >> 8) & 0b111


    def __get_second_reg(self):
        return (self.ir >> 5) & 0b111


    def __get_value(self):
        return self.ir & 0b11111111


    def __in_16bit(self, value):
        return value & 0b1111111111111111