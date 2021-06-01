"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

callerdict =  dict.fromkeys([(call[0]) for call in calls] + [(call[1]) for call in calls],0)

for i in calls:
    callerdict[i[0]] += int(i[3])
    callerdict[i[0]] += int(i[3])

maxvalue = max(callerdict.items(), key=lambda k: k[1])

print(str(maxvalue[0]) + " spent the longest time, " + str(maxvalue[1]) + " seconds, on the phone during September 2016.")


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

