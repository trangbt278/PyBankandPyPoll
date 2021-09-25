import os
budget_file = os.path.join(os.getcwd(), 'PyBank\\resources\\budget_data.csv') #path of source file
fn_analysis_file = os.path.join(os.getcwd(), 'PyBank\\analysis\\pybank_analysis.txt') #path of output file
election_file = os.path.join(os.getcwd(), 'PyPoll\\resources\\election_data.csv') #path of source file
poll_analysis_file = os.path.join(os.getcwd(), 'PyPoll\\analysis\\pypoll_analysis.txt') #path of output file

from PyBank import pybank
from PyPoll import pypoll
print(election_file)
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

# analyze financial from PyBank budget file
print("***************************PYBANK FINANCIAL***************************")
text_result = []
text_result = pybank.analyze_fiancial(budget_file)
print_In_Terminal(text_result)
write_In_Text(fn_analysis_file, text_result) 
print('\n')
print('\n')
print("***************************PYPOLL VOTES***************************")
# analyze vote from PyPoll election file
text_result = pypoll.analyze_vote(election_file)
print_In_Terminal(text_result)
write_In_Text(poll_analysis_file,text_result)
