##///////////////////// PROBLEM STATEMENT /////////////////////////
## Given three ints, a b c, print True if b is greater than a,   //
## and c is greater than b. However, with the exception that if  //
## "bOk" is True, b does not need to be greater than a.          //
##   a b c  bOk                                                  //
##   1 2 4 False -> True                                         //
##   1 2 1 False -> False                                        //
##   1 1 2 True  -> True                                         //
##/////////////////////////////////////////////////////////////////
a, b, c = int(input()), int(input()), int(input())
bok = eval(input())
print((not bok and c > b >a) or (bok and c > b))
