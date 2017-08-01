##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Say that a "clump" in a list is a series of 2 or more adjacent elements   //
## of the same value. Print the number of clumps in the given list.          //
##    1, 2, 2, 3, 4, 4  -> 2                                                 //
##    1, 1, 2, 1, 1  -> 2                                                    //
##    1, 1, 1, 1, 1  -> 1                                                    //
##/////////////////////////////////////////////////////////////////////////////
n = int(input())

l = list()

for i in range(n):
    l.append(int(input()))

clump = 0

clump_num = 0
clump_occur = True
for i in range(len(l)-1):
    if l[i] == l[i+1]:
        if clump_occur == True:
            clump_num += 1
        clump_occur = False
    else:
        clump_occur = True


print(clump_num)
