#Python HW
#imports
# This will allow us to create file paths across operating systems
import os
import csv
import statistics
# VARS and SETS
khan = 0
correy = 0
li = 0
otooley = 0
khan_per = 0
correy_per = 0
li_per = 0
otooley_per = 0
Total_vote = 0

location = set()

Candidate_set, Cand_vote = set(), set()

csvpath = os.path.join('Resources', 'election_data.csv')

#2.1 Read csv
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) #skips header

    for row in csvreader:
        Candidate_set.add(row[2])#2.3 List Unique Candidates
        location.add(row[1])
        Total_vote +=1 #1.3 Sum of all Votes
        #Candidate Conditionals
        if row[2] == 'Khan':
            khan+=1
        if row[2] == 'Correy':
            correy+=1
        if row[2] == 'Li':
            li+=1
        if row[2] == "O'Tooley":
            otooley+=1
    #Percents (could def a function once for all 4 perhaps)
    khan_per = round(((khan/Total_vote)*100), 1)
    correy_per = round(((correy/Total_vote)*100), 1)
    li_per = round(((li/Total_vote)*100), 1)
    otooley_per = round(((otooley/Total_vote)*100), 1)



#2.7 Outputs to toerminal and to CSV
print('The Candidates tracked in this election were ' + str(Candidate_set))
print("There were a total of " + str(Total_vote) + " votes cast across the " + str(location) + " regions.")
print("The candidate Khan recieved " + str(khan) + " votes, or " + (str(khan_per)) + " percent of the total vote.")
print("The candidate O'Tooley recieved " + str(otooley) + " votes, or " + (str(otooley_per)) + " percent of the total vote.")
print("The candidate Correy recieved " + str(correy) + " votes, or " + (str(correy_per)) + " percent of the total vote.")
print("The candidate Li recieved " + str(li) + " votes, or " + (str(li_per)) + " percent of the total vote.")
print("WINNER ------> MR.KHAN! with " + str(khan) + " votes, or " + (str(khan_per)) + " percent of the voters, a confidant majority.")

    #Write to csv# Specify the file to write to
output_path = os.path.join( "Resources", "newpoll.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Candidate', 'Vote Count', 'Vote Percentage'])

    # Write the second row
    csvwriter.writerow(['Khan', str(khan), str(khan_per)])
    csvwriter.writerow(['Li', str(li), str(li_per)])
    csvwriter.writerow(["O'Tooley", str(otooley), str(otooley_per)])
    csvwriter.writerow(['Correy', str(correy), str(correy_per)])
    csvwriter.writerow(['#######', '#######', '#######'])
    csvwriter.writerow(['Total Votes', 'Winner'])
    csvwriter.writerow([str(Total_vote), 'Mr.Khan!'])