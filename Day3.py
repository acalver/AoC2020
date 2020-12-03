import pandas as pd

toboggan = pd.read_csv('./data/Day3_toboggan.csv', header = None)
toboggan = toboggan[0].values

def traversal(right, down, data = toboggan):
    position = 0
    count = 0
    for i in range(down, len(data), down):
        position = (position + right) % 31
        
        if data[i][position] == '#':
            count += 1

    return(count)

R3_D1 = traversal(right = 3, down = 1)
print(R3_D1)

##########################################
#PART 2
##########################################


R1_D1 = traversal(right = 1, down = 1)
R5_D1 = traversal(right = 5, down = 1)
R7_D1 = traversal(right = 7, down = 1)
R1_D2 = traversal(right = 1, down = 2)


print(R1_D1 * R3_D1 * R5_D1 * R7_D1 * R1_D2)    
