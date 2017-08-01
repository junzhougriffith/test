##////////////////////// PROBLEM STATEMENT ////////////////////////////
## Write Python code which, given an integer grade, prints "Pass" if //
## the grade is greater than or equal to 50 but less than or equal   //
## to 100. If the grade is greater than or equal to 0 and less than  //
## 50 it prints "Failed" otherwise it prints "Illegal Grade".        //
##   -10 -> Illegal Grade                                            //
##   23 -> Failed                                                    //
##   50 -> Passed                                                    //
##   78 -> Passed                                                    //
##   128 -> Illegal Grade                                            //
##/////////////////////////////////////////////////////////////////////
grade = int(input())
if grade in range(50,101):
    print("Passed")
elif grade in range(0,50):
    print("Failed")
else:
    print("Illegal Grade")
