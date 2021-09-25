import csv

def analyze_vote(election_file1):
    text_result = []
    max_vote = 0
    #read the poll file and assign items in the a list of dictionary
    with open (election_file1, mode = 'r') as csv_file:
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
    return text_result