##////////////////////////////// PROBLEM STATEMENT /////////////////////////////
## Write Python code that reads a boolean and an integer from the keyboard.   //
## If the boolean is True and the integer is in the range 1. . 100 OR if      //
## the boolean is False and the integer is not in the range 1..100 and the    //
## integer is not in the range -20..-8 print True. Otherwise print False.     //
## You must not use the Python if or if-else statement.                       //
##                                                                            //
## All ranges are inclusive                                                   //
##                                                                            //
## Example inputs/outputs are:                                                //
##    True 50   -> True                                                       //
##    True -5   -> False                                                      //
##    False 50  -> False                                                      //
##    False 200 -> True                                                       //
##    False -5  -> True                                                       //
##//////////////////////////////////////////////////////////////////////////////
b = eval(input())
n = int(input())
#in_range1 = n >= 1 and n <= 100
in_range1 = 1 <= n <= 100
in_range2 = -20 <= n <= -8
print((b and in_range1) or (not b and not in_range1 and not in_range2))
