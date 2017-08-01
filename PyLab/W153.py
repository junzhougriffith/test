##//////// PROBLEM STATEMENT ////////////
## Given 3 numbers, print the largest. //
##   3 2 1 -> 3                        //
##   1 2 3 -> 3                        //
##   3 3 3 -> 3                        //
##///////////////////////////////////////
a = int(input())
b = int(input())
c = int(input())
max_three = a
if b > max_three:
    max_three = b
if c > max_three:
    max_three = c
print(max_three)
