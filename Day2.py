import pandas as pd
import re

passwords = pd.read_csv('./data/Day2_passwords.csv', header=None)

passwords['MinLetter'] = passwords[0].str.extract(r'(^[0-9]*)')
passwords['MaxLetter'] = passwords[0].str.extract(r'((?<=-)[0-9]{1,2})')
passwords['TestLetter'] = passwords[0].str.extract(r'([a-z])')
passwords['TestString'] = passwords[0].str.extract(r'((?<=:).*)')

passwords['MinLetter'] = pd.to_numeric(passwords['MinLetter'])
passwords['MaxLetter'] = pd.to_numeric(passwords['MaxLetter'])

count = 0
for i in range(len(passwords)):
    letter = passwords['TestLetter'][i]
    letter_list = passwords['TestString'].str.findall(letter)[i]
    letter_count = letter_list.count(letter)
    
    if letter_count >= passwords['MinLetter'][i] and letter_count <= passwords['MaxLetter'][i]:
        count += 1
        
print(count)


##############################################
#PART 2
##############################################

count = 0
for i in range(len(passwords)):
    letter = passwords['TestLetter'][i]
    
    if (letter == passwords['TestString'][i][passwords['MinLetter'][i]] or \
    letter == passwords['TestString'][i][passwords['MaxLetter'][i]]) and \
        not(letter == passwords['TestString'][i][passwords['MinLetter'][i]] and \
    letter == passwords['TestString'][i][passwords['MaxLetter'][i]]):
        count += 1
        
print(count)
