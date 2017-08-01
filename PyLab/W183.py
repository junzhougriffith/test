##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Write a program to solve a classic ancient Chinese puzzle: We count 35    //
## heads and 94 legs among the chickens and rabbits in a farm. How many      //
## rabbits and how many chickens do we have?                                 //
##/////////////////////////////////////////////////////////////////////////////

for num_rabbits in range(1, 36):
       if num_rabbits * 4 + (35 - num_rabbits) * 2 == 94:
              print(num_rabbits, 35 - num_rabbits)
