##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given a list of ints, print True if the list contains either 3 even or    //
## 3 odd values all next to each other.                                      //
##    2, 1, 3, 5  -  > True                                                  //
##    2, 1, 2, 5  -  > False                                                 //
##    2, 4, 2, 5  -  > True                                                  //
##/////////////////////////////////////////////////////////////////////////////
n = int(input())
li = list()
for i in range(n):
    li.append(int(input()))
i = 0
res = False
while i + 2 <= len(li) -1:
    if li[i] % 2 == li[i+1] % 2 == li[i+2] % 2:
        res = True
    i += 1
print(res)
