##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Print a list that contains exactly the same numbers as the given list,    //
## but rearranged so that every 3 is immediately followed by a 4. Do not     //
## move the 3's, but every other number may move. The list contains the      //
## same number of 3's and 4's, every 3 has a number after it that is not a 3 //
## or 4, and a 3 appears in the list before any 4.                           //
##    1, 3, 1, 4  -> 1, 3, 4, 1                                              //
##    1, 3, 1, 4, 4, 3, 1  -> 1, 3, 4, 1, 1, 3, 4                            //
##    3, 2, 2, 4  -> 3, 4, 2, 2                                              //
##/////////////////////////////////////////////////////////////////////////////
n = int(input())
l = list()
for i in range(n):
    l.append(int(input()))

for i in range(n-1):
    if l[i] == 3 and l[i + 1] != 4:
        for k in range(n):
            if l[k] == 4 and l[k-1] != 3:

                l[k], l[i+1] = l[i+1], l[k]
                #l[i+1] = 4
                break

print(l)
