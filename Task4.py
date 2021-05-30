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

stext = set([text[0] for text in texts])
rtext = set([text[1] for text in texts])
scall = set([call[0] for call in calls])
rcall = set([call[1] for call in calls])

tnum = list(((scall - stext)-rtext)-rcall)

tnum.sort()

print("These numbers could be telemarketers: ")
print(*tnum, sep = "\n")

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

