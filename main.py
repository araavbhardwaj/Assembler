class ISA:
    def __init__(self):
        self.instructions = {
            "add": ["10000", "A"],
            "sub": ["10001", "A"],
            "movi": ["10010", "B"],
            "mov": ["10011", "C"],
            "ld": ["10100", "D"],
            "st": ["10101", "D"],
            "mul": ["10110", "A"],
            "div": ["10111", "C"],
            "rs": ["11000", "B"],
            "ls": ["11001", "B"],
            "xor": ["11010", "A"],
            "or": ["11011", "A"],
            "and": ["11100", "A"],
            "not": ["11101", "C"],
            "cmp": ["11110", "C"],
            "jmp": ["11111", "E"],
            "jlt": ["01100", "E"],
            "jgt": ["01101", "E"],
            "je": ["01111", "E"],
            "hlt": ["01010", "F"],
            "addf": ["00000", "A"],
            "subf": ["00001", "A"],
            "movf": ["00010", "B"],
            "hack": ["11101", "A"],
            "delete": ["01010", "B"]
        }

        self.registers = {
            "R0": ["000", None],
            "R1": ["001", None],
            "R2": ["010", None],
            "R3": ["011", None],
            "R4": ["100", None],
            "R5": ["101", None],
            "R6": ["110", None],
            "FLAGS": ["111", None]
        }

    def getRegCode(self, reg):
        return self.registers[reg][0]

    def getRegValue(self, reg):
        return self.registers[reg][1]

    def isValidReg(self, reg):
        return reg in self.registers

    def setRegValue(self, reg, value):
        OPCode = self.getRegCode(reg)
        self.registers[reg] = [OPCode, str(value)]

    def getInstructionCode(self, instruction):
        return self.instructions[instruction][0]

    def getInstructionType(self, instruction):
        return self.instructions[instruction][1]

    def isValidLabelName(self, labelName):
        return True
