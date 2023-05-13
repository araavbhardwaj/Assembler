import main
encoding={"A":["opcode","unused"]}
isa=main.ISA()
f=open("input.txt","r")
lines={}
inp=f.readlines()
for line in inp:
    type=""
    x=line.split(" ")
    if x[0]=="mov":
        if "R" in x[1] and "R" in x[2]:
            type="C"
        else:
            type="B"
    elif x[0] in isa.instructions:            
        type=isa.getInstructionType(x[0])
    lines[line[:-1]]=type
    print(type)
binary=[]
for z in lines.keys():
    if lines[z]=="A":
        p=z.split(" ")
        opcode=isa.getInstructionCode(p[0])
        r1=isa.getRegCode(p[1])
        r2=isa.getRegCode(p[2])
        r3=isa.getRegCode(p[3])
        temp=opcode+"00"+r1+r2+r3
        binary.append(temp)
    elif lines[z]=="B":
        p=z.split(" ")
        if p[0]=="mov":
            opcode="00010"
        else:
            opcode=isa.getInstructionCode(p[0])
        r1=isa.getRegCode(p[1])
        imm=bin(int(p[2][1:]))[2:]
        if len(str(imm))>8:
            print("Inavlid Imm value")
            continue

        imm=str(imm)+str((8-(len(str(imm))))*"0")
        
        temp=opcode+r1+str(imm)
        binary.append(temp)
    elif lines[z]=="C":
        p=z.split(" ")
        opcode=isa.getInstructionCode(p[0])
        reg1=isa.getRegCode(p[1])
        reg2=isa.getRegCode(p[2])
        temp=opcode+"00000"+reg1+reg2
        binary.append(temp)
    elif lines[z]=="D":
        p=z.split(" ")
        opcode=isa.getInstructionCode(p[0])
        reg1=isa.getRegCode(p[1])
        mem=p[2]
        temp=opcode+reg1+mem
        binary.append(temp)
    elif lines[z]=="E":
        opcode=isa.getInstructionCode(p[0])
        mem=p[1]
        temp=opcode+"000"+mem
        binary.append(temp)
    elif lines[z]=="F":
        opcode=isa.getInstructionCode(p[0])
        temp=opcode+"00000000000"
        binary.append(temp)
print(binary)
    
    