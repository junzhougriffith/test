##//////////////////////////// PROBLEM STATEMENT ////////////////////////////////
## Given 2 strings, a and b, print a new string made of the first char of a    //
## and the last char of b, so "yo" and  "Python" yields "yn". If either string //
## is length 0, use '@' for its missing char.                                  //
##   "last", "chars" -> "ls"                                                   //
##   "yo", "Python" -> "yn"                                                    //
##   "hi", "" -> "h@"                                                          //
##///////////////////////////////////////////////////////////////////////////////
a = input()
b = input()
if len(a) == 0:
    a = '@'
if len(b) == 0:
    b = '@'
print(a[0] + b[-1])