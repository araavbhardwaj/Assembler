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
            reg_val = int(isa.getRegValue(reg))
            reg_bin = '{0:016b}'.format(reg_val)
            line+=reg_bin+" "
        return line
#________________________Mem related functions__________________________

def read_mem(address,mem):
        return mem[address]
def write_mem(address, data,mem):
        mem[address] = data
def dump_mem(mem,main_list):
    for data in mem[:pc]:
        main_list.append(data)
    for data in mem[pc+1:]:
        main_list.append('{0:016b}'.format(int(data)))
    return main_list
#__________________________EXECUTION ENGINE_______________________________
def execute( instruction,pc, registers,isa,halted):
        opcode = instruction[:5]#opcode val
        operand = instruction#operand val
        # Perform the execution based on the opcode
        if opcode == "00000":  # add
            reg3_bin = operand[13:16]
            reg1_bin = operand[7:10]
            reg2_bin= operand[10:13]
            for reg_bin in regis_dict:
                if reg_bin == reg3_bin:
                    reg3 = regis_dict[reg_bin]
                elif reg_bin == reg2_bin:
                    reg2 = regis_dict[reg_bin]
                elif reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            fn.add_reg(isa, reg1,reg2,reg3)
        elif opcode == "00001":  # sub
            reg3_bin = operand[13:16]
            reg1_bin = operand[7:10]
            reg2_bin= operand[10:13]
            for reg_bin in regis_dict:
                if reg_bin == reg3_bin:
                    reg3 = regis_dict[reg_bin]
                elif reg_bin == reg2_bin:
                    reg2 = regis_dict[reg_bin]
                elif reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            fn.sub_reg(isa, reg1, reg2, reg3)
        elif opcode == "00010":  # mov
            reg1 = operand[6:9]
            imm_value = int(operand[9:16],2)
            for reg_bin in regis_dict:
                if reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            fn.mov_imm(isa, reg1, imm_value)
        elif opcode == "00011":  # movreg
            reg1 = operand[10:13]
            reg2 = operand[13:16]
            for reg_bin in regis_dict:
                if reg_bin == reg2_bin:
                    reg2 = regis_dict[reg_bin]
                elif reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            fn.mov_reg(isa, reg1, reg2)
        elif opcode == "00100":  # ld
            reg1_bin = operand[6:9]
            for reg_bin in regis_dict:
                if reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            reg2 = int(operand[9:16],2)    
            fn.ld(isa,mem, reg1, reg2)
        elif opcode == "00101":  # st
            reg1_bin = operand[6:9]
            for reg_bin in regis_dict:
                if reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            reg2 = int(operand[9:16],2)    
            fn.st(isa,mem, reg1, reg2)
        elif opcode == "00110":  # mul
            reg3_bin = operand[13:16]
            reg1_bin = operand[7:10]
            reg2_bin= operand[10:13]
            for reg_bin in regis_dict:
                if reg_bin == reg3_bin:
                    reg3 = regis_dict[reg_bin]
                elif reg_bin == reg2_bin:
                    reg2 = regis_dict[reg_bin]
                elif reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            fn.mul_reg(isa, reg1, reg2, reg3)
        elif opcode == "00111":  # div
            reg1 = operand[10:13]
            reg2 = operand[13:16]
            for reg_bin in regis_dict:
                if reg_bin == reg2_bin:
                    reg2 = regis_dict[reg_bin]
                elif reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            fn.div_reg(isa, reg1, reg2)
        elif opcode == "01000":  # rs
            reg1 = operand[6:9]
            imm_value = int(operand[9:16],2)
            for reg_bin in regis_dict:
                if reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            fn.right_shift(isa,reg1, imm_value)
        elif opcode == "01001":  # ls
            reg1 = operand[6:9]
            imm_value = int(operand[9:16],2)
            for reg_bin in regis_dict:
                if reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            fn.left_shift(isa, reg1, imm_value)
        elif opcode == "01010":  # xor
            reg3_bin = operand[13:16]
            reg1_bin = operand[7:10]
            reg2_bin= operand[10:13]
            for reg_bin in regis_dict:
                if reg_bin == reg3_bin:
                    reg3 = regis_dict[reg_bin]
                elif reg_bin == reg2_bin:
                    reg2 = regis_dict[reg_bin]
                elif reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            fn.xor_reg(isa, reg1, reg2, reg3)
        elif opcode == "01011":  # or
            reg3_bin = operand[13:16]
            reg1_bin = operand[7:10]
            reg2_bin= operand[10:13]
            for reg_bin in regis_dict:
                if reg_bin == reg3_bin:
                    reg3 = regis_dict[reg_bin]
                elif reg_bin == reg2_bin:
                    reg2 = regis_dict[reg_bin]
                elif reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            fn.or_reg(isa, reg1, reg2, reg3)
        elif opcode == "01100":  # and
            reg3_bin = operand[13:16]
            reg1_bin = operand[7:10]
            reg2_bin= operand[10:13]
            for reg_bin in regis_dict:
                if reg_bin == reg3_bin:
                    reg3 = regis_dict[reg_bin]
                elif reg_bin == reg2_bin:
                    reg2 = regis_dict[reg_bin]
                elif reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            reg1, reg2, reg3 =isa.parse_operands(operand)
            fn.and_reg(isa, reg1, reg2, reg3)
        elif opcode == "01101":  # not
            reg1 = operand[10:13]
            reg2 = operand[13:16]
            for reg_bin in regis_dict:
                if reg_bin == reg2_bin:
                    reg2 = regis_dict[reg_bin]
                elif reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            fn.not_reg(isa, reg1, reg2)
        elif opcode == "01110":  # cmp
            reg1 = operand[10:13]
            reg2 = operand[13:16]
            for reg_bin in regis_dict:
                if reg_bin == reg2_bin:
                    reg2 = regis_dict[reg_bin]
                elif reg_bin == reg1_bin:
                    reg1 = regis_dict[reg_bin]
            fn.cmp(isa, reg1, reg2)
        elif opcode == "01111":  # jmp
            label_address = operand [9:16]
            fn.jump(isa,pc, mem.index(label_address))
        elif opcode == "11100":  # jlt
            label_address = operand [9:16]
            fn.jump_lt(isa,pc, mem.index(label_address))
        elif opcode == "11101":  # jgt
            label_address = operand [9:16]
            fn.jump_gt(isa,pc, mem.index(label_address))
        elif opcode == "11111":  # je
            label_address = operand [9:16]
            fn.jump_eq(isa,pc, mem.index(label_address))
        elif opcode == "11010":  # hlt
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
    program.append(kx)
mem = [0]*256 # main memory mem_addr is the mem index
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
    main_list.append(dump_pc(pc)+dump_reg(isa))
main_list = dump_mem(mem,main_list)

for kx in main_list:
    sys.stdout.write(kx)

