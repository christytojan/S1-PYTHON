class Bank:
  def __init__(self,acc_no,name,acc_type,balance):
    self.acc_no=acc_no
    self.name=name
    self.acc_type=acc_type
    self.balance=balance
    
  def deposit(self,amount):
    self.balance=self.balance+amount
    print("Amount deposit Successfull")
  def withdraw(self,amount):
    if amount<=self.balance:
      self.balance=self.balance-amount
      print("Amount withdrawn successfull")
    else:
      print("Insufficient balance")
  def display(self):
    print("Account number:",self.acc_no)
    print("Name:",self.name)
    print("Account Type:",self.acc_type)
    print("Account balance:",self.balance)            
    
b1=Bank(101,"Varsha","Savings",5000)
b1.display
b1.deposit(2000)
print("Balance after deposit:",b1.balance)
b1.withdraw(1000)
print("Balance after withdrawl:",b1.balance)    
