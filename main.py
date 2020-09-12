#Import the files
import os
import csv

# A list to capture the names, votes and percentage of candidates
candidates = []
num_votes = []
percent_votes = []

# counter for the total number of votes 
total_votes = 0

#Create the path to collect data
election_data = os.path.join("Resources","election_data.csv")

# Open and read CSV 
with open(election_data, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes = (total_votes+1)

        #If the candidate is not on our list, add name to our list,
        # along with a vote in their name. If it is already on our list, we will simply add a vote.

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] +=1
    
    # Add to percent_votes list

    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
    
    # To find the winning candidate

    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

# Displaying results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

# Export a text file with the results
election_file = os.path.join("Output", "election_data.txt")
with open(election_file, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Votes: {str(total_votes)}\n")
    for i in range(len(candidates)):
       outfile.write(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})\n")
    outfile.write("--------------------------\n")
    outfile.write(f"Winner: {winning_candidate}\n")
    outfile.write("--------------------------")