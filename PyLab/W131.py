##///////////// PROBLEM STATEMENT /////////////
## Write Python code which, when it reads    //
## two input boolean values, produces the    //
## following results:                        //
##                                           //
##   True True   -> False                    //
##   True False  -> False                    //
##   False True  -> False                    //
##   False False -> True                     //
##/////////////////////////////////////////////
#b1 = eval(input())
#b2 = eval(input())
#print( not (b1 or b2))


#if input() == 'True':
#    a = True
#else:
#    a = False

a = (input() == 'True')
b = (input() == 'True')


if a == True and b == True:
    print(False)
elif a == True and b == False:
    print(False)
elif a == False and b == True:
    print(False)
else:
    print(True)
