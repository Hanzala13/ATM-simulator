class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            print('Invalid deposit amount.')
            return False

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print('Insufficient funds.')
            return False

    def check_balance(self):
        print(f'Your current balance is ${self.balance:.2f}.')

def main():
    account = BankAccount()
    while True:
        print('Welcome to the ATM!')
        print('1. Check balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Quit')
        option = int(input('Enter your option (1-4): '))
        if option == 1:
            account.check_balance()
        elif option == 2:
            amount = float(input('Enter the deposit amount: '))
            if account.deposit(amount):
                print('Deposit successful.')
        elif option == 3:
            amount = float(input('Enter the withdrawal amount: '))
            if account.withdraw(amount):
                print('Withdrawal successful.')
        elif option == 4:
            break
        else:
            print('Invalid option. Please try again.')

if __name__ == '__main__':
    main()