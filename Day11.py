import copy
import pandas as pd

seats = pd.read_csv('./data/Day11_seats.csv', header = None)
seats = list(seats[0].values)

seatsL = []

for l in seats:
    seatsL.append(list('0'+l+'0'))
seatsL.insert(0, ['0']*len(seatsL[0]))
seatsL.append(['0']*len(seatsL[0]))

def seatStatus(matrix, i,j):
    
    #position = matrix[i][j]
    surroundingList = []
    
    surroundingList.append(matrix[i-1][j-1])
    surroundingList.append(matrix[i-1][j])
    surroundingList.append(matrix[i-1][j+1])
    surroundingList.append(matrix[i][j+1])
    surroundingList.append(matrix[i+1][j+1])
    surroundingList.append(matrix[i+1][j])
    surroundingList.append(matrix[i+1][j-1])
    surroundingList.append(matrix[i][j-1])
    
    surroundingD = dict()
    for s in surroundingList:
        if s not in surroundingD:
                surroundingD[s] = 1
        else:
            surroundingD[s] += 1
            
    return surroundingD


#test = seatStatus(seating_plan, 1, 4)  

def seatChanging(data):
    
    new_plan = copy.deepcopy(data)

    change = True
    while change:
        change = False
        occupied = 0
        
        for i in range(1, len(data) - 1):
            
            for j in range(1, len(data[0])-1):
                #print(i, j)
                position = data[i][j]
                if position == '#':
                    occupied += 1
                
                test = seatStatus(data, i, j)  
        
                if position == 'L' and test.get('#',0) == 0:
                    new_plan[i][j] = '#'
                    change = True
                if position == '#' and test.get('#',0) >= 4:
                    new_plan[i][j] = 'L'
                    change = True
        
        data = copy.deepcopy(new_plan)
        
    print(occupied)
    
#seatChanging(seating_plan)
seatChanging(seatsL)

#############################################
#PART 2
#############################################

    
seating_plan[2]
seating_plan = [list('0L.LL.LL.LL0'),
                #list('000000000000'),
list('0LLLLLLL.LL0'),
list('0L.L.L..L..0'),
list('0LLLL.LL.LL0'),
list('0L.LL.LL.LL0'),
list('0L.LLLLL.LL0'),
list('0..L.L.....0'),
list('0LLLLLLLLLL0'),
list('0L.LLLLLL.L0'),
list('0L.LLLLL.LL0')]
seating_plan.append(['0']*12)
seating_plan.insert(0,['0']*12)

