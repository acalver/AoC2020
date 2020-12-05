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

####################################
#PART 2
####################################

seat_id_list = []

for s in seats:
    
    row = s[:7]
    col = s[7:]

    row_number = seatBinarySearch(vector = 'row', ticket = row)
    col_number = seatBinarySearch(vector = 'col', ticket = col)
    
    calc = row_number * 8 + col_number
        
    seat_id_list.append(calc)

seat_id_list= sorted(seat_id_list)


for i in range(len(seat_id_list)):
    if seat_id_list[i+1] != seat_id_list[i]+1:
        print(seat_id_list[i] + 1)
        break