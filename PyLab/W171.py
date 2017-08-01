##////////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Write a program that reads 3 numbers and prints the largest. Use a function //
## to reduce code duplication. Do not use the Python max function.             //
##///////////////////////////////////////////////////////////////////////////////
# a = 1, b = 2, c = 3
# input
a = int(input())
b = int(input())
c = int(input())

# computation
def my_max(x, y):
    if x > y:
        return x
    else:
        return y

large_ab = my_max(a, b)
res = my_max(large_ab, c)
#res = my_max(my_max(a,b), c)

# output
print(res)
