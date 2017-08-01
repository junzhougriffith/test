##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given an int list, if there is a 2 in the list immediately followed by    //
## a 3, set the 3 element to 0. Print the changed list.                      //
##   1, 2, 3 -> 1, 2, 0                                                      //
##   2, 3, 5 -> 2, 0, 5                                                      //
##   1, 2, 1 -> 1, 2, 1                                                      //
##/////////////////////////////////////////////////////////////////////////////

n = int(input())

l = list()

for i in range(n):
    l.append(int(input()))

for i in range(n-1):
    if l[i] == 2 and l[i+1] == 3:
        l[i+1] = 0


print(l)
