
class ISA:
    def __init__(self):
        self.instructions = {
            "add": ["00000", "A"],
            "sub": ["00001", "A"],
            "mov": ["00010", "B"],
            "movreg": ["00011", "C"],
            "ld": ["00100", "D"],
            "st": ["00101", "D"],
            "mul": ["00110", "A"],
            "div": ["00111", "C"],
            "rs": ["01000", "B"],
            "ls": ["01001", "B"],
            "xor": ["01010", "A"],
            "or": ["01011", "A"],
            "and": ["01100", "A"],
            "not": ["01101", "C"],
            "cmp": ["01110", "C"],
            "jmp": ["01111", "E"],
            "jlt": ["11100", "E"],
            "jgt": ["11101", "E"],
            "je": ["11111", "E"],
            "addf": ["10000", "A"],
            "subf": ["10001", "A"],
            "movf":["10010","B"],
            "xnor":["10011","A"],
            "nand":["10101","A"],
            "nor":["10110","A"],
            "xand":["10111","A"],
            "power":["11000","A"],
            "hlt": ["11010", "F"],
            "var":["","G"],
            "label":["","H"]
        }

        self.registers = {
            "R0": ["000", 0],
            "R1": ["001", 0],
            "R2": ["010", 0],
            "R3": ["011", 0],
            "R4": ["100", 0],
            "R5": ["101", 0],
            "R6": ["110", 0],
            "FLAGS": ["111", "0"*16],
        }
    def getRegCode(self, reg):
        return self.registers[reg][0]

    def getRegValue(self, reg):
        return self.registers[reg][1]

    def isValidReg(self, reg):
        return reg in self.registers

    def setRegValue(self, reg, value):
        OPCode = self.getRegCode(reg)
        self.registers[reg] = [OPCode, value]

    def getInstructionCode(self, instruction):
        return self.instructions[instruction][0]

    def getInstructionType(self, instruction):
        return self.instructions[instruction][1]

    def isValidLabelName(self, labelName):
        return True