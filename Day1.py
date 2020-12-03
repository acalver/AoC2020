import pandas as pd

expenseReport = pd.read_csv('Day1_expenses.csv', header=None)

expenseReport = expenseReport[0].values.tolist()

expenseReport_test = [1721,979,366,299,675,1456]

def expenseClean_2(report):
    
    n = len(report)

    for i in range(n):
           
        for j in range(i+1, n):
            
            if report[i] + report[j] == 2020:
                
                return(report[i] * report[j])
            
print(expenseClean_2(expenseReport))

##############################################
#PART 2
##############################################

def expenseClean_3(report):
    
    n = len(report)

    for i in range(n):
           
        for j in range(i+1, n):
            
            #I tried using a break but for some reason it didnt work
            if report[i] + report[j] > 2020:
                j = n-1
            
            for k in range(i+2, n):
    
                if report[i] + report[j] + report[k] == 2020:
                    
                    return(report[i] * report[j] * report[k])
                    
print(expenseClean_3(expenseReport))
            