import runthis
import sys
import main
import functions

memory = fn.Memory()
program_counter = fn.ProgramCounter()
#here the program variable is a nested list of the output as a binary
#dk if binary is the right variable for it
program = runthis.binary
for address, instruction in enumerate(program):
    memory.write(address, instruction)
register_file = fn.RegisterFile()
halted = False
while not halted:
    instruction = memory.read(program_counter.get())
    halted, new_pc = fn.execute(instruction, program_counter, register_file)
    program_counter.dump()
    register_file.dump()
    program_counter.update(new_pc)
memory.dump()