import os
import csv

# My variables:
months = []     #this will store a list of dates.
list1 = []      #this will store a list of profit.
list2 = []      #stores change
sum_profits = 0

csvpath = os.path.join('budget_data.csv')

with open(csvpath, 'r') as csvfile:

    data = csv.reader(csvfile, delimiter=',')
    header = next(data)
   
    for row in data:                            #Counts the rows of the file, e.g. the months listed
        row_count = 1 + sum(1 for row in data) # I have to add 1 because it read already the first2 rows, but header doesn't count
    
# Sum the content of the second column             
with open(csvpath, 'r') as csvfile:
    
    data = csv.reader(csvfile, delimiter=',')
    headerline = next(data)
    
    
    for row in data:
        sum_profits += int(row[1])
    
with open(csvpath, 'r') as csvfile:
    
    data = csv.reader(csvfile, delimiter=',')
    headerline = next(data)
    
    for row in data:                    # Loop through the data
        months.append(row[0])           #Append the months and profits to new list
        list1.append(float(row[1]))
        
    for i in range(1, len(list1)):
        change = list1[i] - list1[i-1] 
        list2.append(change)
    
    n = len(list2) 
    
    avrg_change = sum(list2) / n 
    average_change = (round(avrg_change,2))
    
    max_profits = (max(list2))
    month_max_id = (list2.index(max(list2))) + 1
    month_max_profit = months[month_max_id]
    
    min_profits =(min(list2))
    month_min_id = (list2.index(min(list2))) + 1
    month_min_profit = months[month_min_id]
    
    print("   Financial Analysis") 
    print("--------------------------------------------------------------------------------")
    print(f'Total months:                       {row_count}')
    print(f'Total:                              ${sum_profits}')
    print(f'Average Change:                     ${average_change}')  
    print(f'Greatest increase in Profits:       {month_max_profit}  ${max_profits}')   
    print(f'Greatest decrease in Profits:       {month_min_profit}  ${min_profits}')   
    
    
    
    f= open("PyBank.txt","w+")
    f.write("Financial Analysis\r\n") 
    f.write("--------------------------------------------------------------------------------\r\n")
    f.write(f'Total months:                       {row_count}\r\n')
    f.write(f'Total:                              ${sum_profits}\r\n')
    f.write(f'Average Change:                     ${average_change}\r\n')  
    f.write(f'Greatest increase in Profits:       {month_max_profit}  ${max_profits}\r\n')   
    f.write(f'Greatest decrease in Profits:       {month_min_profit}  ${min_profits}\r\n')   