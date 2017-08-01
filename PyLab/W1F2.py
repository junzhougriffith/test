##//////////////////// PROBLEM STATEMENT ///////////////////////
## Write a program that reads a filename and prints the       //
## percentage use of each letter in the file.                 //
##//////////////////////////////////////////////////////////////

fname = input()
fhand = open(fname)
di = dict()
for line in fhand:
    line = line.lower()
    for i in line:
       if 'a' <= i <= 'z':
           if i not in di:
               di[i] = 1
           else:
               di[i] += 1
t_value= sum(di.values())
for item in di:
    di[item] = 100*di[item] / t_value

di2 = sorted(di)
for i in di2:
    print('%s %.2f '%(i, di[i]))
