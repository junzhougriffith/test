##////////////////////// PROBLEM STATEMENT ///////////////////////
## Write a program that reads a filename and prints the number  //
## of non-empty lines and the number of words in the file.      //
##////////////////////////////////////////////////////////////////

fname = input()

try:
    fhand = open(fname)
except:
    print("Invalid file name")

count_line = 0
count_words = 0
for line in fhand:
    line = line.rstrip()
    count_line = count_line + 1
    words = line.split()
    count_words += len(words)
print(count_line,count_words)
