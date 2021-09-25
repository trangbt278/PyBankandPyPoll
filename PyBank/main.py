import os
import csv
import sys
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

budget_file = os.path.join(os.getcwd(), 'resources\\budget_data.csv') #path of source file
analysis_file = os.path.join(os.getcwd(), 'analysis\\pybank_analysis.txt') #path of output file
total_amount = 0
average_change = 0
lo, hi = sys.float_info.max, - sys.float_info.max -1 #get max and min of the system float
text_result = []
with open (budget_file, mode = 'r') as csv_file:
    budget_reader = csv.DictReader(csv_file) #read the file to dict
    keys = budget_reader.fieldnames #get dict keys (headers)
    budget_list = list(budget_reader) #convert the dictreader to list
budget_rows = len(budget_list) #get total of months
for each in budget_list:
    profit_loss = float(each[keys[1]])
    total_amount += profit_loss #get total amount
    lo, hi = min(profit_loss, lo), max(profit_loss, hi) #get greatest increase and greatest decrease
hi_keys = [each[keys[0]] for each in budget_list if float(each[keys[1]]) == hi] #get dates for greatest increase
lo_keys = [each[keys[0]] for each in budget_list if float(each[keys[1]]) == lo] #get dates for greatest decrease

text_result.append("Financial Analysis")
text_result.append("----------------------------") 
text_result.append(f"Total Months: {budget_rows}") #text for total of months
text_result.append(f"Total: ${total_amount}") #text for total amount
text_result.append(f"Average  Change: ${average_change}") # text for average change
for each in hi_keys:
    text_result.append(f"Greatest Increase in Profits: {each} (${hi})") #text for the greatest increase
for each in lo_keys:
    text_result.append(f'Greatest Decrease in Profits: {each} (${lo})') #text for the greatest decrease

print_In_Terminal(text_result) #call a function to write the result to the termnial
write_In_Text(analysis_file, text_result) # call a function to write the result the txt file



