##//////////////////////////// PROBLEM STATEMENT ///////////////////////////////
## Print a list that contains the exact same numbers as the given list,       //
## but rearranged so that all the even numbers come before all the odd        //
## numbers. Other than that, the numbers can be in any order. You must modify //
## and print the given list (no additional data structures).                  //
##   1, 0, 1, 0, 0, 1, 1 -> 0, 0, 0, 1, 1, 1, 1                               //
##   3, 3, 2 -> 2, 3, 3                                                       //
##   2, 2, 2 -> 2, 2, 2                                                       //
##//////////////////////////////////////////////////////////////////////////////
n = int(input())
l = list()

for i in range(n):
    l.append(int(input()))

mylist = list()

for item in l:
    if item % 2 == 0:
        mylist.append(item)


for item in l:
    if item % 2 != 0:
        mylist.append(item)

print(mylist)
