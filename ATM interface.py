class Customer:


    def __init__(self, name, balance):
        self.name = name
        self.balance =  balance

    def sysstart(self):
        w_input = str(input('What would you like to do? Type: bal, deposit, withdraw, or quit.'))
        if w_input == 'bal':
            ron.check_bal()
        elif w_input == 'deposit':
            ron.deposit()
        elif w_input == 'withdraw':
            ron.withdraw()
        elif w_input == 'quit':
            exit()

    def check_bal(self):
        print('Your balance is: ' + str(self.balance))
        while True:
            w_input = str(input('What would you like to do? Type: bal, deposit, withdraw, quit? '))
            if w_input == 'bal':
                ron.check_bal()
            elif w_input == 'deposit':
                ron.deposit()
            elif w_input == 'withdraw':
                ron.withdraw()
            elif w_input == 'quit':
                exit()

    def withdraw(self):
        while True:
                w_input = int(input('How much would you like to withdraw? '))
                self.balance = (self.balance - w_input)
                print(self.balance)
                w_input = str(input('What would you like to do? Type: bal, deposit, withdraw, quit? '))
                if w_input == 'bal':
                    ron.check_bal()
                elif w_input == 'deposit':
                    ron.deposit()
                elif w_input == 'quit':
                    exit()


    def deposit(self):
        while True:
            uinput = int(input('How much would you like to deposit? '))

            self.balance = int(self.balance + uinput)
            print(self.balance)
            next_input = str(input('What would you like to do next? Type: bal, deposit, withdraw, quit? '))
            if next_input == 'bal':
                ron.check_bal()
            elif next_input == 'deposit':
                ron.deposit()
            elif next_input == 'withdraw':
                ron.withdraw()
            elif next_input == 'quit':
                exit()

ron = Customer('ron', 1000)
jenny = Customer('jenny', 200)
tom = Customer('ron', 500)

tom.sysstart()

# The purpose of this project was to reinforce basic theories, by putting them into a practical application, and to solidify
# my understanding of OOP.
# The scope of this project, was to create an ATM user interface that has the ability to: Instantiate a new customer, give the user
# the ability to store/withdraw/view the balance, of a currency item.
# I learned what a static method is by accident, and how to bypass this error.
# I solidified my understanding of for, and while loops, and the appropriate application of them respectively.
# I solidified my understanding of using User input as a variable, in a function, and inside of a loop.
# I learned the exit() function.
# Through research on stackoverflow I learned how I could implement this application in real life using a database.
# I learned how to store, and add user input to the values stored in a text file.
# I plan to optimize the functions in the while loops, by using a new function, to follow the DRY principle.
# Bugs: Balance stays at 1000, even when using jenny to initiate program.; Maybe a type error between int, and str in the input fields.







