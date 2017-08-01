##/////////////////////////// PROBLEM STATEMENT ////////////////////////////////
## Given a list length 1 or more of ints, print the difference between the    //
## largest and smallest values in the list.                                   //
##    10, 3, 5, 6  -> 7                                                       //
##    7, 2, 10, 9  -> 8                                                       //
##    2, 10, 7, 2  -> 8                                                       //
##//////////////////////////////////////////////////////////////////////////////

n = int(input())

l = list()

for i in range(n):
    l.append(int(input()))

print(max(l) - min(l))
