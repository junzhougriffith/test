##//////////////////// PROBLEM STATEMENT ////////////////////////
## Write a program which reads two lists and prints two lists, //
## the first printed list contains all elements that are in    //
## both input lists while the second printed list contains all //
## elements that are in only one of the input lists.           //
##///////////////////////////////////////////////////////////////
n1 = int(input())
myList1 = []
for i in range(n1):
    myList1.append(int(input()))

n2 = int(input())
myList2 = []
for i in range(n2):
    myList2.append(int(input()))

s1 = set(myList1)
s2 = set(myList2)

inter_set = s1.intersection(s2)
union_set = s1.symmetric_difference(s2)

print(sorted(list(inter_set)))
print(sorted(list(union_set)))
