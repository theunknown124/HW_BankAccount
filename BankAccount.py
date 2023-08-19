class BankAccount:

    def __int__(self, amount = 0.0):
        self.amount = amount

    def withdraw(self, withdrawAmount):
        if withdrawAmount > self.amount:
            raise ValueError("Error insufficient funds")
        else:
            self.amount -= withdrawAmount
            return "${:.2f}".format(self.amount)

    def deposit(self,depositAmount):
        self.amount += depositAmount
        return "${:.2f}".format(self.amount)

    def getBalance(self):
        balance = "{:,.2f}".format(self.amount)
        return "$" + balance


def main():
    startingAmount = float(input("Enter the starting amount: "))
    account = BankAccount()
    account.amount = startingAmount
    print("bank account:", account.getBalance())

    while True:
        print("Enter 1 to deposit")
        print("Enter 2 to withdraw")
        optionInput = int(input())

        if optionInput == 1:
            depositAmount = float(input("How much would you like to deposit? "))
            account.deposit(depositAmount)
            print("I will deposit ${:.2f} into your account".format(depositAmount))
            print("The balance is ", account.getBalance())

        elif optionInput == 2:
            withdrawAmount = float(input("how much would you like to withdraw? "))
            try:
                account.withdraw(withdrawAmount)
                print("I will withdraw ${:.2f} into your account".format(withdrawAmount))
                print("The balance is", account.getBalance())
            except ValueError as e:
                print(str(e))
                print("The balance is", account.getBalance())

        print()
        choice = input("Would you like to make another transaction? (y/n): ")
        print()
        if choice != "y":
            print("Bye!")
            break



if __name__ == '__main__':
    main()
