##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Create a Ship class then CruiseShip and CargoShip classes that extend the //
## Ship class. They should have the following members:                       //
##   - A field for the number of passengers (CruiseShip).                    //
##   - A field for the cargo capacity in tonnage (CargoShip).                //
##   - A __str__ function that extends the __str__ function in the base class//
##/////////////////////////////////////////////////////////////////////////////

ships = []
class Ship:
  def __init__(self, shipname, ye):
    self.name = shipname
    self.year = ye

  def __str__(self):
    return  ('%s, %d')%(self.name, self.year)

class CruiseShip(Ship):
  def __init__(self, shipname,ye,n3):
    self.__init__(self, shipname,ye)
    self.n_p = n3

  def __str__(self):
    return self.__str__() + str(self.n_p)

class CargoShip(Ship):
  def __init__(self, shipname,ye, ca):
    self.__init__(self, shipname,ye)
    self.capacity = ca

  def __str__(self):
    return self.__str__() + str(self.capacity)


## Assign Ship objects to the list elements.
ships.append(Ship("Lolipop", "1960"))
ships.append(CruiseShip("Disney Magic", "1998", 2400))
ships.append(CargoShip("Black Pearl", "1800", 50000))

for ship in ships:
  print(ship)
