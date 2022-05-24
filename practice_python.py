#the data we need to retrieve
#total no of votes cast
#list of candidates who received votes
#the percentage of votes each candidate won
#total no of votes each candidate won
#the winner of election based on popular vote
import csv
#assign a variable for the file to load and the path
file_to_load='Resources\election_results.csv'
#assign a variable to a direct path
file_to_save='analysis\election_analysis.txt'

with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    print(headers)


# Use the open statement to open the file as a text file.
with open(file_to_save,'w') as txt_file:
# Write some data to the file.
    txt_file.write("Counties in the Election\n-----------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
   