import pandas as pd
#import math 

passports = pd.read_csv('./data/Day4_passports.csv', header = None,
                        skip_blank_lines = False)
passports = list(passports[0].values)

required_entires = set(['byr','iyr','eyr','hgt','hcl','ecl','pid'])
d = dict()
valid_passports = 0
#need this test to avoid double counting passports
tested = False

for i in passports:
    
    if not isinstance(i, str):
        d = dict()
        tested = False
    
    else:
        kv_pairs = i.split(' ')
        
        for j in kv_pairs:
        
            dic_spl = j.split(':')
            d[dic_spl[0]] = dic_spl[1]
            
        if required_entires.issubset(set(d.keys())) and not tested:
            valid_passports += 1
            tested = True
            
            
print(valid_passports)       

next_row = 2

next_row +=1
i = passports[next_row]
