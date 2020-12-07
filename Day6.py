import pandas as pd

cdf = pd.read_csv('./data/Day6_cdf.csv', header = None, skip_blank_lines = False)
cdf = cdf[0].values

cdf_total = set()
cdf_count = 0

total_sum = 0

for i in cdf:
    if not isinstance(i, str):
        total_sum += len(cdf_total)
        cdf_total = set()
    else:
        cdf_total.update(list(i))
    
total_sum += len(cdf_total)
print(total_sum)

###############################################
#PART 2
###############################################
cdf_all_yes = set()
cdf_temp = set()
total_yes_sum = 0
newgroup = True

for i in cdf:
    if not isinstance(i, str):
        total_yes_sum += len(cdf_all_yes)
        cdf_all_yes = set()
        newgroup = True
    elif newgroup:
        cdf_all_yes.update(list(i))
        newgroup = False
        
    else:
        cdf_temp.update(list(i))
        cdf_all_yes = cdf_all_yes.intersection(cdf_temp)
        cdf_temp = set()
    
total_yes_sum += len(cdf_all_yes)
print(total_yes_sum)
