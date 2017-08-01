##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given three ints, a b c, print True if one of b or c is "close"           //
## (differing from a by at most 1), while the  other is "far", differing     //
## from both other values by 2 or more.                                      //
##                                                                           //
##   1 2 10 -> True                                                          //
##   1 2 3 -> False                                                          //
##   4 1 3 -> True                                                           //
##/////////////////////////////////////////////////////////////////////////////
a = int(input())
b = int(input())
c = int(input())

b_close_a = -1 <= b - a <= 1
c_close_a = -1 <= c - a <= 1
b_far_a = b - a <= -2 or b - a >= 2
b_far_c = b - c <= -2 or b - c >= 2
c_far_a = c - a <= -2 or c - a >= 2

if b_close_a and c_far_a and b_far_c:
    t = True
elif c_close_a and b_far_a and b_far_c:
    t = True
else:
    t = False

print(t)
#if -1 <= a-b <= 1 and ((c-a <= -2 or c-a >= 2) and (c - b <=-2 or c-b >= 2)):
#    print(True)
#elif -1 <= a-c <=1 and ((b - a <= -2 or b-a>=2) and (b - c <=-2 or b - c >= 2)):
#    print(True)
#else:
#    print(False)
