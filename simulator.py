import sys
import main
import functions as fn

regis_dict = {
    "000":"R0",
    "001":"R1",
    "010":"R2",
    "011":"R3",
    "100":"R4",
    "101":"R5",
    "110":"R0",
    "111":"FLAGS"
}
def get(item):
        return item
#__________________PC related functions___________________________________

def dump_pc(pc):
        #print("{0:07b}".format(pc),end="        ")
        return "{0:07b}".format(pc)+"        "
#______________________REGISTER related functions_________________________
def read( register,registers):
        return registers[register]

def write( register, value):
        registers[register] = value
def dump_reg(isa):
        line=""
        for reg in isa.registers:
            if reg=="FLAGS":
                line+=str(isa.getRegValue(reg))+" "
            else:
                reg_val = int(isa.getRegValue(reg))
                reg_bin = '{0:016b}'.format(reg_val)
                line+=reg_bin+" "
        return line+"\n"
#________________________Mem related functions__________________________

def read_mem(address,mem):
        return mem[address]
def write_mem(address, data,mem):
        mem[address] = data
def dump_mem(mem,main_list):
    for data in mem:
        if type(data)==int:
            main_list.append('{0:016b}'.format(data)+"\n")
        else:
            main_list.append(str(data)+"\n")
#__________________________EXECUTION ENGINE_______________________________
def execute( instruction,pc, registers,isa,halted):
        opcode = instruction[:5]#opcode val
        operand = instruction#operand val
        # Perform the execution based on the opcode
        if opcode == "00000":  # add
            fn.reset_flag(isa)
            reg3_bin = operand[13:16]
            reg1_bin = operand[7:10]
            reg2_bin= operand[10:13]
            for reg_bin in regis_dict:
                if reg_bin == reg3_bin:
                    reg3 = regis_dict[reg_bin]
                if reg_bin == reg2_bin:
                    reg2 = regis_dict[reg_bin]
                if reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            fn.add_reg(isa, reg1,reg2,reg3)
        elif opcode == "00001":  # sub
            fn.reset_flag(isa)
            reg3_bin = operand[13:16]
            reg1_bin = operand[7:10]
            reg2_bin= operand[10:13]
            for reg_bin in regis_dict:
                if reg_bin == reg3_bin:
                    reg3 = regis_dict[reg_bin]
                if reg_bin == reg2_bin:
                    reg2 = regis_dict[reg_bin]
                if reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            fn.sub_reg(isa, reg1, reg2, reg3)
        elif opcode == "00010":  # mov
            fn.reset_flag(isa)
            reg1_bin = operand[6:9]
            imm_value = int(operand[9:16],2)
            for reg_bin in regis_dict:
                if reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            fn.mov_imm(isa, reg1, imm_value)
        elif opcode == "00011":  # movreg
            reg1_bin = operand[10:13]
            reg2_bin = operand[13:16]
            for reg_bin in regis_dict:
                if reg_bin == reg2_bin:
                    reg2 = regis_dict[reg_bin]
                if reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            fn.mov_reg(isa, reg1, reg2)
            fn.reset_flag(isa)
        elif opcode == "00100":  # ld
            fn.reset_flag(isa)
            reg1_bin = operand[6:9]
            for reg_bin in regis_dict:
                if reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            reg2 = int(operand[9:16],2)    
            fn.ld(isa,mem, reg1, reg2)
        elif opcode == "00101":  # st
            fn.reset_flag(isa)
            reg1_bin = operand[6:9]
            for reg_bin in regis_dict:
                if reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            reg2 = int(operand[9:16],2)    
            fn.st(isa,mem, reg1, reg2)
        elif opcode == "00110":  # mul
            fn.reset_flag(isa)
            reg3_bin = operand[13:16]
            reg1_bin = operand[7:10]
            reg2_bin= operand[10:13]
            for reg_bin in regis_dict:
                if reg_bin == reg3_bin:
                    reg3 = regis_dict[reg_bin]
                if reg_bin == reg2_bin:
                    reg2 = regis_dict[reg_bin]
                if reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            fn.mul_reg(isa, reg1, reg2, reg3)
        elif opcode == "00111":  # div
            fn.reset_flag(isa)
            reg1_bin = operand[10:13]
            reg2_bin = operand[13:16]
            for reg_bin in regis_dict:
                if reg_bin == reg2_bin:
                    reg2 = regis_dict[reg_bin]
                if reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            fn.div_reg(isa, reg1, reg2)
        elif opcode == "01000":  # rs
            fn.reset_flag(isa)
            reg1_bin = operand[6:9]
            imm_value = int(operand[9:16],2)
            for reg_bin in regis_dict:
                if reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            fn.right_shift(isa,reg1, imm_value)
        elif opcode == "01001":  # ls
            fn.reset_flag(isa)
            reg1_bin = operand[6:9]
            imm_value = int(operand[9:16],2)
            for reg_bin in regis_dict:
                if reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            fn.left_shift(isa, reg1, imm_value)
        elif opcode == "01010":  # xor
            fn.reset_flag(isa)
            reg3_bin = operand[13:16]
            reg1_bin = operand[7:10]
            reg2_bin= operand[10:13]
            for reg_bin in regis_dict:
                if reg_bin == reg3_bin:
                    reg3 = regis_dict[reg_bin]
                if reg_bin == reg2_bin:
                    reg2 = regis_dict[reg_bin]
                if reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            fn.xor_reg(isa, reg1, reg2, reg3)
        elif opcode == "01011":  # or
            fn.reset_flag(isa)
            reg3_bin = operand[13:16]
            reg1_bin = operand[7:10]
            reg2_bin= operand[10:13]
            for reg_bin in regis_dict:
                if reg_bin == reg3_bin:
                    reg3 = regis_dict[reg_bin]
                if reg_bin == reg2_bin:
                    reg2 = regis_dict[reg_bin]
                if reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            fn.or_reg(isa, reg1, reg2, reg3)
        elif opcode == "01100":  # and
            fn.reset_flag(isa)
            reg3_bin = operand[13:16]
            reg1_bin = operand[7:10]
            reg2_bin= operand[10:13]
            for reg_bin in regis_dict:
                if reg_bin == reg3_bin:
                    reg3 = regis_dict[reg_bin]
                if reg_bin == reg2_bin:
                    reg2 = regis_dict[reg_bin]
                if reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            reg1, reg2, reg3 =isa.parse_operands(operand)
            fn.and_reg(isa, reg1, reg2, reg3)
        elif opcode == "01101":  # not
            fn.reset_flag(isa)
            reg1_bin = operand[10:13]
            reg2_bin = operand[13:16]
            for reg_bin in regis_dict:
                if reg_bin == reg2_bin:
                    reg2 = regis_dict[reg_bin]
                if reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            fn.not_reg(isa, reg1, reg2)
        elif opcode == "01110":  # cmp
            fn.reset_flag(isa)
            reg1_bin = operand[10:13]
            reg2_bin = operand[13:16]
            for reg_bin in regis_dict:
                if reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
                if reg_bin == reg2_bin:
                    reg2 = regis_dict[reg_bin]
            fn.cmp(isa, reg1, reg2)
        elif opcode == "01111":  # jmp
            fn.reset_flag(isa)
            label_address = int(operand [9:16],2)
            fn.jmp(isa,pc, mem.index(instruction))
        elif opcode == "11100":  # jlt
            label_address = int(operand [9:16],2)
            fn.jlt(isa,pc, mem.index(operand))
            fn.reset_flag(isa)
        elif opcode == "11101":  # jgt
            label_address = int(operand [9:16],2)
            fn.jgt(isa,pc, mem.index(operand))
            fn.reset_flag(isa)
        elif opcode == "11111":  # je
            label_address = int(operand [9:16],2)
            fn.je(isa,pc, mem.index(operand))
            fn.reset_flag(isa)
        elif opcode == "11010":  # hlt
            fn.reset_flag(isa)
            halted = True
        else:
            print("Invalid opcode")
        # Update the program counter
        pc = pc + 1
        return halted,pc
#main loop starts here
#program is the nested list after run this

program = []
for kx in sys.stdin:
    program.append(kx.strip())

# with open("test") as file:
#     program = []
#     for kx in file:
#         program.append(kx.strip())

mem = ["0"*16]*128 # main memory mem_addr is the mem index
pc = 0 #program counter
isa = main.ISA()
#registers = {"R0": 0,"R1": 0,"R2": 0,"R3": 0,"R4": 0,"R5": 0,"R6": 0,"FLAGS": 0}# register memory
for address, instruction in enumerate(program):
    write_mem(address, instruction,mem)
halted =False
main_list =[]
line =""
while not halted:
    instruction = read_mem(get(pc),mem)
    halted,pc = execute(instruction,pc,isa.registers,isa,halted)
    
    main_list.append(dump_pc(pc-1)+dump_reg(isa))
dump_mem(mem,main_list)

for kx in main_list:
    sys.stdout.write(kx)
# print(len(main_list))
# for i in main_list:
#     print(i)
