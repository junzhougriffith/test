##////////////////////////////////////// PROBLEM STATEMENT /////////////////////////////////////////
## The following main function asks the user for details for a bank account and creates an        //
## instance of a BankAccount class. The main function calls the constructor of BankAccount        //
## to initialise values and also uses get accessor functions to print out the BankAccount details.//
## Create and complete the BankAccount class so that the file compiles and runs.                  //
##//////////////////////////////////////////////////////////////////////////////////////////////////

class BankAccount:

    def __init__(self, at1, at2, at3, at4):
        self.accountNumber = at1
        self.firstname = at2
        self.surname = at3
        self.balance = at4

    def getAccountNumber(self):
        return self.accountNumber

    def getFirstname(self):
        return self.firstname

    def getLastname(self):
        return self.surname

    def getBalance(self):
        return self.balance





accountNumber = int(input())
firstname = input()
surname = input()
balance = float(input())

b = BankAccount(accountNumber, firstname, surname, balance)

print(str(b.getAccountNumber()) + ", " + b.getFirstname() + ", " +
          b.getLastname() + ", " + str(b.getBalance()))
