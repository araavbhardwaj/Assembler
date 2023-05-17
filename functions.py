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

