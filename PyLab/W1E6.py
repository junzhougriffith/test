##/////////////////////////// PROBLEM STATEMENT /////////////////////////////
## Write a binary search function which searches an item in a sorted       //
## list. The function should return the index of element to be searched in //
## the list. Read the list and search for 11 and 12                        //
##///////////////////////////////////////////////////////////////////////////

def bin_search(l, item):
    left = 0
    right = len(l) -1
    while left <= right :
        mid = (right + left)//2
        if l[mid] == item:
            return mid
        elif l[mid] > item:
            right = mid - 1
        else:
            left = mid + 1
    return -1



li=[2,5,7,9,11,17,222]
print(bin_search(li,11))
print(bin_search(li,12))
