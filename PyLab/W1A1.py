##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given a string, print a string length 2 made of its first 2 chars. If the //
## string length is less than 2, use  '@' for the missing chars.             //
##   ("hello") -> "he"                                                       //
##   ("hi") -> "hi"                                                          //
##   ("h") -> "h@"                                                           //
##/////////////////////////////////////////////////////////////////////////////
s = input()

if len(s) >= 2:
    print(s[:1])

else:
    print(s + '@')
