##/////////////// PROBLEM STATEMENT //////////////////
##  Checks a product code by ensuring that the code //
##  is at least 10 characters long and that         //
##  characters at indices 3 thru 7 are numeric.     //
##////////////////////////////////////////////////////
co = input()
if len(co) < 10:
    print('Improper code length:', co)
else:
    try:
        num = int(co[3:7])
        i = co.find('-')
        print(co[i-1], num)
    except:
        print('District is not numeric:', co)