from enum import IntEnum, auto


class OpeCode(IntEnum):
    MOV = 0
    ADD = auto()
    SUB = auto()
    AND = auto()
    OR = auto()
    SL = auto()
    SR = auto()
    SRA = auto()
    LDL = auto()
    LDH = auto()
    CMP = auto()
    JE = auto()
    JMP = auto()
    LD = auto()
    ST = auto()
    HLT = auto()


class Register(IntEnum):
    R0 = 0
    R1 = auto()
    R2 = auto()
    R3 = auto()
    R4 = auto()
    R5 = auto()
    R6 = auto()
    R7 = auto()