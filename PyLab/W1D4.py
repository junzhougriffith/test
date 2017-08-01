##/////////// PROBLEM STATEMENT ///////////////
## Given a list of ints, print True if the   //
## list contains no 1's and no 3's.          //
##    0, 2, 4  -  > True                     //
##    1, 2, 3  -  > False                    //
##    1, 2, 4  -  > False                    //
##/////////////////////////////////////////////
n = int(input())
l = list()
res = True
for i in range(n):
    l.append(int(input()))

if 3 in l or 1 in l:
    res = False
print(res)
