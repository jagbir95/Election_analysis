# Add our dependencies.
import csv
file_to_load='Resources\election_results.csv'
#assign a variable to a direct path
file_to_save='analysis\election_analysis.txt'
#Initialize a total vote counter.
total_votes=0

candidate_options=[]

candidate_votes={}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes+=1
        # Get the candidate name from each row.
        candidate_name=row[2]
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name]=0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name]+=1

# Use the open statement to open the file as a text file.
with open(file_to_save,'w') as txt_file:
# Write some data to the file.
    txt_file.write("Election Results\n-----------------------\n")
    txt_file.write(f"Total votes: {total_votes:,}\n-----------------------\n")
        
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes_count=candidate_votes[candidate_name]
        vote_percentage=(votes_count/total_votes)*100
        txt_file.write(f"{candidate_name}: {vote_percentage:.1f}% of ({votes_count:,})\n")
        # print all candidate results to the terminal
        print(f"{candidate_name}: {vote_percentage:.1f}% of ({votes_count:,})\n")
        # Determine winning vote count, winning percentage, and candidate.
        if (votes_count>winning_count) and (vote_percentage>winning_percentage):
            winning_count=votes_count
            winning_candidate=candidate_name
            winning_percentage=vote_percentage
        else:
            pass
    # Print the winning candidates' results to the terminal.
    winning_candidate_summary=(
        f"-----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning vote count: ({winning_count:,})\n"
        f"Winning percentage: {winning_percentage:.1f}%\n"
        f"-----------------------------\n"
    )
    print(winning_candidate_summary)
    txt_file.write(f"{winning_candidate_summary}")
    

   