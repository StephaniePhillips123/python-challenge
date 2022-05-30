# Dependencies
from importlib import resources
import os
import csv

# Specify the file to read
file_path = os.path.join("Resources", "budget_data.csv")

# Open the file using "read" mode. Specify the variable to hold the contents
with open(file_path) as csvfile:

    # Initialize csv.reader
    csvreader = csv.reader(csvfile)

    header=next(csvreader)

    #print(header[1])

    # define the variables
    Profit = []
    months = []
    net_change = []

    #read through each row of data after header
    for rows in csvreader:
        Profit.append(int(rows[1]))
        months.append(rows[0])

    # calculate total length of months
    total_months = len(months)
    #print total months
    
    # find net amount of profit and loss & net change
    
    for x in range(1, len(Profit)):
        net_change.append((int(Profit[x]) - int(Profit[x-1])))
    #print nret change

    # calculate average revenue change
    revenue_average = sum(net_change) / len(net_change)
    #print average change

    # greatest increase in revenue
    greatest_increase = max(net_change)
    #print increase in rev

    # greatest decrease in revenue
    greatest_decrease = min(net_change)
    #print decrease in rev

    # print the Results
    print("Financial Analysis")

    print("....................................................................................")

    print("total months: " + str(total_months))

    print("Total: " + "$" + str(sum(Profit)))

    print("Average change: " + "$" + str(revenue_average))

    print("Greatest Increase in Profits: " + str(months[net_change.index(max(net_change))+1]) + " " + "$" + str(greatest_increase))

    print("Greatest Decrease in Profits: " + str(months[net_change.index(min(net_change))+1]) + " " + "$" + str(greatest_decrease))

     # make an output to a text file

    file = open("pybank.txt","w")

    file.write("Financial Analysis" + "\n")

    file.write("...................................................................................." + "\n")

    file.write("total months: " + str(total_months) + "\n")

    file.write("Total: " + "$" + str(sum(Profit)) + "\n")

    file.write("Average change: " + "$" + str(revenue_average) + "\n")

    file.write("Greatest Increase in Profits: " + str(months[net_change.index(max(net_change))+1]) + " " + "$" + str(greatest_increase) + "\n")

    file.write("Greatest Decrease in Profits: " + str(months[net_change.index(min(net_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")

    file.close()