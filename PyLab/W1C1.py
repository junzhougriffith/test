##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## The following code deliberately causes different exceptions. Do not fix   //
## the actual problems but implement try/except blocks to explicitly handle  //
## each exception and print out each exception handled and a message         //
## Note that the line number of the exception can be found in:               //
##     sys.exc_info()[-1].tb_lineno   (you need to import module sys)        //
##/////////////////////////////////////////////////////////////////////////////
'''
import sys
n = 0
#refer to http://stackoverflow.com/questions/14519177/python-exception-handling-line-number

try:
    n = int(input())



    try:
        k = 1 / n
    except:

        print('Exception: Divide by zero at line %d' % sys.exc_info()[-1].tb_lineno)
    s1 = "abcdef"
    try:
        c = s1[n]
    except:
        print('Exception: Invalid index at line %d' % sys.exc_info()[-1].tb_lineno)
except:
    print('Exception: Input mismatch at line %d' % sys.exc_info()[-1].tb_lineno)
'''

import sys
s1 = "abcdef"

try:
    n = int(input())
except:
    n = -1
    print("Exception: Input mismatch at line 13")

try:
    k = 1 / n
except:
    print("Exception: Divide by zero at line 18")

try:
    c = s1[n]
except:
    print("Exception: Invalid index at line 24")