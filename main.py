import os

import csv

csvpath = os.path.join("C:\\Users\\jackb\\Desktop\\python-challenge\\Pybank\\pybankcsv.csv" )

#row = []

total = 0

average_change = 0

greatest_profit_increase = 0

greatest_profit_decrease = 0

number_of_months = 0

with open(csvpath, newline="", errors='ignore') as csvfile:
   
    csvreader = csv.reader(csvfile,delimiter=',')
    
    reader=next(csvreader)
    
    for row in csv.reader(csvfile):
        
        total+= int(row[1])
        
        number_of_months+=1

        average_change = (total / number_of_months)


   
    print("Total Months: ", + number_of_months)

    print("Total: $", + total)

    print("Average Change: $", + average_change)

    print("Greatest Profit Increase: $", greatest_profit_increase)

    print("Greatest Profit Decrease: $", greatest_profit_decrease)

        
       



    












