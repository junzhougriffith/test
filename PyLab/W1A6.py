##//////////////// PROBLEM STATEMENT //////////////////
## Given a string, print a "rotated left 2" version  //
## where the first 2 chars are moved to the end. The //
## string length will be at least 2.                 //
##   "Hello" -> "lloHe"                              //
##   "Python" -> "thonPy"                            //
##   "Hi" -> "Hi"                                    //
##/////////////////////////////////////////////////////

## >>>>>> Your Python Code starts here <<<<<<
a = input()
res = a[2:] + a[:2]

print(res)

## >>>>>> Your Python Code ends here <<<<<<
