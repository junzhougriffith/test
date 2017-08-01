##/////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Write a program to read the file. ./dataFiles/mbox-short.txt and:        //
##   1. Build a histogram that shows how many messages have come from       //
##      each email address, and print the counts in ascending order.        //
##   2. Determine who has the most messages in the file and print how       //
##      many messages the person has.                                       //
##////////////////////////////////////////////////////////////////////////////
fame = "../dataFiles/mbox-short.txt"
h = open(fame, 'r')
dfrom = dict()

for line in h:
    line = line.rstrip()
    if line.startswith('From:'):
        words = line.split(" ")
        dfrom[words[1]] = dfrom.get(words[1],0)+1

lst1 = sorted(dfrom.values())

bigcount = None
bigword = None
for word,count in dfrom.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count


print(lst1,"Most emails: %s"%bigword)
