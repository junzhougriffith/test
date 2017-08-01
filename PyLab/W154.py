##////////////////////// PROBLEM STATEMENT //////////////////////////
## You have a blue lottery ticket, with ints a, b, and c on it.    //
## This makes three pairs, which we'll call ab, bc and ac.         //
## Consider the sum of the numbers in each pair. If any pair sums  //
## to exactly 10, the result is 10. Otherwise if the ab sum is     //
## exactly 10 more than either bc or ac sums, the result is 5.     //
## Otherwise the result is 0.                                      //
##   9, 1, 0 -> 10                                                 //
##   9, 2, 0 -> 0                                                  //
##   6, 1, 4 -> 10                                                 //
##///////////////////////////////////////////////////////////////////
a = int(input())
b = int(input())
c = int(input())
ab = a + b
bc = b + c
ac = a + c
if ab == 10 or bc == 10 or ac ==10:
    result = 10
elif ab - bc == 10 or ab - ac == 10:
    result = 5
else:
    result = 0
print(result)
