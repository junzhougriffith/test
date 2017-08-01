#///////////////////// PROBLEM STATEMENT /////////////////////
# Read integers until -1 is input. Print the length of the  //
# longest continuous sequence numbers where the increment   //
# or decrement is constant. Include the first number of the //
# sequence in the length of the sequence.                   //
#     1,2,3,4,5,6,7,10,6,7,8,20,25,30,40,55,60,-1 => 7      //
#     1,2,3,4,5,10,15,20,6,20,15,10,5,0,-5,-10,-15,-1 => 8  //
#/////////////////////////////////////////////////////////////

'''
n1 = int(input())
if n1 == -1:
    maxlen =0
n2 = int(input())
if n2 == -1:
    maxlen = 1
else:
    maxlen = 2
curlen = 2


n1 = int(input())
if n1 == -1:
    maxlen = 0
n2 = int(input())

if n2 == -1:
    maxlen = 1
else:
    maxlen = 2
curlen = 2

while True:

    n3 = int(input())
    if n3 == -1:
        break
    if n1 + n3 == 2*n2:
        curlen +=1
        if curlen > maxlen:
            maxlen = curlen
    else:
        curlen = 2
    n1 = n2
    n2 = n3
print(maxlen)
'''

length = 2
max_length = length
n1 = int(input())
n2 = int(input())

while True:
    n3 = int(input())
    if n3 == -1:
        break
    if n1 - n2 == n2 - n3:
        length += 1
        if length > max_length:
            max_length = length
    else:
        length = 2
    n1 = n2
    n2 = n3

print(max_length)
