import main
# #1 Addition 10000
# def add_with_overflow(reg1, reg2):
#     reg3 = reg1 + reg2

#     if reg3 < reg1 or reg3 < reg2:
#         overflow_flag = True
#     else:
#         overflow_flag = False

#     return reg3, overflow_flag

# #2 Subtraction 10001
# def subtract_with_overflow(reg1, reg2):
#     if reg2 > reg1:
#         reg3 = 0
#         overflow_flag = True
#     else:
#         reg3 = reg1 - reg2
#         overflow_flag = False

#     return reg3, overflow_flag

# #3  Move Immediate 10010
# def assign_imm_to_reg(reg1, imm):
  
#     imm &= 0xFF
#     reg1 = imm
#     return reg1


# #4 Move Register 10011
# def assign_reg1_to_reg2(reg1):
#     reg2 = reg1
#     return reg2

# #5  Load data from mem_addr into reg1 10100
# def load_data(mem_addr):
#     reg1 = mem_addr  
#     return reg1

# #6  Store data from reg1 to mem_addr  10101

# # // CHECK THIS ONE pls 
# def store_data(reg1, mem_addr):
#     memory[mem_addr] = reg1
#     memory = [0] * 65536  
#     reg1 = 42  
#     mem_addr = 0x1000  
#     store_data(reg1, mem_addr)

# #7 multiply_with_overflow  10110
# def multiply_with_overflow(reg1, reg2):
#     reg3 = reg1 * reg2

#     max_value = 2**31 - 1 # 32-bit signed integers
#     min_value = -2**31
#     if reg3 > max_value or reg3 < min_value:
#         overflow_flag = True
#     else:
#         overflow_flag = False

#     return reg3, overflow_flag

# #8  divide_registers 10111
# def divide_registers(reg3, reg4):
#     quotient = reg3 // reg4
#     remainder = reg3 % reg4
#     return quotient, remainder

# #9 Right Shift  11000
# def right_shift(reg1, imm):
#     imm &= 0xFF
#     reg1 >>= imm

#     return reg1


# #10 Left Shift 11001
# def left_shift(reg1, imm):
#     imm &= 0xFF
#     reg1 <<= imm
#     return reg1


# #11 Exclusive OR 11010
# def bitwise_xor(reg1, reg2):
#     reg3 = reg1 ^ reg2
#     return reg3


# #12 Or  11011
# def bitwise_or(reg1, reg2):
#     reg3 = reg1 | reg2
#     return reg3

# #12 And  11100
# def bitwise_and(reg1, reg2):
#     reg3 = reg1 & reg2
#     return reg3

# #13 Invert 11101
# def bitwise_not(reg1):
#     reg2 = ~reg1
#     return reg2

# #14 Compare 11110
# def compare_registers(reg1, reg2):
#     FLAGS = {}

#     if reg1 == reg2:
#         FLAGS['ZF'] = True 
#         FLAGS['CF'] = False  
#     elif reg1 < reg2:
#         FLAGS['ZF'] = False  
#         FLAGS['CF'] = True  
#     else:
#         FLAGS['ZF'] = False  
#         FLAGS['CF'] = False  

#     return FLAGS


# #15 Unconditional Jump  11111
# def jump_to_memory(mem_addr):
#     program_counter = mem_addr

#     return program_counter

# #16 Jump If Less Than 01100
# def jump_if_lt(mem_addr, flags):
#     if flags.get('LT'):
#         program_counter = mem_addr
#     else:
#         program_counter = None 

#     return program_counter

# #17 Jump If Greater Than 01101
# def jump_if_gt(mem_addr, flags):
#     if flags.get('GT'):
#         program_counter = mem_addr
#     else:
#         program_counter = None  

#     return program_counter
 
# #18 Jump If Equal 01111
# def jump_if_eq(mem_addr, flags):
#     if flags.get('EQ'):
#         program_counter = mem_addr
#     else:
#         program_counter = None  

#     return program_counter


# #19 Halt 01010
# ## DK THIS ONE
isa=main.ISA()
def RegisterNone(reg):
    reg_val = getRegValue(reg)
    if reg_val == None:
        return 1
    else :
        return 0

def RegisterError(reg):
    reg_val = isa.getRegValue(reg)
    if reg_val not in range (0,128):
        print("Invalid value stored in register",reg)
    else:
        return

def mov_imm(reg,reg_val):
    reg[1] = reg_val
    RegisterError(reg)

def add_reg(reg1,reg2,reg3):
    reg3_val = getRegValue(reg3)
    reg2_val = getRegValue(reg2)
    reg1_val = reg2_val + reg3_val
    mov_imm(reg1,reg1_val)

def sub_reg(reg1, reg2, reg3):
    reg2_val = getRegValue(reg2)
    reg3_val = getRegValue(reg3)
    reg1_val = reg2_val - reg3_val
    mov_imm(reg1,reg1_val)

def mov_reg(reg1, reg2):
    reg2_val = getRegValue(reg2) 
    mov_imm(reg1, reg2_val)

def mul_reg(reg1, reg2, reg3):
    reg2_val = getRegValue(reg2)  
    reg3_val = getRegValue(reg3)  
    reg1_val = reg2_val * reg3_val
    mov_imm(reg1, reg1_val)  

def div_reg(reg3, reg4):
    reg3_val = getRegValue(reg3)  
    reg4_val = getRegValue(reg4) 
    try:
        quotient = reg3_val // reg4_val
    except:
        print("Divsion by 0 is not possible")
        quit()
    remainder = reg3_val % reg4_val
    
    mov_imm("R0", quotient) 
    mov_imm("R1", remainder) 
def InvalidCases(line,PC):
    list_reg = isa.registers.keys()
    list_ins = isa.instructions.keys()
    if line[0] not in list_ins :
        print("Invalid instruction at line",PC)
        quit()
def SupportedInstruction(type,line,PC):
    list_reg = isa.registers.keys()
    list_ins = isa.instructions.keys()
    if line[0] not in list_ins :
        print("Invalid instruction at line",PC)
        quit()
    if type=="A":
        try:
            if line[1] not in list_reg or line[2] not in list_reg or line[3] not in list_reg:
                print("Invalid register number at line",PC)
                quit()
        except:
            print("General Syntax Error at line",PC)
            quit()
        # if RegisterNone(line[2]) or RegisterNone(line[3]):
        #     print("No value stored in register")
        #     quit()
         

    elif type == "B":
        if len(line)!=3:
            print("Syntax Error at line",PC)
            quit()

        elif line[2]=="FLAGS":
            pass
        else:
            try: x = int(line[2][1:])
            except : 
                print("Invalid immediate value .Not a whole number between 0 to 127 at line",PC)
                quit()
            if line[1] not in list_reg :
                print("Invalid register at line",PC)
                quit()
            elif line[2][0]!="$":
                print("Invalid symbol at line",PC)
                quit()
            elif x not in range(0,127):
                print("Invalid immediate value at line",PC)
                quit()
        

    elif type == "C":
        if len(line)!=3:
            print("Syntax Error at line",PC)
            quit()
        if line[1] not in list_reg or line[2] not in list_reg:
            print("Invalid register number at line",PC)
            quit()
        # if line[0]!="mov":
        #     if RegisterNone(line[2]) or RegisterNone(line[1]):
        #         print("No value stored in",line[2])
    
    elif type == "D":
        if len(line)!=3:
            print("Syntax Error at line",PC)
            quit()
        if line[1] not in list_reg :
            print("Invalid register number at line",PC)
            quit()
    elif type == "E":
        if len(line)!=2:
            print("Syntax Error at line",PC)
            quit()

def HaltError(lines): 
    for ins_idx in range(len(lines)):
        if lines[ins_idx] == "hlt" and ins_idx != len(lines)-1:
            print("Invalid use of hlt operation at line",ins_idx+1)
            quit()
    if lines[-1]=="hlt":
        return
    else:
        print("No halts found at the end!!!")  
        quit()

def FlagError(line):
    if line[0]!="mov" and line[-1]=="FLAG":
        print("Invalid use of FLAGS")
        quit()

def check_variable_declaration(variables,code_lines,line_ct):
    var_declared = False
    instructions_started = False
    if (variables.keys()==[]):
        pass
    else:
        for line in code_lines:
            if line.startswith('var'):
                if instructions_started:
                    print("Error: Variable declared after instructions at line",line_ct)
                    quit()
                    return

                var_declared = True
            elif not line.startswith('var') and not line.startswith(';'):
                instructions_started = True

        if not var_declared:
            print("Error: No variable declaration found.")
            quit()
def check_variables(variables,line,line_ct):
    if line[2] in variables:
        pass
    else:
        print("Variable not declared at line",line_ct)
        quit()

