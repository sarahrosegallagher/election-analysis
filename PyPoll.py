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

#open to read
with open(file_to_load) as election_data:

    #read the file object w reader function
    file_reader = csv.reader(election_data)

    #read and consume header row
    headers = next(file_reader)
    print(headers)



