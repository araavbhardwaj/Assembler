import main
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

def mov_imm(isa,reg,reg_val):
    isa.setRegValue(reg,reg_val)    
    isa.setRegValue(reg,reg_val)
    RegisterError(reg)

def add_reg(isa ,reg1, reg2, reg3):
    reg3_val = isa.getRegValue(reg3)
    reg2_val = isa.getRegValue(reg2)
    reg1_val = reg2_val + reg3_val

    if reg1_val > 65535:
        isa.setRegValue("FLAGS",1) 
        mov_imm(isa,reg1, 0)
    else:
        mov_imm(isa,reg1,reg1_val)

def sub_reg(isa,reg1, reg2, reg3):
    reg2_val = isa.getRegValue(reg2)
    reg3_val = isa.getRegValue(reg3)
    reg1_val = reg2_val - reg3_val
    
    if reg1_val < 0:
        isa.setRegValue("FLAGS",1) 
        mov_imm(isa,reg1, 0)
    else:
         mov_imm(isa,reg1,reg1_val)
def ld(isa,mem,reg1, mem_addr):
    reg1_val = mem[mem_addr]  
    mov_imm(isa,reg1, reg1_val)

def st(isa,mem,reg1, mem_addr):
    mem[mem_addr] = isa.getRegValue(reg1)  #mem is a array (pls check)

def mov_reg(isa,reg1, reg2):
    reg2_val = isa.getRegValue(reg2) 
    mov_imm(isa,reg1, reg2_val)

def mul_reg(isa,reg1, reg2, reg3):
    reg2_val = isa.getRegValue(reg2)  
    reg3_val = isa.getRegValue(reg3)  
    reg1_val = reg2_val * reg3_val
    mov_imm(isa,reg1, reg1_val)  
    if reg1_val > 65535:
        isa.setRegValue("FLAGS",1) 

def div_reg(isa,reg3, reg4):
    reg3_val = isa.getRegValue(reg3)  
    reg4_val = isa.getRegValue(reg4) 
    try:
        quotient = reg3_val // reg4_val
    except:
        print("Divsion by 0 is not possible")
        quit()
    remainder = reg3_val % reg4_val
    
    mov_imm(isa,"R0", quotient) 
    mov_imm(isa,"R1", remainder) 
    if isa.reg1_val > 65535:
        isa.setRegValue("FLAGS",1) 


def rs(isa, reg1, imm):
    reg1_val = isa.getRegValue(reg1)
    shift_amount = imm & 0x7F  #  0x7F to ensure a 7-bit value
    reg1_val >>= shift_amount
    mov_imm(isa,reg1, reg1_val)

def ls(isa,reg1, imm):
    reg1_val = isa.getRegValue(reg1)
    shift_amount = imm & 0x7F #  0x7F to ensure a 7-bit value
    reg1_val <<= shift_amount
    mov_imm(isa,reg1, reg1_val)

def xor_reg(isa,reg1, reg2, reg3):
    reg2_val = isa.getRegValue(reg2)
    reg3_val = isa.getRegValue(reg3)
    reg1_val = reg2_val ^ reg3_val
    mov_imm(isa,reg1, reg1_val)

def or_reg(isa, reg1, reg2, reg3):
    reg2_val = isa.getRegValue(reg2)
    reg3_val = isa.getRegValue(reg3)
    reg1_val = reg2_val | reg3_val
    mov_imm(isa,reg1, reg1_val)

def and_reg(isa,reg1, reg2, reg3):
    reg2_val = isa.getRegValue(reg2)
    reg3_val = isa.getRegValue(reg3)
    reg1_val = reg2_val & reg3_val
    mov_imm(isa,reg1, reg1_val)

def not_reg(isa,reg1, reg2):
    reg2_val = isa.getRegValue(reg2)
    reg1_val = ~reg2_val
    mov_imm(isa,reg1, reg1_val)




def cmp(isa,reg1, reg2):  # CHECKKKKKK THIS ONE PLS
    reg1_val = isa.getRegValue(reg1)
    reg2_val = isa.getRegValue(reg2)

    if reg1_val < reg2_val:
        isa.setRegValue("FLAGS",1) 
    elif reg1_val > reg2_val:
        isa.setRegValue("FLAGS",-1) 
    else:
        isa.setRegValue("FLAGS",0) 

def jmp(pc,mem_addr):
    pc = mem_addr  


def jlt(isa,pc ,mem_addr):
    if isa.getRegValue("FLAGS") == -1 : 
        jmp(pc, mem_addr)


def jgt(isa,pc, mem_addr):
    if isa.getRegValue("FLAGS") == 1 : 
        jmp(pc, mem_addr)

def je(isa,pc ,mem_addr):
   if isa.getRegValue("FLAGS") == 0 : 
        jmp(pc, mem_addr)
        
def InvalidCases(line,PC):
    list_reg = isa.registers.keys()
    list_ins = isa.instructions.keys()
    if line[0] not in list_ins :
        print("Invalid instruction at line",PC)
        quit()
def SupportedInstruction(type,line,PC):
    list_reg = isa.registers.keys()
    list_ins = isa.instructions.keys()
    if line[0] not in list_ins  :
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
    if lines[-1].strip()=="hlt":
        return
    
    for ins_idx in range(len(lines)):
        if ":" in lines[ins_idx] and "hlt" in lines[ins_idx]:
            return
        if lines[ins_idx] == "hlt" and ins_idx != len(lines)-1:
            print("Invalid use of hlt operation at line",ins_idx+1)
            quit()
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

def InvalidCases(line,PC):
    list_reg = isa.registers.keys()
    list_ins = isa.instructions.keys()
    if line[0] not in list_ins :
        print("Invalid instruction at line",PC)
        quit()
def SupportedInstruction(type,line,PC):
    list_reg = isa.registers.keys()
    list_ins = isa.instructions.keys()
    if line[0] not in list_ins  :
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
        if ":" in lines[ins_idx] and "hlt" in lines[ins_idx]:
            return
        if "hlt" in lines[ins_idx] and ins_idx != len(lines)-1:
            print("Invalid use of hlt operation at line",ins_idx+1)
            quit()
    if lines[-1].strip()=="hlt":
        return
    else:
        print("No halts found at the end!!!")  
        quit()

def FlagError(line):
    if line[0]!="mov" and line[-1]=="FLAGS":
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

def decimal_to_ieee(decimal):
    shifts = 0
    if decimal != 0:
        while abs(decimal) < 1:
            decimal *= 2
            shifts -= 1
        while abs(decimal) >= 2:
            decimal /= 2
            shifts += 1

    # Calculate the exponent value
    exponent = shifts + 3  # bias is 3
    # Calculate the mantissa by converting the fractional part to binary
    fractional_part = abs(decimal) - int(abs(decimal))
    mantissa = ""
    for _ in range(5):
        fractional_part *= 2
        bit = int(fractional_part)
        mantissa += str(bit)
        fractional_part -= bit

    # Convert the exponent to a 3-bit binary representation
    exponent_binary = bin(exponent)[2:].zfill(3)

    # Combine the exponent and mantissa to form the 8-bit IEEE representation
    ieee = exponent_binary + mantissa
    return ieee