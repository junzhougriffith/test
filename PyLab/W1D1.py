##/////////////////////////////// PROBLEM STATEMENT ////////////////////////
##  Complete the following list comprehension problems                    //
##//////////////////////////////////////////////////////////////////////////
test_number = int(input())

# With the given list, write a program to print this list after removing
# all duplicate values with original order reserved.

if test_number == 1:
  li1 = [12,24,35,24,88,120,155,88,120,155]
  mylist1 = list()
  for i in range(len(li1)):
    if li1[i] not in mylist1:
      mylist1.append(li1[i])
  print(mylist1)
# With two given lists write a program to make a list whose elements are
# intersection of the given lists.

if test_number == 2:
  li2 = [1,3,6,78,35,55]
  li3 = [12,24,35,24,88,120,155]
  mylist2 = list()
  for item in li2:
    if item in li3:
      mylist2.append(item)
  print(mylist2)
# By using list comprehension, write a program to print the list after
# removing the value 24.

if test_number == 3:
  li4 = [12,24,35,24,88,120,155]
  mylist3 = list()
  for item in li4:
    if item != 24:
      mylist3.append(item)
  print(mylist3)
# By using list comprehension, please write a program to print the list
# after removing the 0th,4th,5th numbers in the list.

if test_number == 4:
  li5 = [12,24,35,70,88,120,155]
  mylist4 = list()
  for i in range(len(li5)):
    if i != 0 and i != 4 and i != 5:
      mylist4.append(li5[i])
  print(mylist4)
# By using list comprehension, please write a program to print the list
# after removing numbers which are divisible by 5 and 7.

if test_number == 5:
  li6 = [12,24,35,70,88,120,155]
  mylist5 = list()
  for i in range(len(li6)):
    if li6[i] % 5 != 0 and li6[i] % 7 != 0:
      mylist5.append(li6[i])
  print(mylist5)