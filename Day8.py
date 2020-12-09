import re
import pandas as pd
import copy

instructions = ['nop +0', 'acc +1', 'jmp +4', 'acc +3', 'jmp -3', 'acc -99', 'acc +1', 'jmp -4', 'acc +6']

code_loop = pd.read_csv('C:\\Users\\328652\\Documents\\Python\\AoC\\Day8_loop.csv', header = None)
code_loop = code_loop[0].values

def loopingInputs(prog = code_loop):
    accumulator = 0
    i_position = 0
    #i = instructions[i_position]
    Looping = False
    completed_actions = []
    
    while not Looping:
        
        if i_position >= len(prog) - 1:
            return((i_position, accumulator))
            
        i = prog[i_position]
        action = i[:3]
    
        if i_position in completed_actions:
            Looping = True
        else:
            completed_actions.append(i_position)
    
            if action == 'nop':
                i_position += 1
                
            elif action == 'acc':
                accumulator += int(re.findall('[-+][0-9]+', i)[0])
                i_position += 1
                
            else:
                i_position += int(re.findall('[-+][0-9]+', i)[0])
  
    return((Looping, accumulator))
        
print(loopingInputs())

###############################################

###############################################


def changeCodeValue(prog):
    
    for j in range(len(prog)):
        
        new_list = prog.copy()
        
        ins = new_list[j]
        action = ins[:3]
        
        if action == 'nop':
             new_list[j] = 'jum ' + re.findall('[-+][0-9]+', ins)[0]
             
        elif action == 'jmp':
            new_list[j] = 'nop ' + re.findall('[-+][0-9]+', ins)[0]
        
        test = loopingInputs(prog = new_list)
        
        if test[0] != True:
            return(test)
            
prog = instructions
print(changeCodeValue(code_loop))
