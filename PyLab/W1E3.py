##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given an int list, print a new list with double the length where its      //
## last element is the same as the original list, and all the other          //
## elements are 0. The original list will be length 1 or more.               //
##    4, 5, 6  -> 0, 0, 0, 0, 0, 6                                           //
##    1, 2  -> 0, 0, 0, 2                                                    //
##    3  -> 0, 3                                                             //
##/////////////////////////////////////////////////////////////////////////////
n = int(input())
l = list()

for i in range(n):
    l.append(int(input()))

nl = list()
for i in range(2*len(l)):
    nl.append(0)

nl[-1] = l[-1]

print(nl)
