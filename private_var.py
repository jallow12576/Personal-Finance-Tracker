class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def deposit(self, amount):
        self.__balance += amount
        
    def get_amount(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_amount())