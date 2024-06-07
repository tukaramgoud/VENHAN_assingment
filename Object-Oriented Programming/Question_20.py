"""20. Write a class `BankAccount` with the following:
*Attributes: account_number, account_holder, balance
*Methods:
*`__init__(self, account_number: str, account_holder: str, balance: float = 0.0)`:
Constructor to initialize the attributes.
*`deposit(self, amount: float) -> None`: Method to deposit money into the account.
*`withdraw(self, amount: float) -> bool`: Method to withdraw money from the account. It
should return True if the withdrawal was successful, and False if there were insufficient
funds.
*`get_balance(self) -> float`: Method to return the current balance.
"""


class BankAccount():
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder 
        self.balance = balance 

    def deposit(self, amount):
        self.balance = amount + self.balance
        return self.balance
    
    def withdraw(self, amount):
        self.balance = self.balance - amount 
        return self.balance
    
    def get_balance(self):
        return "The current Balance is {}".format(self.balance)
    
bank_1 = BankAccount('123456789', "TukaramGoud" ,200.0)
(bank_1.deposit(300))
(bank_1.deposit(500))
(bank_1.withdraw(100))
print(bank_1.get_balance())