#import dependencies
import os
import csv

#path
csvpath = os.path.join("..", "Resources", "budget_data.csv")

#start with what to look for
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999]
total_net = 0


 #open file
with open(csvpath) as csvfile:    
    csvreader = csv.reader(csvfile, delimiter=',')
    #Read header
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")
    
    first_row = next(csvreader)
#Add up to get the total months
    total_months += 1
    prev_net = int(first_row[1])
    total_net += int(first_row[1])
    
    for row in csvreader:
        total_months += 1
        total_net += int(row[1])
        
        #net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]
        
        #greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            #then
            greatest_increase[1] = net_change
            
        #greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row [0]
            greatest_decrease[1] = net_change

#average change
monthly_avg = sum(net_change_list) / len(net_change_list)

#result summary
output = (f"FINANCIAL ANALYSIS\n"
    f"---------------------------------------------------------------------------\n"
    f"Total months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${monthly_avg: .2f}\n"
    f"Grestest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Grestest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")               

print(output)    

#Export as txt.file
with open("output_file.txt", "w") as txt_file:
    txt_file.write(output)
    