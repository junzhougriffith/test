##///////////// PROBLEM STATEMENT /////////////
## Write Python code which, when it reads    //
## two input boolean values, produces the    //
## following results:                        //
##                                           //
##   True True   -> False                    //
##   True False  -> False                    //
##   False True  -> True                     //
##   False False -> False                    //
##/////////////////////////////////////////////

#b1 = eval(input())
#b2 = eval(input())
#print((not b1) and b2)

a = eval(input())
b = eval(input())

if a == True and  b == True:
    res = False
elif a == True and b == False:
    res = False
elif a == False and b == True:
    res = True
else:
    res = False

print(res)
