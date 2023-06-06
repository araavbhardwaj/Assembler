
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
            "FLAGS": ["111", 0],
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
        operands = instruction.split()[1:]
        print(operands)  # Split the instruction string and exclude the opcode
        return operands
import functions

class Memory:
    def _init_(self):
        self.memory = [0] * 256
    def read(self, address,mem):
        return mem[address]
    def write(self, address, data,mem):
        mem[address] = data
    def dump(self,mem):
        for data in mem:
            print(f"data:016b")#printing the mem dump as 16 bit binary rep


class ProgramCounter:
    def _init_(self):
        self.pc = 0

    def get(self,pc):
        return pc

    def update(self, new_pc,pc):
        pc = new_pc
    def dump(self,pc):
        print(f"pc:07b",end=' ')


class RegisterFile:
    def _init_(self):
        self.registers = {"R0": 0,"R1": 0,"R2": 0,"R3": 0,"R4": 0,"R5": 0,"R6": 0,"FLAGS": 0}

    def read(self, register):
        return self.registers[register]

    def write(self, register, value):
        self.registers[register] = value
    def dump(self):
        for value in self.registers:
            print(f"value:016b",end=" ")
        print()


class ExecutionEngine:
    def _init_(self, memory, program_counter, register_file):
        self.memory = memory
        self.program_counter = program_counter
        self.register_file = register_file
        self.halted = False
        
'''
    def execute(self, instruction,program_counter, register_file,isa):
        opcode = instruction[:5]
        operand = instruction[5:] 

        # Perform the execution based on the opcode
        if opcode == "00000":  # add
            reg1, reg2, reg3 = isa.parse_operands(operand)
            isa.add_reg(self.register_file, reg1, reg2, reg3)
        elif opcode == "00001":  # sub
            reg1, reg2, reg3 =isa.parse_operands(operand)
            isa.sub_reg(self.register_file, reg1, reg2, reg3)
        elif opcode == "00010":  # mov
            reg1, imm_value =isa.parse_operands(operand)
            isa.mov_imm(self.register_file, reg1, imm_value)
        elif opcode == "00011":  # movreg
            reg1, reg2 = isa.parse_operands(operand)
            isa.mov_reg(self.register_file, reg1, reg2)
        elif opcode == "00100":  # ld
            reg1, reg2 =isa.parse_operands(operand)
            isa.ld(self.memory, self.register_file, reg1, reg2)
        elif opcode == "00101":  # st
            reg1, reg2 = isa.parse_operands(operand)
            isa.st(self.memory, self.register_file, reg1, reg2)
        elif opcode == "00110":  # mul
            reg1, reg2, reg3 =isa.parse_operands(operand)
            isa.mul_reg(self.register_file, reg1, reg2, reg3)
        elif opcode == "00111":  # div
            reg1, reg2 =isa.parse_operands(operand)
            isa.div_reg(self.register_file, reg1, reg2)
        elif opcode == "01000":  # rs
            reg1, imm_value = isa.parse_operands(operand)
            isa.right_shift(self.register_file, reg1, imm_value)
        elif opcode == "01001":  # ls
            reg1, imm_value = isa.parse_operands(operand)
            isa.left_shift(self.register_file, reg1, imm_value)
        elif opcode == "01010":  # xor
            reg1, reg2, reg3 = isa.parse_operands(operand)
            isa.xor_reg(self.register_file, reg1, reg2, reg3)
        elif opcode == "01011":  # or
            reg1, reg2, reg3 = isa.parse_operands(operand)
            isa.or_reg(self.register_file, reg1, reg2, reg3)
        elif opcode == "01100":  # and
            reg1, reg2, reg3 =isa.parse_operands(operand)
            isa.and_reg(self.register_file, reg1, reg2, reg3)
        elif opcode == "01101":  # not
            reg1, reg2 =isa.parse_operands(operand)
            isa.not_reg(self.register_file, reg1, reg2)
        elif opcode == "01110":  # cmp
            reg1, reg2 = isa.parse_operands(operand)
            isa.cmp(self.register_file, reg1, reg2)
        elif opcode == "01111":  # jmp
            label_address = isa.parse_label(operand)
            isa.jump(self.program_counter, label_address)
        elif opcode == "11100":  # jlt
            label_address = isa.parse_label(operand)
            isa.jump_lt(self.register_file, self.program_counter, label_address)
        elif opcode == "11101":  # jgt
            label_address =isa.parse_label(operand)
            isa.jump_gt(self.register_file, self.program_counter, label_address)
        elif opcode == "11111":  # je
            label_address = isa.parse_label(operand)
            isa.jump_eq(self.register_file, self.program_counter, label_address)
        elif opcode == "11010":  # hlt
            self.halted = True
        else:
            print("Invalid opcode")

        # Update the program counter
        new_pc = self.program_counter.get() + 1
        self.program_counter.update(new_pc)

        return self.halted,new_pc
'''