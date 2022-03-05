# data we need to retrieve
#1. total number of votes cast
#2. a complete list of candidates 
#3. percentage of votes each candidate got 
#4. total number of votes each candidate got
#5. winner by popular vote 
#

#import dependencies 
import os
import csv
import datetime as dt

#reading path
file_to_load = os.path.join("Resources/election_results.csv")
#writing path
file_to_save = os.path.join("analysis", "election-analysis.txt")

#initalize a total vote counter variable 
total_votes = 0

#candidate options list 
candidate_options = []

#candidate vote count dictionary 
candidate_votes = {}

#declare variables for winning statement 
winning_candidate = ""
winning_count = 0
winning_percentage = 0 

#open to read
with open(file_to_load) as election_data:

    #read the file object w reader function
    file_reader = csv.reader(election_data)

    #read and consume header row
    headers = next(file_reader)

    #print rows
    for row in file_reader:
        # add to the total vote count 
        total_votes += 1

        #print the candidate name fo reach row
        candidate_name = row[2]

        # add the candidate name to the candidate list (if for unique)
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # begin tracking that candidate's vote count 
            candidate_votes[candidate_name] = 0
        #increment votes for each candidate 
        candidate_votes[candidate_name]+=1

#determine percentage 
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    print (f" {candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #determine win count and candidate
    #determine if the votes is great than the winning count 
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # if true set win count to votes and win perc to vote perc
        winning_count = votes
        winning_percentage = vote_percentage
        #set win cand
        winning_candidate = candidate_name
winning_summary = (
    f"--------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"---------------------\n"
)    
print(winning_summary)


