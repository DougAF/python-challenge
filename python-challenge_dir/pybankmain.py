#Python HW
#imports
# This will allow us to create file paths across operating systems
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
#1.1 Read file
# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)
#1.2 Calculate Total Months
#1.3 Sum of all Profits/Losses
#1.4 Avg change in profits/losses
#1.5 Max inc in Profit (best day)
#1.6 Max Decrease in losses (worst day)
#1.7 Output to terminal and CSV
