#///////////////////// PROBLEM STATEMENT ///////////////////////
# Add up all the numbers in the range 1 to 100 (inclusive)    //
# which are the product of any 3 different numbers less       //
# than this number. For example, 60 = 3 * 4 * 5. Only add the //
# number once.                                                //
#     Answer: 1278                                            //
#///////////////////////////////////////////////////////////////

count = 0

for val in range(1,101):
    goodNum = False
    for a in range(2,val):
        for b in range(2,a):
            for c in range(2,b):
                if a*b*c == val:
                    goodNum = True
    if goodNum == True:
        count = count + val
print(count)
