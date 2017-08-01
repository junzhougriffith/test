##////////////// PROBLEM STATEMENT ////////////////
## We'll say that a number is "teen" if it is in //
# the range 13..19 inclusive. Given 3 integer   //
# values, print True if 1 or more of them are   //
# teen.                                         //
#   13, 20, 10 -> True                          //
##   20, 19, 10 -> True                          //
##   20, 10, 13 -> True                          //
##/////////////////////////////////////////////////
a = int(input())
b = int(input())
c = int(input())
# print(13 <= a <= 19 or 13 <= b <= 19 or 13 <= c <= 19)
print(a in range(13, 20) or b in range(13, 20) or c in range(13, 20))
