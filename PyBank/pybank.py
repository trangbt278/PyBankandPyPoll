import csv
import sys

def analyze_fiancial(budget_file):
    total_amount = 0
    average_change = 0
    lo, hi = sys.float_info.max, - sys.float_info.max -1 #get max and min of the system float
    pre_amount = sys.float_info.max
    text_result = []
    changes = []
    with open (budget_file, mode = 'r') as csv_file:
        budget_reader = csv.DictReader(csv_file) #read the file to dict
        keys = budget_reader.fieldnames #get dict keys (headers)
        budget_list = list(budget_reader) #convert the dictreader to list
    budget_rows = len(budget_list) #get total of months
    for each in budget_list:
        profit_loss = float(each[keys[1]])
        if pre_amount != sys.float_info.max:
            cur_amount = profit_loss
            changes.append(cur_amount - pre_amount ) #add changes in Profit/Losses in a list
            pre_amount = cur_amount
        else: 
            cur_amount = profit_loss
            pre_amount = cur_amount
        total_amount += profit_loss #get total amount
        lo, hi = min(profit_loss, lo), max(profit_loss, hi) #get greatest increase and greatest decrease
    
    average_change = "{:.2f}".format(sum(changes)/len(changes)) # get average change
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
    return text_result




