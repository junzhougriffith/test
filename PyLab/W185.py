#///////////////////// PROBLEM STATEMENT /////////////////////
# Read integers until -1 is input. Print the length of the  //
# longest continuous sequence of numbers where a number is  //
# the sum of the 2 preceding numbers. Do not include the    //
# first 2 numbers in the length of the sequence.            //
#     1,2,3,4,5,8,13,21,34,55,10,6,7,8,20,25,30,40,-1 => 4  //
#     1,2,3,4,5,10,15,20,8,13,21,34,55,89,144,-1 => 5       //
#     5,8,13,21,34,55,89,144,1,2,3,4,5,10,15,20,-1 => 6     //
#/////////////////////////////////////////////////////////////
n1 = int(input())

n2 = int(input())

maxlen = 0

curlen = 0
while True:

    n3 = int(input())
    if n3 == -1:
        break
    if n1 + n2 == n3:
        curlen +=1
        if curlen > maxlen:
            maxlen = curlen
    else:

        curlen = 0
    n1 = n2
    n2 = n3
print(maxlen)
