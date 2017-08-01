##///////////// PROBLEM STATEMENT /////////////////////
## Read 3 integers and print them in ascending order //
##   1 3 2 -> 1 2 3                                  //
##   3 1 2 -> 1 2 3                                  //
##   8 5 2 -> 2 5 8                                  //
##/////////////////////////////////////////////////////
a = int(input())
b = int(input())
c = int(input())
'''
if a > b:
    m = a
    a = b
    b = m
if b > c:
    m = b
    b = c
    c = m
if a > b:
    m = a
    a = b
    b = m
print(a, b, c)
'''
s = [a, b, c]
#s.sort()
print(s.sort())