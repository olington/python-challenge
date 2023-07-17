#dependencies
import os
import csv

#path
csvpath = os.path.join("Resources", "election_data.csv")

#variables
Charles_Casper_Stockham_count = 0
Diana_DeGette_count = 0
Raymon_Anthony_Doane_count = 0

#open file
with open(csvpath) as csvfile:    
    csvreader = csv.reader(csvfile, delimiter=',')
    #Read header
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")

    voter_information = csvfile   


    # set up what we want to look for
    candidate_list = {}
    row_count = 0
    
    for row in csvreader:
        #print(row[2]) and get candidate votes
        if row[2] == "Charles Casper Stockham":
            Charles_Casper_Stockham_count += 1
        elif row[2] == "Diana DeGette":
            Diana_DeGette_count += 1
        elif row[2] == "Raymon Anthony Doane":
            Raymon_Anthony_Doane_count += 1
        
        row_count += 1    
#print(row_count)        
# print(Charles_Casper_Stockham_count)
# print(Diana_DeGette_count)
# print(Raymon_Anthony_Doane_count)

Charles_Casper_Stockham_percentage = (Charles_Casper_Stockham_count / row_count) * 100
Diana_DeGette_percentage = (Diana_DeGette_count / row_count) * 100
Raymon_Anthony_Doane_percentage = (Raymon_Anthony_Doane_count / row_count) * 100

print(Charles_Casper_Stockham_percentage)
print(Diana_DeGette_percentage)
print(Raymon_Anthony_Doane_percentage)

#result summary
output = (f"Election Results\n"
    f"---------------------------------------------------------------------------\n"
    f"Total Votes: {row_count}\n"
    f"---------------------------------------------------------------------------\n"
    f"Charles Casper Stockham: {Charles_Casper_Stockham_percentage: .2f}% ({Charles_Casper_Stockham_count})\n"
    f"Diana DeGette: {Diana_DeGette_percentage: .2f}% ({Diana_DeGette_count})\n"
    f"Raymon Anthony Doane: {Raymon_Anthony_Doane_percentage: .2f}% ({Raymon_Anthony_Doane_count})\n"
    f"---------------------------------------------------------------------------\n"
    f"Winner : Diana DeGette\n"
    f"---------------------------------------------------------------------------\n")       

print(output)    

file_to_save = os.path.join("Analysis", "output_file.txt")

#Export as txt.file
with open(file_to_save, "w") as txt_file:
    txt_file.write(output)
    