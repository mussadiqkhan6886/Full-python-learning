class Bank:
    def __init__(self):
        self._balance = 0
        
    @property
    def balance(self):
        return self._balance
    
    def withdraw(self, n):
        self._balance -= n
        
    def deposit(self, n):
        self._balance += n
        
def main():
    account = Bank()
    print("Balance: ", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance: ", account.balance)
    
main()
        