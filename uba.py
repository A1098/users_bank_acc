class BankAccount:
    BankName = "DojoOne"
    accounts=[]
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        print(f"{self} a Deposit of, {str(amount)}, was successfully processed!")
        print(f"Balance: {self.balance}")
        return self
    def withdraw(self, amount):
        if self.balance > 0:
            self.balance -= amount
            print("A withdraw of", amount, "was successfully processed")
            print("Your acount balance is", self.balance)
        else:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        return self
    def yield_interest(self):
        if self.balance > 0:
            int_pymt = self.int_rate * self.balance
            self.balance += int_pymt
            print(f"Your interest payment today will be {int_pymt} ")
            print(f"{self} has succesfully received interest payment")
            print("account balance:", self.balance)
            return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    @classmethod
    def all_accounts(cls):
        return cls.accounts

class User:
    bank_name = "First National Dojo"
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(int_rate= 0, balance=0)
    def make_deposit(self, amount):
        self.account += amount
        print(self.name, ", a Deposit of", str(amount), "was successfully processed!")
        print(self.name, ", your account balance is:", self.account)
    def make_withdrawal(self, amount):
        self.account -= amount
        if self.account <= 0:
            print(self.name, "Your account balance is:", self.account)
        else:
            print(self.name, "a withdrawal of", str(amount), "was successfully processed!")
            print("Your account balance is:", self.account)
    def display_user_balance(self):
        print(self.account)


Madrid = User("Fidel Madrid")
Ferrencini = User("Francesca Ferrencini")
Ion = User("John Ion")
Madrid.account.deposit(100)