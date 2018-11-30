import os
import csv

csvpath = os.path.join('election_data.csv')

with open(csvpath, 'r') as csvfile:

    data = csv.reader(csvfile, delimiter=',')
    #print(data)
    header = next(data)
    #print(f"Header: {header}")


    for row in data:                            #Counts the rows of the file, e.g. total numbers of votes
        row_count = 1 + sum(1 for row in data) # I have to add 1 because it read already the first2 rows, but header doesn't count
             
with open(csvpath, 'r') as csvfile:

    data = csv.reader(csvfile, delimiter=',')
    #print(data)
    header = next(data)
    candidate1 = "Khan"
    candidate2 = "Correy"
    candidate3 = "Li"
    candidate4 = "O'Tooley"
    kahn_votes = 0
    correy_votes = 0
    li_votes = 0
    ot_votes = 0
    
    for row in data:
        if row[2] == candidate1:
            kahn_votes = kahn_votes + 1
            
        if row[2] == candidate2:
            correy_votes = correy_votes + 1
        
        if row[2] == candidate3:
            li_votes = li_votes + 1    

        if row[2] == candidate4:
            ot_votes = ot_votes + 1

    percent_kh = (kahn_votes/row_count)*100
    percent_khan = round(percent_kh,2)

    percent_co = (correy_votes/row_count)*100
    percent_correy = round(percent_co,2)
    
    percent_l = (li_votes/row_count)*100
    percent_li = round(percent_l,2)
   
    percent_o = (ot_votes/row_count)*100
    percent_ot = round(percent_o,2)
   
    d = {"Kahn": percent_khan, "Correy": percent_correy, "Li": percent_li, "O'Tooley": percent_ot}
    
    winner = max(d, key=d.get)
    
    print("   Election Results") 
    print("---------------------------------------------------------")
    print(f'Total votes:{row_count}')
    print(f'Kahn:      {percent_khan} % ({kahn_votes})')
    print(f'Correy:    {percent_correy} % ({correy_votes})')
    print(f'Li:        {percent_li} % ({li_votes})')
    print(f"O'Tooley:  {percent_ot} % ({ot_votes})")
    print("---------------------------------------------------------")
    print(f'The winner is: {winner}')
    print("---------------------------------------------------------")


    f= open("PyPoll.txt","w+")
    f.write("   Election Results\r\n") 
    f.write("-------------------------------------------------------\r\n")
    f.write(f'Total votes:{row_count}\r\n')
    f.write(f'Kahn:      {percent_khan} % ({kahn_votes})\r\n')
    f.write(f'Correy:    {percent_correy} % ({correy_votes})\r\n')
    f.write(f'Li:        {percent_li} % ({li_votes})\r\n')
    f.write(f"O'Tooley:  {percent_ot} % ({ot_votes})\r\n")
    f.write("-------------------------------------------------------\r\n")
    f.write(f'The winner is: {winner}\r\n')
    f.write("-------------------------------------------------------\r\n")


