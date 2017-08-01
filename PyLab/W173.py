##///////////////////////// PROBLEM STATEMENT //////////////////////////
## Given three ints, a b c, one of them is small, one is medium and   //
## one is large. Print True if the three values are evenly spaced,    //
## so the difference between small and medium is the same as the      //
## difference between medium and large. Use a function.               //
##   2 4 6 -> True                                                    //
##   4 6 2 -> True                                                    //
##   4 6 3 -> False                                                   //
##//////////////////////////////////////////////////////////////////////


def evenly_spaced(x, y, z):
    return y - x == z - y

a, b, c = int(input()), int(input()), int(input())
print(evenly_spaced(a, b, c) or evenly_spaced(b, a, c) or evenly_spaced(a, c, b))
