##//////////////////// PROBLEM STATEMENT //////////////////////////
## Given a number n, print True if n is in the range 1..10,      //
## inclusive. Unless "outsideMode" is True, in which case print  //
## True if the number is less or equal to 1, or greater or equal //
## to 10.                                                        //
##   n  outsideMode                                              //
##   5,    False     -> True                                     //
##   11,   False     -> False                                    //
##   11,   True      -> True                                     //
##/////////////////////////////////////////////////////////////////
a = int(input())
outside_mode = eval(input())
print((not outside_mode and a in range(1,11)) or (outside_mode and a not in range(2, 10)))
