##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given a string, print True if the first 2 chars in the string also appear //
## at the end of the string, such as with "edited".                          //
##   "edited" -> True                                                        //
##   "edit" -> False                                                         //
##   "ed" -> True                                                            //
##/////////////////////////////////////////////////////////////////////////////
s = input()
if len(s) == 1:
    print(False)
else:
    fir2_s = s[:2]
    las2_s = s[-2:]
    if fir2_s == las2_s:
        print(True)
    else:
        print(False)