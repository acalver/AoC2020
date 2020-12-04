import pandas as pd
import re

passports = pd.read_csv('./data/Day4_passports.csv', header = None,
                        skip_blank_lines = False)
passports = list(passports[0].values)

required_entires = set(['byr','iyr','eyr','hgt','hcl','ecl','pid'])

def valid_passports(required = required_entires, data = passports):

    d = dict()
    valid_p = []
    #need this test to avoid double counting passports
    tested = False
    
    for i in data:
        
        if not isinstance(i, str):
            d = dict()
            tested = False
        
        else:
            kv_pairs = i.split(' ')
            
            for j in kv_pairs:
            
                dic_spl = j.split(':')
                d[dic_spl[0]] = dic_spl[1]
                
            if required.issubset(set(d.keys())) and not tested:
                valid_p.append(d)
                tested = True
               
    return(valid_p)

valid = valid_passports()
print(len(valid))


##################################
#PART 2
##################################

def valid_entries(data = valid):
    
    valid_e = 0
    
    for i in valid:
        
        keys = sorted(i.keys())
        
        if 'cid' in keys:
            keys.remove('cid')
            
        byr_test = int(i['byr'])
        ecl_test = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        eyr_test = int(i['eyr'])
        hcl_test = re.search('^#[a-z0-9]{6}', i['hcl'])
        hgt_test = re.search('^[0-9]{2,3}[cmin]{2}$',i['hgt'])
        iyr_test = int(i['iyr'])
        pid_test = re.search('^[0-9]{9}$', i['pid'])
        
        
        if byr_test >= 1920 and byr_test <= 2020 and \
        i['ecl'] in ecl_test and \
        eyr_test >= 2020 and eyr_test <= 2030 and \
        hcl_test is not None and \
        iyr_test >= 2010 and iyr_test <= 2020 and \
        pid_test is not None and \
        hgt_test is not None:
            
            if (hgt_test.group()[3:5] == 'cm' and int(hgt_test.group()[0:3]) >= 150 and int(hgt_test.group()[0:3]) <= 193) or \
            (hgt_test.group()[3:5] == 'in' and int(hgt_test.group()[0:3]) >= 59 and int(hgt_test.group()[0:3]) <= 76):
                
                valid_e += 1
        
        
    return(valid_e)
        
        
print(valid_entries())       

i = valid[0]
