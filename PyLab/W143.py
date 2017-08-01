##////////////////////////////// PROBLEM STATEMENT /////////////////////////////
## Write Python code that reads two integers from the keyboard. Given two     //
## inclusive ranges -8..-4 and 10..16 print True if both integers are in one  //
## of these ranges or both integers are not in these ranges. Otherwise print  //
## False.                                                                     //
## You must not use the Python if or if-else statement.                       //
##                                                                            //
## All ranges are inclusive                                                   //
##                                                                            //
## Example inputs/outputs are:                                                //
##    10 50   -> False                                                        //
##    20 5    -> True                                                         //
##    100 20  -> True                                                         //
##    -5 20   -> False                                                        //
##    -5 12   -> True                                                         //
##    -10 0   -> True                                                         //
##//////////////////////////////////////////////////////////////////////////////
a = int(input())
b = int(input())
range1 = a in range(-8, -3) or a in range(10, 17)
range2 = b in range(-8, -3) or b in range(10, 17)
print((range1 and range2) or (not range1 and not range2))
