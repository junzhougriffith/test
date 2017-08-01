##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given a string, print a new string made of 3 copies of the first 2 chars  //
## of the original string. The string may  be any length. If there are fewer //
## than 2 chars, use whatever is there.                                      //
##   "Hello" -> "HeHeHe"                                                     //
##   "ab" -> "ababab"                                                        //
##   "H" -> "HHH"                                                            //
##/////////////////////////////////////////////////////////////////////////////
s1 = input()

if len(s1) >= 2:
    print(s1[:2] * 3)
else:
    print(s1[:] + s1[:] + s1[:])
