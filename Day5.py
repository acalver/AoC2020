import pandas as pd

seats = pd.read_csv('./data/Day5_seats.csv', header = None)
seats = seats[0].values

def seatBinarySearch(vector, ticket, vector_min = 0):
    
    if vector == 'row':
        vector_max = 127
    else:
        vector_max = 7
    
    l = len(ticket) - 1
    
    for i in ticket[:l]:
        
        if i == 'F' or i == 'L':
            
            test = (vector_max - vector_min) / 2
            
            if not isinstance(test, int):
                test = round(test)
            
            vector_max -= test
            
        else:
            vector_min += round((vector_max - vector_min) / 2)
            
    if ticket[l] == 'F' or ticket[l] == 'L':
        return vector_min
    else:
        return vector_max
    
i = 'R'
i = 'L'

seat_combo = 0

for s in seats:
    
    row = s[:7]
    col = s[7:]

    row_number = seatBinarySearch(vector = 'row', ticket = row)
    col_number = seatBinarySearch(vector = 'col', ticket = col)
    
    calc = row_number * 8 + col_number
        
    if calc > seat_combo:
        seat_combo = calc
        
print(seat_combo)



seats = 'FFBFFFFRRR'
row = seats[:7]
col = seats[7:]

row_number = seatBinarySearch(vector = 'row', ticket = row)
col_number = seatBinarySearch(vector = 'col', ticket = col)
        
print(row_number * 8 + col_number)

'''
print(seatBinarySearch(max_value = 127, ticket = 'FFFBBBF'))

    col_min, col_max = 0, 7
    
    
        
i = ticket[1]
    
    while not finished:
        if L[minindex][measureIndex] > search or \
            L[maxindex][measureIndex] < search:
            return 'Not in list'
            finished = True
        
        elif search == L[midpoint][measureIndex]:
            #return index and variable value
            return midpoint
        #[L[midpoint][0], L[midpoint][measureIndex]]
            finished = True
        
        elif search > L[midpoint][measureIndex]:
            minindex = midpoint + 1
            if maxindex - minindex == 1:
                midpoint = minindex
            else:
                midpoint = maxindex - ((maxindex - minindex)//2)
            
        else:
            maxindex = midpoint - 1
            if maxindex - minindex == 1:
                midpoint = maxindex
            else:
                midpoint = maxindex - ((maxindex - minindex)//2)
                
    return 'Not in list'
        
'''