from cpu import CPU
from assembler import Assembler


if __name__ == "__main__":
    filename = "test_sum10.txt"
    text = open(filename, "r").readlines()
    for i, line in enumerate(text):
        text[i] = line.rstrip("\n")

    asm = Assembler()

    machine_codes = asm.asm(text)
    
    for code in machine_codes:
        print(f"{code:015b}")

    cpu = CPU()
    cpu.execute(machine_codes)