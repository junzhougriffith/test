##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## We'll say that a lowercase 'g' in a string is "happy" if there is another //
## 'g' immediately to its left or right.  Print True if all the g's in the   //
## given string are happy.                                                   //
##   "xxggxx" -> True                                                        //
##   "xxgxx" -> False                                                        //
##   "xxggyygxx" -> False                                                    //
##/////////////////////////////////////////////////////////////////////////////
string = input()
res = True
if len(string) == 1:
    res = False
elif len(string) >1:
    n = 1
    while n < len(string)-1:
        if string[n] == 'g':
            if string[n + 1] != 'g' and string[n - 1] != 'g':
                res = False
        n += 1
    if string[0] == 'g' and  string[1] != 'g':
        res = False
    if string[-1] == 'g' and string[-2] != 'g':
        res = False

print(res)
