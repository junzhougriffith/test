##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Print True if the string "cat" and "dog" appear the same number of times  //
## in the given string. Do not use the Python count function.                //
##   "catdog" -> True                                                        //
##   "catcat" -> False                                                       //
##   "1cat1cadodog" -> True                                                  //
##/////////////////////////////////////////////////////////////////////////////

'''
s = input()

if s.count('cat') == s.count('dog'):
    res = True
else:
    res = False

print(res)
'''

s = input()

i = 0
num_cat = 0
num_dog = 0
while i+3 <= len(s):
     if s[i : i + 3] == 'cat':
         num_cat += 1
     if s[i : i + 3] == 'dog':   #not include wright value
         num_dog +=1
     i += 1

print(num_cat == num_dog)