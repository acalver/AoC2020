import pandas as pd
import itertools

preamble = [35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576]
        
encoded = pd.read_csv('./data/Day9_encoding.csv', header = None)
encoded = list(encoded[0].values)
    
def encodedSum(input_list, check_length):
    
    for k in range(check_length, len(input_list)):
        target = input_list[k]
        #print('target = ', target)
        sequence = input_list[k-check_length:k]
        #print('sequence =', sequence)
    
        totals_list = []
        for i in range(check_length):
            
            for j in range(i+1, check_length):
                
                totals_list.append(sequence[i] + sequence[j])
                
        if target not in totals_list:
            return target

print(encodedSum(encoded, 25))
