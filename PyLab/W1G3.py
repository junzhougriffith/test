##///////////////// PROBLEM STATEMENT //////////////////
## The problem statement is in file BankAccounts.pdf. //
##//////////////////////////////////////////////////////
account1 =  Account(1, 100.0)
savings1 =  SavingsAccount(2, 10000.0, 5.0)
cheque1 =  ChequeAccount(3, 1000.0, 100.0, 50.0)
print(str(account1.getAccountNumber()) + " " + str(account1.getBalance()))
if not account1.deposit(50.0):
  print(str(account1.getAccountNumber()) + ": Deposit Failed")
print(str(account1.getAccountNumber()) + " " + str(account1.getBalance()))
if not account1.withdraw(50.0):
  print(str(account1.getAccountNumber()) +": Withdrawal Failed")
print(str(account1.getAccountNumber()) + " " + str(account1.getBalance()))
print(str(savings1.getAccountNumber()) + " " + str(savings1.getBalance()))
if not savings1.deposit(50.0):
  print(str(savings1.getAccountNumber()) +": Deposit Failed")
print(str(savings1.getAccountNumber()) + " " + str(savings1.getBalance()))
if not savings1.withdraw(50.0):
  print(str(savings1.getAccountNumber()) +": Withdrawal Failed")
print(str(savings1.getAccountNumber()) + " " + str(savings1.getBalance()))
print(str(cheque1.getAccountNumber()) + " " + str(cheque1.getBalance()))
if not cheque1.deposit(50.0):
  print(str(cheque1.getAccountNumber()) +": Deposit Failed")
print(str(cheque1.getAccountNumber()) + " " + str(cheque1.getBalance()))
if not cheque1.withdraw(1000.0):
  print(str(cheque1.getAccountNumber()) +": Withdrawal Failed")
print(str(cheque1.getAccountNumber()) + " " + str(cheque1.getBalance()))
