##///////////////////////// PROBLEM STATEMENT //////////////////////////
## Given three ints, a b c, one of them is small, one is medium and   //
## one is large. Print True if the three values are evenly spaced,    //
## so the difference between small and medium is the same as the      //
## difference between medium and large.                               //
##   2 4 6 -> True                                                    //
##   4 6 2 -> True                                                    //
##   4 6 3 -> False                                                   //
##//////////////////////////////////////////////////////////////////////
'''
a = int(input())
b = int(input())
c = int(input())

if a - b ==  b - c :
    print(True)
elif a - c == c - b:
    print(True)
elif c - a == a - b:
    print(True)
else:
    print(False)
'''

a = int(input())
b = int(input())
c = int(input())

# find largest int, assign to l
if a > b and a > c:    #  a >= b and a >= c:  because the input may be like 4, 4, 2, in this case, if without '=', no value will assing to l according to the three 'if' conditions.
    l = a

if b > a and b > c:    # b >= a and b >= c:    (similar reason to the first 'if' statement
    l = b

if c > a and c > b:    # c >= a and c >= b:
    l = c

# find median int, assign to m
if (a > b and a < c) or (a > c and a < b):   # (a >= b and a <= c) or (a >= c and a <= b):
    m = a

if (b > a and b < c) or (b > c and b < a):   #(b >= a and b <= c) or (b >= c and b <= a):
    m = b

if (c > a and c < b) or (c > b and c < a):   #(c >= a and c <= b) or (c >= b and c <= a):
    m = c

# find smallest int, assign to s

if (a < b and a < c):   # (a <= b and a <= c):
    s = a

if (b < a and b < c):   # (b <= a and b <= c):
    s = b

if (c < a and c < b):   # (c <= a and c <= b):
    s = c

# calculation the difference between s, m & l

if l - m == l - s:         # this line should be  l - m == m - s:
    print(True)

else:
    print(False)
Thanks