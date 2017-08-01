##//////////////////////////// PROBLEM STATEMENT /////////////////////////////
## Print the "centered" average of a list of ints, which we'll say is the   //
## mean average of the values, except not counting the largest and smallest //
## values in the list.  Use int division to produce the final average. You  //
## may assume that the list is length 3 or more.                            //
##    1, 2, 3, 4, 100  -> 3                                                 //
##    1, 1, 5, 5, 10, 8, 7  -> 5                                            //
##    -10, -4, -2, -4, -2, 0  -> -3                                         //
##////////////////////////////////////////////////////////////////////////////

n = int(input())
l = list()
for i in range(n):
    l.append(int(input()))

l.remove(min(l))
l.remove(max(l))

print(sum(l)//len(l))
