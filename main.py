import functions
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
            "hlt": ["11010", "F"],
            "var":["","G"],
            "label":["","H"]
        }

        self.registers = {
            "R0": ["000", None],
            "R1": ["001", None],
            "R2": ["010", None],
            "R3": ["011", None],
            "R4": ["100", None],
            "R5": ["101", None],
            "R6": ["110", None],
            "FLAGS": ["111", None],
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
    def parse_operands(instruction):
        operands = instruction.split()[1:]  # Split the instruction string and exclude the opcode
        return operands


class Memory:
    def _init_(self):
        self.memory = [0] * 256

    def read(self, address):
        return self.memory[address]

    def write(self, address, data):
        self.memory[address] = data
    def dump(self):
        for data in self.memory:
            print("{}".format(data:016b))#printing the mem dump as 16 bit binary rep


class ProgramCounter:
    def _init_(self):
        self.pc = 0

    def get(self):
        return self.pc

    def update(self, new_pc):
        self.pc = new_pc
    def dump(self):
        print("{}".format(self.pc:07b),end=' ')


class RegisterFile:
    def _init_(self):
        self.registers = {"R0": 0,"R1": 0,"R2": 0,"R3": 0,"R4": 0,"R5": 0,"R6": 0,"FLAGS": 0}

    def read(self, register):
        return self.registers[register]

    def write(self, register, value):
        self.registers[register] = value
    def dump(self):
        reg_vals = [value:016b for value in self.registers]
        print(' '.join(register_values))


class ExecutionEngine:
    def _init_(self, memory, program_counter, register_file):
        self.memory = memory
        self.program_counter = program_counter
        self.register_file = register_file
        self.halted = False
        self.isa = ISA()

    def execute(self, instruction):
        opcode = self.isa.getInstructionCode(instruction)
        operand = instruction[5:]

        # Perform the execution based on the opcode
        if opcode == "00000":  # add
            reg1, reg2, reg3 = self.isa.parse_operands(operand)
            self.isa.add_reg(self.register_file, reg1, reg2, reg3)
        elif opcode == "00001":  # sub
            reg1, reg2, reg3 = self.isa.parse_operands(operand)
            self.isa.sub_reg(self.register_file, reg1, reg2, reg3)
        elif opcode == "00010":  # mov
            reg1, imm_value = self.isa.parse_operands(operand)
            self.isa.mov_imm(self.register_file, reg1, imm_value)
        elif opcode == "00011":  # movreg
            reg1, reg2 = self.isa.parse_operands(operand)
            self.isa.mov_reg(self.register_file, reg1, reg2)
        elif opcode == "00100":  # ld
            reg1, reg2 = self.isa.parse_operands(operand)
            self.isa.ld(self.memory, self.register_file, reg1, reg2)
        elif opcode == "00101":  # st
            reg1, reg2 = self.isa.parse_operands(operand)
            self.isa.st(self.memory, self.register_file, reg1, reg2)
        elif opcode == "00110":  # mul
            reg1, reg2, reg3 = self.isa.parse_operands(operand)
            self.isa.mul_reg(self.register_file, reg1, reg2, reg3)
        elif opcode == "00111":  # div
            reg1, reg2 = self.isa.parse_operands(operand)
            self.isa.div_reg(self.register_file, reg1, reg2)
        elif opcode == "01000":  # rs
            reg1, imm_value = self.isa.parse_operands(operand)
            self.isa.right_shift(self.register_file, reg1, imm_value)
        elif opcode == "01001":  # ls
            reg1, imm_value = self.isa.parse_operands(operand)
            self.isa.left_shift(self.register_file, reg1, imm_value)
        elif opcode == "01010":  # xor
            reg1, reg2, reg3 = self.isa.parse_operands(operand)
            self.isa.xor_reg(self.register_file, reg1, reg2, reg3)
        elif opcode == "01011":  # or
            reg1, reg2, reg3 = self.isa.parse_operands(operand)
            self.isa.or_reg(self.register_file, reg1, reg2, reg3)
        elif opcode == "01100":  # and
            reg1, reg2, reg3 = self.isa.parse_operands(operand)
            self.isa.and_reg(self.register_file, reg1, reg2, reg3)
        elif opcode == "01101":  # not
            reg1, reg2 = self.isa.parse_operands(operand)
            self.isa.not_reg(self.register_file, reg1, reg2)
        elif opcode == "01110":  # cmp
            reg1, reg2 = self.isa.parse_operands(operand)
            self.isa.cmp(self.register_file, reg1, reg2)
        elif opcode == "01111":  # jmp
            label_address = self.isa.parse_label(operand)
            self.isa.jump(self.program_counter, label_address)
        elif opcode == "11100":  # jlt
            label_address = self.isa.parse_label(operand)
            self.isa.jump_lt(self.register_file, self.program_counter, label_address)
        elif opcode == "11101":  # jgt
            label_address = self.isa.parse_label(operand)
            self.isa.jump_gt(self.register_file, self.program_counter, label_address)
        elif opcode == "11111":  # je
            label_address = self.isa.parse_label(operand)
            self.isa.jump_eq(self.register_file, self.program_counter, label_address)
        elif opcode == "11010":  # hlt
            self.halted = True
        else:
            print("Invalid opcode")

        # Update the program counter
        new_pc = self.program_counter.get() + 1
        self.program_counter.update(new_pc)

        return self.halted,new_pc
