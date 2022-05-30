# Dependencies
from importlib import resources
import os
import csv

# Specify the file to read
file_path = os.path.join("Resources", "election_data.csv")

# Open the file using "read" mode. Specify the variable to hold the contents
with open(file_path) as csvfile:

    # Initialize csv.reader
    csvreader = csv.reader(csvfile)

    header=next(csvreader)

    #print(header[1])

    #define the variables
    voter_ids=[]
    counties=[] 
    candidates=[] 
    candidate_names=[] 
    total_votes=[]
    result_printout=[] 
    percentage_vote=[] 

    #Set conditions at 0
    line_count=0
    winnervotes=0
    loservotes=0
    loop1=0
    loop2=0
    loop3=0
    loop4=0
    
    #Read data in rows f data and assign to columns
    for row in csvreader:
        voterid=row[0] 
        county=row[1] 
        candidate=row[2] 
        voter_ids.append(voterid) 
        counties.append(county) 
        candidates.append(candidate) 
    
    #Calculate total number of votes in the "Voter ID" column
    line_count= len(voter_ids) #
    #print )line_count)

#Select first candidate name for comparison
candidate_names.append(candidates[0]) 
#print (candidate_names)

#Loop through candidates list to determine who was voted for 
for loop1 in range (line_count-1):
    if candidates[loop1+1] != candidates[loop1] and candidates[loop1+1] not in candidate_names:
        candidate_names.append(candidates[loop1+1])

n=len(candidate_names)
#print(n)

#Loop through to get range of candidates with votes and count votes to add to list total
for loop2 in range (n): 
    total_votes.append(candidates.count(candidate_names[loop2])) 
#print(n))
#print(total_votes)

#Loop through to get range of candidates with votes and calculate % per candidate found. Find the winner
for loop3 in range(n): 
    percentage_vote.append(f'{round((total_votes[loop3]/line_count*100), 4)}%') 
    if total_votes[loop3]>winnervotes: 
        winner=candidate_names[loop3]
        winnervotes=total_votes[loop3]
#print(winner)

#Loop through and format list of the results print out
for loop4 in range(n):
    result_printout.append(f'{candidate_names[loop4]}: {percentage_vote[loop4]} ({total_votes[loop4]})')

resultlines='\n'.join(result_printout) 

#output lines
#I had to google this one below
analysis=f'\
Election Results\n\
----------------------------\n\
Total Votes: {line_count}\n\
----------------------------\n\
{resultlines}\n\
----------------------------\n\
Winner: {winner} \n\
----------------------------\n'

print(analysis) 

#output into text file named pypoll.txt

file1=open("pypoll.txt","w") 
file1.writelines(analysis) 
file1.close() 