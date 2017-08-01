##/////////////// PROBLEM STATEMENT /////////////////
## Convert a height input as centimetres to metres //
## and centimetres                                 //
##                                                 //
##  centimetres     metres centimetres             //
##      110      ->    1       10                  //
##     1256      ->   12       56                  //
##///////////////////////////////////////////////////
cm = int(input())
print(cm//100, cm%100)
