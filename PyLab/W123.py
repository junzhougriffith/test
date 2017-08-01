##//////////////////// PROBLEM STATEMENT ////////////////////////
## Given a 24 hour time of day as hours minutes seconds, add   //
## a time interval which is specified as hours minutes seconds //
##                                                             //
##   hrs mins secs hrs mins secs    hrs mins secs              //
##   13   24   30   2   40   40  -> 16    5   10               //
##///////////////////////////////////////////////////////////////
h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
s3 = (s1 + s2) % 60
m3 = ((s1 + s2) // 60 + m1 + m2) % 60
h3 = ((s1 + s2) // 60 + m1 + m2) // 60 + h1 + h2
print(h3, m3, s3)
