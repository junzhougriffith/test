##////////////////////// PROBLEM STATEMENT ///////////////////////
## Read file "../dataFiles/mbox-short.txt" and record the       //
## domain name where the message was sent from instead of who   //
## the mail came from (i.e., the whole email address). At the   //
## end of the program, print out the values of your             //
## dictionary sorted by domain name.                            //
##////////////////////////////////////////////////////////////////
fname = "../dataFiles/mbox-short.txt"
h = open(fname, 'r')
emai_from = dict()


for line in h:
    line = line.rstrip()


    if line.startswith('From:'):
        words = line.split(" ")
        words = words[1].split("@")
        emai_from[words[1]] = emai_from.get(words[1],0)+1

lst1 = sorted(emai_from.items())
res = []
for c, n in lst1:
    res.append(n)
print(res)
