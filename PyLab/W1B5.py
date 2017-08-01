##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## A website requires the users to input username and password to            //
## register. Write a program to check the validity of password input by      //
## users. Following are the criteria for checking the password: 1. At least  //
## 1 letter between [a-z] 2. At least 1 number between [0-9] 1. At least 1   //
## letter between [A-Z] 3. At least 1 character from [0@] 4. Minimum        //
## length of transaction password: 6 5. Maximum length of transaction        //
## password: 12 Your program should accept a sequence of colon separated     //
## passwords and will check them according to the above criteria. Passwords  //
## that match the criteria are to be printed, each separated by a comma.     //
## Example If the following passwords are given as input to the program:     //
## ABd1234@1:a F1#:2w3E*:2We3345 Then, the output of the program should be:  //
## ABd1234@1                                                                 //
##/////////////////////////////////////////////////////////////////////////////

## 1. At least 1 letter between [a-z]
def check_lower_case(cand_password):
    for ch in cand_password:
        if "a" <= ch and ch <= "z":
            return True
    return False
## 2. At least 1 letter between [A-Z]
def check_upper_case(cand_password):
    for ch in cand_password:
        if "A" <= ch and ch <= "Z":
            return True
    return False
## 3. At least 1 number between [0-9]
def check_digits(cand_password):
    for ch in cand_password:
        if "0" <= ch and ch <= "9":
            return True
    return False
## 4. Minimum length of transaction password: 6, Maximum length of transaction password: 12
def check_length(cand_password):
    return len(cand_password) >= 6 and len(cand_password) <= 12
## check candidate password
def check_cand_password(cand_password):
    return check_lower_case(cand_password) and check_upper_case(cand_password) and check_digits(cand_password) and check_length(cand_password)
############################################################################33
s = input()
while(len(s) > 0):
    colon_loc = s.find(':')
    if colon_loc == -1:
        break
    cand_password = s[:colon_loc]
    s = s[colon_loc+1:len(s)]
    if check_cand_password(cand_password):
        print(cand_password)

