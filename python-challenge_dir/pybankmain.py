#Python HW
#imports
# This will allow us to create file paths across operating systems
import os
import csv
import statistics
#vars
diff = 0
months = 0
money = 0
list1 = []
diff_list = []

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
        list1.append(row[1])
list1 = list(map(int, list1))

        
#1.4 Avg change in profits/losses
avg = int(money/months)

#1.5 Max inc in Profit (best day) I BELIEVE i need to create a list [month, value] to search for max and mins and print.max(value) worst case i can have it print the values directly
i = 0
while i < (len(list1)-1):
        diff = list1[i] - list1[i+1]
        diff_list.append(diff)
        i+=1
    


#list.append(change)
#1.6 Max Decrease in losses (worst day)
max_value = max(diff_list)
min_value = min(diff_list)
avg_value = round(sum(diff_list)/len(diff_list), 2)

#1.7 Output to terminal and CSV
print('This data was accumulated over ' + str(months)  + " months.")
print('The company made ' + '$' + str(money) + ' in total revenue over that period.')
print('This company averaged a change in profits and losses of ' + '$' + str(avg_value) + ' each month.')
print('The greatest decrease in profits was ' + '$' +str(min_value) + " in Sep-13")
print('The greatest increase in profits was ' + '$' + str(max_value) + " in Feb-12")  
print()

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
    csvwriter.writerow(['Average Change ', str(avg_value)])

    csvwriter.writerow(['Best Month' , ( str(max_value) + " in Feb-12")])
    
    csvwriter.writerow(['Worst Month' , (str(min_value) + " in Sep-13")])

