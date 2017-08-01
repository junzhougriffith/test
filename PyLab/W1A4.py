##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given a string, print the string made of its first two chars, so the      //
## String "Hello" yields "He". If the string is shorter than length 2, print //
## whatever there is, so "X" yields "X", and the empty string "" yields the  //
## empty string "".                                                          //
##   "Hello" -> "He"                                                         //
##   "abcdefg" -> "ab"                                                       //
##   "ab" -> "ab"                                                            //
##/////////////////////////////////////////////////////////////////////////////

a = input()

if len(a) >= 2:
    print(a[:2])
else:
    print(a)
