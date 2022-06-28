import csv
import os

#file_to_load = "Resources\election_results.csv"
#election_data = open(file_to_load, 'r')
#file_to_load.close()

#with open(file_to_load) as election_data:
 
    # print(election_data)
file_to_load = os.path.join{"terminal.integrated.cwd": "C: /Desktop/Election_Analysis/Resources/election_results.csv"}
#os.path.join("Resources", "election_results.csv")
#file_to_load = os.path.join("..","Resources", "election_results.csv")

#with open(file_to_load) as election_data:
    #print(election_data)

file_to_save = os.path.join("analysis", "election_analysis.txt")
#open(file_to_save, "w")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = [] 
candidate_votes = {}    


# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0 
winning_percentage = 0 

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
# Read the header row.
    headers = next(file_reader)
# Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1
# Get the candidate name from each row.
    candidate_name = row[2]
 # If the candidate does not match any existing candidate add it the
        # the candidate list.         
    if candidate_name not in candidate_options:
        candidate_options.append(candidate_name)
        candidate_votes[candidate_name] = 0
        print(candidate_votes)
        candidate_votes[candidate_name] += 1
# Determine winning vote count and candidate
# Determine if the votes is greater than the winning count. 
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
# Determine winning vote count, winning percentage, and candidate.
    
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate_name      
        winning_percentage = vote_percentage

    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage: .1f}%\n"
    f"-------------------------\n"



    


