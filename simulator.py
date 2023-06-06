#import runthis
import sys
import main
import functions as fn
'''
memory = main.Memory()
program_counter = main.ProgramCounter()
fn = main.ExecutionEngine()
#here the program variable is a nested list of the output as a binary
#dk if binary is the right variable for it
program = ["0000000000001010",
"0000000001101010",
"0000000010011100",
"1101000000000000"]
print("a")
mem = [0]*256
pc = 0 
isa = main.ISA()
print(list(enumerate(program)))
for address, instruction in enumerate(program):
    memory.write(address, instruction,mem)
    print("b")
register_file = main.RegisterFile()
print("c")
halted = False
print("d")
while not halted:
    print("e")
    instruction = memory.read(program_counter.get(pc),mem)
    
    halted, new_pc = fn.execute(instruction, program_counter, register_file,isa)
    program_counter.dump(pc)
    register_file.dump()
    program_counter.update(new_pc,pc)
memory.dump(mem)
print("g")
'''

def get(item):
        return item
#__________________PC related functions___________________________________
def update_pc( new_pc,pc):
        pc = new_pc
def dump_pc(pc):
        print(f"pc:07b",end=' ')
#______________________REGISTER related functions_________________________
def read( register,registers):
        return registers[register]

def write( register, value):
        registers[register] = value
def dump_reg():
        for value in self.registers:
            print(f"value:016b",end=" ")
        print()
#________________________Mem related functions__________________________

def read_mem( address,mem):
        return mem[address]
def write_mem(address, data,mem):
        mem[address] = data
def dump_mem(mem):
        for data in mem:
            print(f"data:016b")#printing the mem dump as 16 bit binary rep
#__________________________EXECUTION ENGINE_______________________________
def execute( instruction,pc, registers,isa):
        opcode = instruction[:5]#opcode val
        operand = instruction#operand val
        # Perform the execution based on the opcode
        if opcode == "00000":  # add
            reg3 = operand[13:16]
            reg1 = operand[7:10]
            reg2= operand[10:13]
            isa.add_reg( reg1,reg2,reg3)
        elif opcode == "00001":  # sub
            reg3 = operand[13:16]
            reg1 = operand[7:10]
            reg2= operand[10:13]
            isa.sub_reg( reg1, reg2, reg3)
        elif opcode == "00010":  # mov
            reg1 = operand[6:9]
            imm_value = operand[9:16]
            isa.mov_imm( reg1, imm_value)
        elif opcode == "00011":  # movreg
            reg1 = operand[10:13]
            reg2 = operand[13:16]
            isa.mov_reg( reg1, reg2)
        elif opcode == "00100":  # ld
            reg1 = operand[6:9]
            reg2 = operand[9:16]    
            isa.ld(mem, reg1, reg2)
        elif opcode == "00101":  # st
            reg1 = operand[6:9]
            reg2 = operand[9:16]
            isa.st(mem, reg1, reg2)
        elif opcode == "00110":  # mul
            reg3 = operand[13:16]
            reg1 = operand[7:10]
            reg2= operand[10:13]
            isa.mul_reg( reg1, reg2, reg3)
        elif opcode == "00111":  # div
            reg1 = operand[10:13]
            reg2 = operand[13:16]
            isa.div_reg( reg1, reg2)
        elif opcode == "01000":  # rs
            reg1 = operand[6:9]
            imm_value = operand[9:16]
            isa.right_shift(reg1, imm_value)
        elif opcode == "01001":  # ls
            reg1 = operand[6:9]
            imm_value = operand[9:16]
            isa.left_shift( reg1, imm_value)
        elif opcode == "01010":  # xor
            reg3 = operand[13:16]
            reg1 = operand[7:10]
            reg2= operand[10:13]
            isa.xor_reg( reg1, reg2, reg3)
        elif opcode == "01011":  # or
            reg3 = operand[13:16]
            reg1 = operand[7:10]
            reg2= operand[10:13]
            isa.or_reg( reg1, reg2, reg3)
        elif opcode == "01100":  # and
            reg3 = operand[13:16]
            reg1 = operand[7:10]
            reg2= operand[10:13]
            reg1, reg2, reg3 =isa.parse_operands(operand)
            isa.and_reg( reg1, reg2, reg3)
        elif opcode == "01101":  # not
            reg1 = operand[10:13]
            reg2 = operand[13:16]
            isa.not_reg( reg1, reg2)
        elif opcode == "01110":  # cmp
            reg1 = operand[10:13]
            reg2 = operand[13:16]
            isa.cmp( reg1, reg2)
        elif opcode == "01111":  # jmp
            label_address = operand [9:16]
            isa.jump(pc, mem.index(label_address))
        elif opcode == "11100":  # jlt
            label_address = operand [9:16]
            isa.jump_lt(pc, mem.index(label_address))
        elif opcode == "11101":  # jgt
            label_address = operand [9:16]
            isa.jump_gt(self.register_file, self.program_counter, label_address)
        elif opcode == "11111":  # je
            label_address = operand [9:16]
            isa.jump_eq(self.register_file, self.program_counter, label_address)
        elif opcode == "11010":  # hlt
            self.halted = True
        else:
            print("Invalid opcode")

        # Update the program counter
        new_pc = self.program_counter.get() + 1
        self.program_counter.update(new_pc)

        return self.halted,new_pc
#main loop starts here
#program is the nested list after run this
program = ["0000000000001010",
"0000000001101010",
"0000000010011100",
"1101000000000000"]
mem = [0]*256 # main memory
pc = 0 #program counter
isa = main.ISA()
#registers = {"R0": 0,"R1": 0,"R2": 0,"R3": 0,"R4": 0,"R5": 0,"R6": 0,"FLAGS": 0}# register memory
for address, instruction in enumerate(program):
    write_mem(address, instruction,mem)
halted =False
while not halted:
    instruction = read_mem(get(pc))
    halted,pc = execute(instruction,pc,isa.registers,isa)
    dump_pc(pc)
    register_file.dump()
    program_counter.update(new_pc,pc)
memory.dump(mem)
print("g")
