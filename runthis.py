import main
import functions
import sys
isa=main.ISA()
inp=[]
for kx in sys.stdin:
    inp.append(kx)
lines={}
variables={}
labels={}
line_ct=1
def tabspaces(string):
    if "\t" in string or "\n" in string or "  " in string:
        string=string.replace("\t"," ")
        string=string.replace("  "," ")
        string=string.replace("\n","")
        string=string.strip()
    return string
var_count = 0
for i in range(len(inp)):
    if inp[i][0:3] != "var":
        var_count += 1 
Error_list=[]      
PC=-1
i=0
functions.HaltError(inp)
for line in inp:
    line=tabspaces(line)
    line=tabspaces(line)
    PC+=1
    type=""
    x=line.split(" ")
    if ":" in x[0]:
        mem=str(bin(PC))[2:]
        mem=str((7-(len(str(mem))))*"0")+mem
        labels[x[0][:-1]]=mem
        x[1]=x[1].strip()
        if x[1]=="mov":
            if "R" in x[2] and ("R" in x[3] or "FLAGS" in x[3]):
                type="C"
            else:
                type="B"
        elif x[1] in isa.instructions:            
            type=isa.getInstructionType(x[1])
        line=line.strip()
        line=line[len(x[0])+1:]
        line=line.strip()
        lines[line]=type
        inp[i]=line
        i=i+1
        continue
    elif x[0]=="mov":
        if "R" in x[1] and ("R" in x[2] or "FLAGS" in x[2]):
            type="C"
        else:
            type="B"
    elif x[0] in isa.instructions:            
        type=isa.getInstructionType(x[0])
    lines[line]=type
    inp[i]=line

    if type=="G":
        PC-=1
    if type=="F":
        break
    i=i+1
binary=[]
for z in inp:
    p=z.split(" ")
    if lines[z]=="A":
        functions.SupportedInstruction("A", p, line_ct)
        functions.FlagError(p)
        opcode=isa.getInstructionCode(p[0])
        r1=isa.getRegCode(p[1])
        r2=isa.getRegCode(p[2])
        r3=isa.getRegCode(p[3])
        temp=opcode+"00"+r1+r2+r3+"\n"
        binary.append(temp)
    elif lines[z]=="B":
        functions.SupportedInstruction("B", p, line_ct)
        functions.FlagError(p)
        if p[0]=="mov":
            opcode="00010"
        else:
            opcode=isa.getInstructionCode(p[0])
        r1=isa.getRegCode(p[1])
        if p[2]=="FLAGS":
            val=isa.getRegCode(p[2])
        else:
            val=bin(int(p[2][1:]))[2:]
            if len(str(val))>7:
                print("Inavlid Imm value")
                continue
        val=str((7-(len(str(val))))*"0")+str(val)
        
        temp=opcode+"0"+r1+str(val)+"\n"
        binary.append(temp)
    elif lines[z]=="C":
        functions.SupportedInstruction("C", p, line_ct)
        functions.FlagError(p)
        if p[0]=="mov":
            opcode="00011"
        else:
            opcode=isa.getInstructionCode(p[0])
        reg1=isa.getRegCode(p[1])
        if p[2]=="FLAGS":
            reg2=isa.getRegCode(p[2])
        else:        
            reg2=isa.getRegCode(p[2])
        temp=opcode+"00000"+reg1+reg2+"\n"
        binary.append(temp)
    elif lines[z]=="D":
        functions.SupportedInstruction("D", p, line_ct)
        functions.FlagError(p)
        functions.check_variable_declaration(variables,inp,line_ct)
        functions.check_variables(variables, p,line_ct)
        opcode=isa.getInstructionCode(p[0])
        reg1=isa.getRegCode(p[1])
        mem=variables[p[2]]
        temp=opcode+"0"+reg1+mem+"\n"
        binary.append(temp)
    elif lines[z]=="E":
        functions.FlagError(p)
        functions.SupportedInstruction("E", p, line_ct)
        if z.split()[1] not in labels.keys():
            print("label not defined")
            quit()
        opcode=isa.getInstructionCode(p[0])
        mem=(labels[p[1]])
        temp=opcode+"0000"+mem+"\n"
        binary.append(temp)
    elif lines[z]=="F":
        opcode=isa.getInstructionCode(p[0])
        temp=opcode+"00000000000"+"\n"
        binary.append(temp)
    elif lines[z]=="G":
        functions.check_variable_declaration(variables,inp,line_ct)
        mem=str(bin(var_count))[2:]
        mem=str((7-(len(str(mem))))*"0")+mem
        variables[p[1]]=mem
        var_count+=1
    functions.InvalidCases(p, line_ct)
    line_ct+=1
binary[-1]=binary[-1][:-1]
for kx in binary:
    sys.stdout.write(kx)



