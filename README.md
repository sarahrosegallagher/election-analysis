# Election Analysis

## Project Overview
A Colorado Board of Elections employee assigned the following tasks to complete the election audit for a recent local Congressional election. 

1. Calculate the total number of votes cast.
2. Get a complete list of candidates. 
3. Caclulate the total number of votes each candidate received. 
4. Calculate the percentage of votes each candidate won. 
5. Determine the winner of the election based on popular vote. 

## Resources
- Data Source: election_results.csv
- Software: Python 3.10.2, Visual Studio Code 1.65.0

## Summary
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
-The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane

- The candidate results were:
    - Charles Casper Stockham: 23.0% (85,213)
    - Diana DeGette: 73.8% (272,892)
    - Raymon Anthony Doane: 3.1% (11,606)

- The winner of the election was:
    - Diana DeGette, with 73.8% of the vote and 272,892 number of votes.

## Challenge Overview
The secondary project was to return to the original data set to find three additional pieces of information pertaining to the counties where votes were cast.

- Find the voter turnout for each county.
    
- Calculate the percentage of votes from each county out of the total count. 
    
- Find the county with the highest turnout. 

## Challenge Methods  
Each of these pieces of information were found using the same methods as I used for the candidates. I initialized a list for the counties, a dictionary for the votes per county, and variables to track the largest coutny and voter turnout. 

Next, I extracted the county name from each row to use, first, in an if statement to add a unique instance of each county to the list of counties and then to iterate over each row to count each instance of that county as a vote. 

After that, I used a for loop with an if statement to do the following: caculate the percentage of votes for the county; create an f string to write the county results to a text file; determine the winning county and its vote count; create an f string to write the largest county summary to a text file.

Finally, I reviewed the formatting within each f string to be written to the text file, checking for consistency and readability. 

## Challenge Summary 
The results of this analysis are as follows:
- County Votes:
    - Jefferson: 10.5% (38,855)
    - Denver: 82.8% (306,055)
    - Arapahoe: 6.7% (24,801)

- Largest County:
    - Denver 82.8% (306,055)
