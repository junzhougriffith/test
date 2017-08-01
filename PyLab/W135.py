##/////////////// PROBLEM STATEMENT ////////////////
## Given two temperatures, print True if one is   //
## less than 0 and the other is greater than 100. //
##   120, -1 -> True                              //
##   -1, 120 -> True                              //
##   2, 120 -> False                              //
##//////////////////////////////////////////////////
t1 = int(input())
t2 = int(input())
print((t1<0 and t2>100) or (t2<0 and t1>100))
