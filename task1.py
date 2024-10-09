#  Task 1: Define a class for a bank account with attributes for account number, balance, and owner name. Include methods for deposit, withdrawal, and transfer.
class BankAccount:
    def __init__(self,account_number,owner_name,balance=0):
        self.account_number= account_number
        self.owner_name = owner_name
        self.balance = balance

# deposit method
    def deposit(self,amount):
        if amount > 0:
            print(f"Deposited {amount} to {self.owner_name} account .New balance is {self.balance}.")
        else:
            print("Dear customer,Deposited must be positive ")
    
    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw {amount} from {self.owner_name} account.Nee balance is {self.balance}")
        elif amount > self.balance:
            print("sorry,insufficient amount for withdraw")
        else:
            print("withdraw amount must be positive")
    def transfer(self,amount,target_amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            target_amount.balance += amount
            print(f"Transfered {amount} from {self.owner_name} account to {target_amount.owner_name} amount")
            print(f"New balance for {self.owner_name} is {self.balance}")
            print(f"New balance for {target_amount.owner_name} is {target_amount.balance}")
        elif amount > self.balance:
            print("sorry,insufficient amount for transfer")
        else:
            print("transfer amount must be positive")

acc1= BankAccount("0900","Esha",1000)
acc2= BankAccount("1234","Sana",800)

acc1.deposit(200)
acc1.withdraw(150)
acc1.transfer(300,acc2)