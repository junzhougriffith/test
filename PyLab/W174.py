##//////////////////////////// PROBLEM STATEMENT ///////////////////////////
## Write a program that reads temperatures in Celsius, converts them to   //
## Fahrenheit and then back to Celsius. The input is float numbers.       //
## Use functions for the conversions.                                     //
##//////////////////////////////////////////////////////////////////////////

def converts_ce_fa(x):
    return 9.0/5.0*x+32
cel_tem = float(input())
print(cel_tem, converts_ce_fa(cel_tem), cel_tem)
#print("%.1f = %.2f=%.1f"%(cel_tem, converts_ce_fa(cel_tem), cel_tem))
