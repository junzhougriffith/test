##//////////////////////// PROBLEM STATEMENT ///////////////////////////
## Given 3 int values, a, b, c, print their sum. However, if any of   //
## the values is a teen -- in the range 13..19 inclusive -- then that //
## value counts as 0, except 15 and 16 do not count as a teen. Write  //
## a separate helper function that takes in an int value and returns  //
## that value fixed for the teen rule. In this way, you avoid         //
## repeating the teen code 3 times (i.e. decomposition).              //
##                                                                    //
##   1  2  3 -> 6                                                     //
##   2  13  1 -> 3                                                    //
##   2  1  14 -> 3                                                    //
##//////////////////////////////////////////////////////////////////////

a = int(input())
b = int(input())
c = int(input())

def fixed_value(v):
     #if v in range(13, 20) and v != 15 and v != 16:
     if v in range(13, 15) or v in range(17, 20):
         return 0
     else:
         return v



a1 = fixed_value(a)
b1 = fixed_value(b)
c1 = fixed_value(c)

print(a1 + b1 + c1)
