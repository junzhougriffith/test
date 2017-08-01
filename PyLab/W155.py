##////////////////////// PROBLEM STATEMENT //////////////////////
## You are driving a little too fast, and a police officer     //
## stops you. Write code to compute the result, encoded as an  //
## int value: 0=no ticket, 1=small ticket, 2=big ticket. If    //
## speed is 60 or less, the result is 0. If speed is between   //
## 61 and 80 inclusive, the result is 1. If speed is 81 or     //
## more, the result is 2. Unless it is your birthday -- on     //
## that day, your speed can be 5 higher in all cases.          //
##                                                             //
##  Speed  Birthday  Result                                    //
##   60    False   ->   0                                      //
##   65    False   ->   1                                      //
##   65    True   ->    0                                      //
##///////////////////////////////////////////////////////////////
speed = int(input())
birthday = eval(input())
'''
if birthday == False:
    if speed <= 60:
        ticket_type = 0
    elif 61 <= speed <= 80:
        ticket_type = 1
    else:
        ticket_type = 2
else:
    if speed-5 <= 60:
        ticket_type = 0
    elif 61 <= (speed-5) <= 80:
        ticket_type = 1
    else:
        ticket_type = 2
print(ticket_type)
'''
bound_1 = 60
bound_2 = 80
if birthday == True:
    bound_1 += 5
    bound_2 += 5
if speed <= bound_1:
    ticket_type = 0
elif speed > bound_2:
    ticket_type = 2
else:
    ticket_type = 1
print(ticket_type)
