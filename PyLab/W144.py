##/////////// PROBLEM STATEMENT ///////////////
## Given 2 int values, print True if either  //
## of them is in the range 10..20 inclusive. //
##   12, 99 -> True                          //
##   21, 12 -> True                          //
##   8, 99 -> False                          //
##/////////////////////////////////////////////
a = int(input())
b = int(input())
print(a in range(10, 21) or b in range(10, 21))
