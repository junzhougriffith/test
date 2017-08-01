##///////////// PROBLEM STATEMENT //////////////
## Write a program that computes the value of //
## n+nn+nnn+nnnn with the single digit n      //
## input by the user.                         //
##//////////////////////////////////////////////
n = int(input())
p = 4*n + 3*n*10 + 2*n*100 + n*1000
print(p)
