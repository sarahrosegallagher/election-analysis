
#import dependencies 
import os
import csv

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

# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}

#declare variables for winning statement 
winning_candidate = ""
winning_count = 0
winning_percentage = 0 

# 2: Track the largest county and county voter turnout.
largest_county = ""
largest_county_count = 0
largest_county_percentage = 0

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

        # 3: Extract the county name from each row.
        county_name = row[1]

        # add the candidate name to the candidate list (if for unique)
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # begin tracking that candidate's vote count 
            candidate_votes[candidate_name] = 0
        #increment votes for each candidate 
        candidate_votes[candidate_name]+=1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:
            county_options.append(county_name)

            # 4b: Add the existing county to the list of counties.


            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0 
        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1



# save results to our text file
with open (file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    #save the final vote count to text file
    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        cvotes = county_votes.get(county_name)
        # 6c: Calculate the percentage of votes for the county.
        county_percentage = float(cvotes) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_result = (f"{county_name}: {county_percentage:.1f}% ({cvotes:,})\n")
         # 6e: Save the county votes to a text file.
        txt_file.write(county_result)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (cvotes > largest_county_count) and (county_percentage > largest_county_percentage):
            largest_county_count = cvotes
            largest_county_percentage = county_percentage
            largest_county = county_name 

    # 7: Print the county with the largest turnout to the terminal.
    largest_county_summary = (
        f"-------------------------\n"
        f"Largest County: {largest_county}\n"
        f"Largest County Vote Count: {largest_county_count:,}\n"
        f"Largest County Vote Percentage: {largest_county_percentage:.1f}%\n"
        f"-------------------------\n"
    )    
    print(largest_county_summary)
    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_county_summary)


    #determine percentage 
    for candidate_name in candidate_votes:
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f" {candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        #determine win count and candidate
        #determine if the votes is great than the winning count 
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if true set win count to votes and win perc to vote perc
            winning_count = votes
            winning_percentage = vote_percentage
            #set win cand
            winning_candidate = candidate_name
    winning_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")    
    print(winning_summary)
    txt_file.write(winning_summary)


