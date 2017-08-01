##//////////////////////////// PROBLEM STATEMENT /////////////////////////////
## Write a Python program that, given a cost of an item (less than or equal //
## to one dollar), gives the number of 50 cent, 20 cent, 10 cent, 5 cent    //
## and 1 cent coins the buyer would receive if they handed over one dollar. //
## You must minimise the number of coins in the change.                     //
##////////////////////////////////////////////////////////////////////////////
icost = int(input())
change = 100 - icost
n50 = change // 50
change = change % 50
n20 = change // 20
change = change % 20
n10 = change // 10
change = change % 10
n5 = change // 5
n1 = change % 5
print(n50, n20, n10, n5, n1)
