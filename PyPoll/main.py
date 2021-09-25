import os
import csv
#Description: print text to terminal
#Input: a list of strings
def print_In_Terminal(texts):
    for text in texts:
        print(text)
#Description: write text to text file
#Input: a file and a list of strings
def write_In_Text(file, texts):
    with open (file, mode = 'w') as txt_file:
        for text in texts:
               txt_file.write(f'{text}\n')
        txt_file.close

election_file = os.path.join(os.getcwd(), 'resources\\election_data.csv') #path of source file
analysis_file = os.path.join(os.getcwd(), 'analysis\\pypoll_analysis.txt') #path of output file
text_result = []
max_vote = 0
#read the poll file and assign items in the a list of dictionary
with open (election_file, mode = 'r') as csv_file:
    election_reader = csv.DictReader(csv_file)
    keys = election_reader.fieldnames
    election_list = list(election_reader)
text_result.append("Election Results")
text_result.append("-------------------------")
total_votes = len(election_list)
text_result.append(f"Total Votes: {total_votes}")
text_result.append("-------------------------")
#get candidate name and their votes 
candidate_vote = {}
for each in election_list:
    if each[keys[2]] in candidate_vote:
        candidate_vote[each[keys[2]]] +=1
    else:
        candidate_vote[each[keys[2]]] = 1
#calculate percentage vote and max vote
for k, v in candidate_vote.items():
    percentage_vote = round((v / total_votes) * 100)
    formatted_percentage_vote = "{:.2f}".format(percentage_vote)
    text_result.append(f"{k}: {formatted_percentage_vote}% ({v})")
    max_vote = max(v,max_vote)
winner = str(([k for k, v in candidate_vote.items() if v == max_vote])).strip()
winner = winner[2:len(winner)-2]
text_result.append("-------------------------")
text_result.append(f"Winner: {winner}")
text_result.append("-------------------------")
print_In_Terminal(text_result)
write_In_Text(analysis_file, text_result)