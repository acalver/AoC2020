import pandas as pd

jolt = pd.read_csv('./data/Day10_jolt.csv', header = None)
jolt = jolt[0].values

def joltDifferences(data):
    
    data = sorted(data)
    data.insert(0,0)
    data.append(max(data) + 3)

    one_diff = 0
    three_diff = 0
    
    for i in range(len(data) - 1):
        j = i + 1
        
        if data[j] - data[i] == 1:
            one_diff += 1
        
        elif data[j] - data[i] == 3:
            three_diff += 1
        
    print(one_diff * three_diff)
    
joltDifferences(jolt)

#########################################
#PART 2
########################################

def adapterCombinations(data):
    data = sorted(data)
    data.append(max(data) + 3)
    
    #start = list(filter(lambda x: x < 4, data))
    
    arrangements = dict()
    
    if 1 in data:
        arrangements[1] = 1
    if 2 in data:
        arrangements[2] = 2
    if 3 in data:
        arrangements[3] = 4
    
    for i in range(len(arrangements), len(data)):
        
        x1, x2, x3 = data[i] -3, data[i] - 2, data[i] - 1
        
        arrangements[data[i]] = arrangements.get(x1,0) + arrangements.get(x2, 0) + arrangements.get(x3,0)
        
    print(arrangements[max(data)])

print(adapterCombinations(data = jolt))



print(adapterCombinations(data = eg))
print(adapterCombinations(data = long_input))
eg = [16,10,15,5,1,11,7,19,6,12,4]
long_input = [28,
33,
18,
42,
31,
14,
46,
20,
48,
47,
24,
23,
49,
45,
19,
38,
39,
11,
1,
32,
25,
35,
8,
17,
7,
9,
4,
2,
34,
10,
3]