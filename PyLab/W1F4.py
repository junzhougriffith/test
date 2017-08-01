##////////////////////////////// PROBLEM STATEMENT ///////////////////////////
## Write a function counts the number of k-mers in a string containing DNA. //
## You must read the string and an integer n and find the number of times   //
## each substring of length n occurs in the string.                         //
##////////////////////////////////////////////////////////////////////////////
s = input()
n = int(input())
d = dict()

for i in range(len(s)-n + 1):
    d[s[i:i + n]] = d.get(s[i:i+n], 0) +1

t = sorted(d.items())
for v, n in t:
    print('%s:%d'%(v, n), end = ' ')
