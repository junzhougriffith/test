##///////////////////// PROBLEM STATEMENT /////////////////////////
## Your cell phone rings. Print True if you should answer it.    //
## Normally you answer, except in the morning you only answer if //
## it is your mum calling. In all cases, if you are asleep, you  //
## do not answer.                                                //
##                                                               //
##  Morning  Mum   Asleep    Result                              //
##   False  False  False  -> True                                //
##   False  False  True   -> False                               //
##   True   False  False  -> False                               //
##/////////////////////////////////////////////////////////////////
morning = eval(input())
mum = eval(input())
asleep = eval(input())
if asleep:
    print( not asleep)
else:
    if morning:
        if mum:
            print(mum)
        else:
            print(mum)
    else:
        print(not morning)
