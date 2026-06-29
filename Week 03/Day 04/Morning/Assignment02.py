#            =================  ATM Machine Simulation    ======================


# Design an ATM class with_pin (private), _ balance (private), and_owner (protected). Implement authenticate(pin), deposit(amt), withdraw(amt), and mini_statement() methods. Limit withdrawal to *20,000/transaction. Use @property for balance (read-only from outside).

# Hint: authenticate() should set an internal_authenticated flag; check it in withdraw/deposit



class ATM:
    def __init__(self, owner, pin=1234, balance=0):
        self.__pin = pin
        self.__balance = balance
        self._owner = owner
        self._authenticated = False

    def authenticate(self, pin):
        if pin == self.__pin:
            self._authenticated = True
            print("Access Allowed!")
        else:
            raise ValueError("Wrong PIN. Access Denied.")

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amt):
        if not self._authenticated:
            raise PermissionError("Authenticate first")

        if amt <= 0:
            raise ValueError("Invalid Amount")

        self.__balance += amt
        print(f"${amt} deposited successfully")

    def withdraw(self, amt):
        if not self._authenticated:
            raise PermissionError("Authenticate first")

        if amt > 20000:
            raise ValueError("Maximum withdrawal limit is $20,000")

        if amt > self.__balance:
            raise ValueError("Insufficient Balance")

        self.__balance -= amt

    def mini_statement(self):
        print(f"Owner: {self._owner}")
        print(f"Current Balance: ${self.__balance}")



acc1 = ATM("Tanish", 1234, 10000)

acc1.authenticate(1234)
acc1.deposit(5000)
acc1.withdraw(3000)
acc1.mini_statement()
print("Balance:", acc1.balance)
print()
#_______________________________________________________
acc2 = ATM("Ayush", 54263,1000)

acc2.authenticate(54263)
acc2.deposit(2)
acc2.withdraw(200)
acc2.mini_statement()
print("Balance:", acc2.balance)
print()