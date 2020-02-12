from const import OpeCode, Register


class Assembler:
    def __init__(self):
        pass

    def asm(self, mnemonic_str_list):
        machine_codes = []
        for mnemonic_str in mnemonic_str_list:
            m = Mnemonic(mnemonic_str)
            machine_codes.append(m.assemble())

        return machine_codes


class Mnemonic:
    def __init__(self, s):
        tmp = s.split(" ")
        
        splited_m = []
        for token in tmp:
            if token != " ":
                splited_m.append(token)

        self.ope = self.__str_to_opecode(splited_m[0])
        
        self.arg1 = self.__str_to_value(splited_m[1]) if len(splited_m) > 1 else None
        self.arg2 = self.__str_to_value(splited_m[2]) if len(splited_m) > 2 else None


    def __str_to_opecode(self, op_str):
        ope_dict = {
            "mov": OpeCode.MOV,
            "add": OpeCode.ADD,
            "sub": OpeCode.SUB,
            "and": OpeCode.AND,
            "or": OpeCode.OR,
            "sl": OpeCode.SL,
            "sr": OpeCode.SR,
            "sra": OpeCode.SRA,
            "ldl": OpeCode.LDL,
            "ldh": OpeCode.LDH,
            "cmp": OpeCode.CMP,
            "je": OpeCode.JE,
            "jmp": OpeCode.JMP,
            "ld": OpeCode.LD,
            "st": OpeCode.ST,
            "hlt": OpeCode.HLT,
        }

        if op_str in ope_dict.keys():
            return ope_dict[op_str]

        raise ValueError


    def __str_to_register(self, reg_str):
        reg_dict = {
            "Reg0": Register.R0,
            "Reg1": Register.R1,
            "Reg2": Register.R2,
            "Reg3": Register.R3,
            "Reg4": Register.R4,
            "Reg5": Register.R5,
            "Reg6": Register.R6,
            "Reg7": Register.R7,
        }

        if reg_str in reg_dict.keys():
            return reg_dict[reg_str]

        raise ValueError


    def __str_to_value(self, value_str):
        if value_str[0:3] == "Reg":
            return self.__str_to_register(value_str)

        return int(value_str)


    def assemble(self):
        two_reg_ope_list = [
            OpeCode.MOV,
            OpeCode.ADD,
            OpeCode.SUB,
            OpeCode.AND,
            OpeCode.OR,
            OpeCode.CMP
        ]

        one_reg_ope_list = [
            OpeCode.SL,
            OpeCode.SR,
            OpeCode.SRA
        ]

        reg_value_ope_list = [
            OpeCode.LDL,
            OpeCode.LDH,
            OpeCode.LD,
            OpeCode.ST
        ]

        one_value_ope_list = [
            OpeCode.JE,
            OpeCode.JMP
        ]

        no_value_ope_list = [
            OpeCode.HLT
        ]

        code = self.ope << 11

        if self.ope in two_reg_ope_list:
            code += (self.arg1 << 8)
            code += (self.arg2 << 5)
        elif self.ope in one_reg_ope_list:
            code += (self.arg1 << 8)
        elif self.ope in reg_value_ope_list:
            code += (self.arg1 << 8)
            code += self.arg2
        elif self.ope in one_value_ope_list:
            code += self.arg1
        elif self.ope in no_value_ope_list:
            pass
        else:
            raise ValueError

        return code