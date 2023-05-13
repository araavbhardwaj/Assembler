import main
isa=main.ISA()
f=open("input.txt","r")
lines={}
inp=f.read().splitlines()
variables={}
labels={}
var_count = 0
for i in range(len(inp)):
    if inp[i][0:3] != "var":
        var_count += 1 
PC=-1
for line in inp:
    PC+=1
    type=""
    x=line.split(" ")
    if ":" in x[0]:
        mem=str(bin(PC))[2:]
        mem=str((8-(len(str(mem))))*"0")+mem
        labels[x[0][:-1]]=mem

        if x[1]=="mov":
            if "R" in x[2] and "R" in x[3]:
                type="C"
            else:
                type="B"
        elif x[1] in isa.instructions:            
            type=isa.getInstructionType(x[1]) 
        lines[line[len(x[0])+1:]]=type
        continue
    elif x[0]=="mov":
        if "R" in x[1] and "R" in x[2]:
            type="C"
        else:
            type="B"
    elif x[0] in isa.instructions:            
        type=isa.getInstructionType(x[0])
        
  
    lines[line]=type
binary=[]
print(labels)
print(lines)
PC=-1
for z in lines.keys():
    PC+=1
    p=z.split(" ")
    if lines[z]=="A":
        opcode=isa.getInstructionCode(p[0])
        r1=isa.getRegCode(p[1])
        r2=isa.getRegCode(p[2])
        r3=isa.getRegCode(p[3])
        temp=opcode+"00"+r1+r2+r3
        binary.append(temp)
    elif lines[z]=="B":
        if p[0]=="mov":
            opcode="00010"
        else:
            opcode=isa.getInstructionCode(p[0])
        r1=isa.getRegCode(p[1])
        imm=bin(int(p[2][1:]))[2:]
        if len(str(imm))>8:
            print("Inavlid Imm value")
            continue
        imm=str((8-(len(str(imm))))*"0")+str(imm)
        
        temp=opcode+r1+str(imm)
        binary.append(temp)
    elif lines[z]=="C":
        opcode=isa.getInstructionCode(p[0])
        reg1=isa.getRegCode(p[1])
        reg2=isa.getRegCode(p[2])
        temp=opcode+"00000"+reg1+reg2
        binary.append(temp)
    elif lines[z]=="D":
        opcode=isa.getInstructionCode(p[0])
        reg1=isa.getRegCode(p[1])
        mem=variables[p[2]]
        temp=opcode+reg1+mem
        binary.append(temp)
    elif lines[z]=="E":
        opcode=isa.getInstructionCode(p[0])
        mem=(labels[p[1]])
        temp=opcode+"000"+mem
        binary.append(temp)
    elif lines[z]=="F":
        opcode=isa.getInstructionCode(p[0])
        temp=opcode+"00000000000"
        binary.append(temp)
    elif lines[z]=="G":
        mem=str(bin(var_count))[2:]
        mem=str((8-(len(str(mem))))*"0")+mem
        variables[p[1]]=mem
        var_count+=1
print(lines)
print(binary)
print(variables)
    
