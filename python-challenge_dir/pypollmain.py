#Python HW
#imports
# This will allow us to create file paths across operating systems
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

#2.1 Read csv

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
#2.2 Analyze vote and calc Total

#2.3 List Unique Candidates
#2.4 % of votes each Candidate won Can_per = (Can_vote/Total_vote)100
#2.5 Total # votes each candidate Can_per x Total Vote or sum by tick
#2.6 Candidate with most votes (print max)
#2.7 Outputs to toerminal and to CSV
