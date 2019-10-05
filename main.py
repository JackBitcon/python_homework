import os

import csv

voter_csv = os.path.join("C:\\Users\\jackb\\Desktop\\python-challenge\\Pypoll\\Pypoll_Resources_election_data.csv")

total_votes = 0

khan_votes = 0

correy_votes = 0

li_votes = 0

otooley_votes = 0

khan_percent = 0

correy_percent = 0

li_percent = 0

otooley_percent = 0

with open(voter_csv, newline="", errors='ignore') as csvfile:

    csvreader = csv.reader(csvfile,delimiter=',')
    
    reader=next(csvreader)
    
    for row in csv.reader(csvfile):

        total_votes+=1

        name = str(row[2])

        if name == "Khan":

            khan_votes+=1

        if name == "Correy":

            correy_votes+=1

        if name == "Li":

            li_votes +=1

        if name == "O'Tooley":

            otooley_votes+=1

        khan_percent = float(khan_votes/total_votes)

        correy_percent = float(correy_votes/total_votes)

        li_percent = float(li_votes/total_votes)

        otooley_percent = float(otooley_votes/total_votes)

    print("Election Results: ")

    print("-------------------------------")
    
    print("Total Votes: ", + total_votes)

    print("-------------------------------")

    print(f"Khan: ", + khan_votes, "(",khan_percent,")")

    print(f"Correy: ", + correy_votes, "(",correy_percent,")")

    print(f"Li: ", + li_votes, "(",li_percent,")")

    print(f"O'Tooley: ", + otooley_votes, "(",otooley_percent,")")

    print("-------------------------------")

    print("Winner: Khan")

    print("-------------------------------")





