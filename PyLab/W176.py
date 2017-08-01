##//////////////////////////// PROBLEM STATEMENT ///////////////////////////////////
## Given three ints, a b c, print True if one of b or c is "close"                //
## (differing from a by at most 1), while the  other is "far", differing          //
## from both other values by 2 or more. Use a function to remove code duplication //
##                                                                                //
##   1 2 10 -> True                                                               //
##   1 2 3 -> False                                                               //
##   4 1 3 -> True                                                                //
##//////////////////////////////////////////////////////////////////////////////////
'''def close(x, y):
    if -1 <= x-y <= 1:
        return True
    return False

def far(x, y):
    if x - y <= -2 or x - y >= 2:
        return True
    return False

a, b, c = int(input()), int(input()), int(input())
print(close(a,b) and far(a,c) and far(b,c) or (close(a,c) and far(b,a) and far(b,c))) '''


def check_distribution(x, y, z):
    if -1 <= x-y <= 1 and (z - x <= -2 or z - x >= 2) and (z - y <= -2 or z - y >= 2):
        return True
    return False

a, b, c = int(input()), int(input()), int(input())
print(check_distribution(a, b, c) or check_distribution(a, c, b))
