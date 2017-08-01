##///////////////////// PROBLEM STATEMENT ////////////////////////
## Write a program that takes a score (0..100) as its input     //
## and returns a grade according to:                            //
##      <= 100 and >= 90 -> A                                   //
##      < 90 and >= 80 -> B                                     //
##      < 80 and >= 70 -> C                                     //
##      < 70 and >= 60 -> D                                     //
##      < 60 and >= 0 -> F                                      //
##      Outside these ranges gives an X                         //
## Use a function to calculate the grade.                       //
##////////////////////////////////////////////////////////////////


def grade_lev(x):
    if x not in range(0, 101):
        return 'X'
    elif x >= 90:
        return 'A'
    elif x >= 80:
        return 'B'
    elif x >= 70:
        return 'C'
    elif x >= 60:
        return 'D'
    else:
        return 'F'

score = int(input())
print(grade_lev(score))
