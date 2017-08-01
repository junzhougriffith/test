##/////////////////// PROBLEM STATEMENT /////////////////////////
## Given a 12 hour time of day as hours minutes seconds pm,    //
## add a time interval which is specified as hours minutes     //
## seconds. The input pm is 0 for morning and 1 afternoon.     //
##                                                             //
##   hrs mins secs am/pm  hrs mins secs    hrs mins secs am/pm //
##    1   24   30    1     2   40   40  ->  4   5    10    1   //
##///////////////////////////////////////////////////////////////
h1=int(input())
m1=int(input())
s1=int(input())
ap=int(input())
h2=int(input())
m2=int(input())
s2=int(input())

h1=h1+12*ap
s3=(s1+s2)%60
m3=((s1+s2)//60+m1+m2)%60
h3=((s1+s2)//60+m1+m2)//60+h1+h2
h3=h3%24
if h3 > 12:
    ap =1
else:
    ap = 0
#ap=h3//12
h3=h3%12

print(h3,m3,s3,ap)
