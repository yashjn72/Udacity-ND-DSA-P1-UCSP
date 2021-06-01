"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# addeing 1st column and 2nd column of texts and calls list i.e. caller and receiver
numberlist = [text[0] for text in texts] + [text[1] for text in texts] + [call[0] for call in calls] + [call[1] for call in calls]
uniquenumlist = set(numberlist)
print("There are " + str(len(uniquenumlist))+ " different telephone numbers in the records.")


#print(set([text[0] for text in texts] + [text[1] for text in texts] + [call[0] for call in calls] + [call[1] for call in calls]))

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
