# The data we need to retrieve
    # The total number of votes cast
    # A complete list of candidates who recived votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote

import datetime as dt
#now = dt.datetime.now()    
#print ("The time right now is ", now) 

import csv
dir(csv)

import os
dir(os)

file_to_load = "C:\\Users\\LSchu\\Documents\\Class\\Python\\Challange 3\\election_results (1).csv"

file_to_save = "C:\\Users\\LSchu\\Documents\\Class\\Python\\Challange 3\\election_analysis.txt"


# Initialize a total vote counter.
total_votes = 0

candidate_options = []
candidate_votes = {}

#county list
county_list = []
#votes dictionary
county_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0


# empty string for county with largest turn out
largest_county_turnout = ""
# variable for number of votes in larest county turnout
winning_county_count = 0
winning_county_percentage = 0



# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes += 1

        # Get the candidate name from each row.
        candidate_name = row[2]
            
        # Extract the county name from each row.
        county_name = row[1]


        # If the candidate does not match any existing candidate add it to the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1


        # Write an if statement that checks that the county does not match any existing county in the county list.
        if county_name not in county_list:

            county_list.append(county_name)

            county_votes[county_name] = 0

            print(county_votes)

        # Add a vote to that county's vote count.
        county_votes[county_name] += 1


with open(file_to_save, "w") as txt_file:

    # Print the final vote count (
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

 # for loop to get the county from the county dictionary
    for county_name in county_votes:

        # county vote count
        votes = county_votes[county_name]

        # percentage of votes for the county
        vote_percentage = float(votes) / float(total_votes) * 100

        
        county_results = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_results,end="")

        txt_file.write(county_results)

        # if statement to determine the winning county and get its vote count
        if (votes > winning_county_count) and (vote_percentage > winning_county_percentage):
            winning_county_count = votes
            winning_county = county_name
            winning_county_percentage = vote_percentage
    
    # print the county with the largest turnout to the terminal.
    Largest_County_Turnout = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n"
        )
    
    print(Largest_County_Turnout)

 # Save the county with the largest turnout to a text file.
    txt_file.write(Largest_County_Turnout)
    Candidate_Votes = (f"\nCandidate Votes:\n")
    print(Candidate_Votes,end="")
    txt_file.write(Candidate_Votes)


    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        
        Candidate_Votes = (f"Candidate Votes:\n")
        
        print(candidate_results,end="")
       
        txt_file.write(candidate_results)

        # winning vote count, winning percentage, and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate 
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    
    txt_file.write(winning_candidate_summary)


