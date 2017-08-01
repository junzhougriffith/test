##//////////////////////////// PROBLEM STATEMENT ////////////////////////////
## Write a program that reads from a file whose title(file name) is input from  //
## the keyboard. The file contains one integer per line and the program    //
## finds the average of the integers (add all integers and divide by the   //
## number of integers read). Note that the file may contain invalid        //
## integers (e.g. 123AB45) and these must be handled by using exceptions.  //
##///////////////////////////////////////////////////////////////////////////

fname = input()
fhand = open(fname)
num_int = 0
sum =0

for line in fhand:
    try:
        i = int(line)
        num_int += 1
        sum += i
    except:
        continue

print(sum/num_int)