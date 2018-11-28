import os
import csv

csvpath = os.path.join('election_data.csv')

with open(csvpath, 'r') as csvfile:

    data = csv.reader(csvfile, delimiter=',')
    #print(data)
    header = next(data)
    #print(f"Header: {header}")

#Counts the rows of the file, e.g. total numbers of votes
    for row in data:
        row_count = 1 + sum(1 for row in data) # I have to add 1 because it read already the first2 rows, but header doesn't count
        print("   Election Results") 
        print("-------------------------")
        print(f'Total votes:{row_count}')
        


#d = {}
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

    #print(kahn_votes)
    #print(correy_votes)
    #print(li_votes)
    #print(ot_votes)
    percent_kh = (kahn_votes/row_count)*100
    percent_khan = round(percent_kh,2)
    #print(percent_khan)
    percent_co = (correy_votes/row_count)*100
    percent_correy = round(percent_co,2)
    #print(percent_correy)
    percent_l = (li_votes/row_count)*100
    percent_li = round(percent_l,2)
    #print(percent_li)
    percent_o = (ot_votes/row_count)*100
    percent_ot = round(percent_o,2)
    #print(percent_ot)
    print(f'Kahn:      {percent_khan} % ({kahn_votes})')
    print(f'Correy:    {percent_correy} % ({correy_votes})')
    print(f'Li:        {percent_li} % ({li_votes})')
    print(f"O'Tooley:  {percent_ot} % ({ot_votes})")

  # d[row['Kahn']] = d.get(row['Kahn'], 0) + 1
        
 
#for k in d:
 #   print('{} => {}'.format(k, d[k]))   
    
   


       
    
    #    if (row[2]) == "Kahn":
           # kahn_votes = sum(1 for row in data) sum(1 for row in data if str(row) == "Kahn")
         #   print(kahn_votes)
     #   elif (row[2]) == "Correy":
        #    correy_votes = 1 + sum(1 for row in data) 
       #     print(correy_votes)
      #  elif (row[2]) == "Li":
          #  li_votes = 1 + sum(1 for row in data) 
           # print(li_votes)    
      #  elif (row[2]) == "O'Tooley":
            #ot_votes = 1 + sum(1 for row in data) 
            #print(ot_votes)   