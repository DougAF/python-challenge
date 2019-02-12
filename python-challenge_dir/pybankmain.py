#Python HW
#imports
# This will allow us to create file paths across operating systems
import os
import csv
#vars

months = 0
money = 0
csvpath = os.path.join('Resources', 'budget_data.csv')

# lambda arguments : expression
#diff = lambda x, y : y - x

#1.1 Read file
# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) #skips header

    # Read each row of data after the header
    for row in csvreader:
        months += 1 #1.2 Calculate Total Months
        money += int(row[1]) #1.3 Sum of all Profits/Losses
#1.4 Avg change in profits/losses
avg = int(money/months)
#1.5 Max inc in Profit (best day) I BELIEVE i need to create a list [month, value] to search for max and mins and print.max(value) worst case i can have it print the values directly

#1.6 Max Decrease in losses (worst day)

#1.7 Output to terminal and CSV
print('This data was accumulated over ' + str(months)  + " months.")
print('The company made ' + '$' + str(money) + ' over that period.')
print('This company averaged a profit of ' + '$' + str(avg) + ' each month.')
    
    # Specify the file to write to --> write to csv
output_path = os.path.join("Resources", "newbudget_data.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfileout:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfileout, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Output', 'Value'])

    # Write the Third  row
    csvwriter.writerow(['Total Months ', months])
    # Write the Fourth row
    csvwriter.writerow(['Total Revenue ', money])
    # Write the second row
    csvwriter.writerow(['Average Change ', "1"])

    csvwriter.writerow(['Best Month' , ("Date " + "income")])
    
    csvwriter.writerow(['Worst Month' , ("Date " + "income")])