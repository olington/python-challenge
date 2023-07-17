#dependencies
import os
import csv

#path
csvpath = os.path.join("Resources", "election_data.csv")

#open file
with open(csvpath) as csvfile:    
    csvreader = csv.reader(csvfile, delimiter=',')
    #Read header
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")

    voter_information = csvfile
   
    ballot_id_count = int(voter_information[0])    
    Charles_Casper_Stockham_count = 0
    Diana_Degette_count = 0
    Raymon_Anthony_Doane_count = 0

    total_votes = len(ballot_id_count)
    print(total_votes)
    # set up what we want to look for
    candidate_list = {}


    # loop through each row of the data set
# for row in csvreader:

   
    # if row[2] == "Charles_Casper_Stockham":
    #     Charles_Casper_Stockham_count += 1
    # elif row[2] == "Diana Degette":
    #     Diana_Degette_count += 1
    # elif row[2] == "Raymon Anthony Doane":
    #     Raymon_Anthony_Doane_count += 1