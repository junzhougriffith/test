##//////////// PROBLEM STATEMENT //////////////////
## Given an int n, print the absolute difference //
## between n and 21, except print double the     //
## absolute difference if n is over 21.          //
##   19 -> 2                                     //
##   10 -> 11                                    //
##   21 -> 0                                     //
##/////////////////////////////////////////////////
n = int(input())
if n <= 21:
    result = 21 - n
else:
    result = (n - 21) * 2
print(result)
