from colorama import Back,Fore,Style
import hashlib
print(Back.BLACK )
print(Style.BRIGHT )
print(Fore.MAGENTA )
class User:
    def _init_(self):
        self.name = ""
        self.username = ""
        self.password_hash = ""
        self.account_lock = False
        self.no_of_attempts = 3
        self.hundreds = 0
        self.two_hundreds = 0
        self.five_hundreds = 0
        self.two_thousands = 0
        self.balance = 0

    
    def get_string_hash(self, string):
        b_string = bytes(string,'UTF-8')
        sha256 = hashlib.sha256()
        sha256.update(b_string)
        return sha256.hexdigest()


    def show_menu(self):
        while True:
            self.choice = int(input("\n ..       WELCOME TO SWIZZZ BANK     ..\n\n\n\n\n\
             Menu: (choose item no. like 1 or 2) \n\n\n\n\n\
             PRESS 1 TO............CREATE NEW ACCOUNT                    \n\n\n\n\n\
             PRESS 2 FOR............CASH DEPOSIT                         \n\n\n\n\n\
             PRESS 3 FOR ..........CASH WITHDRAWAL                       \n\n\n\n\n\
             PRESS 4 TO........CHECK FOR BANK BALANCE                     \n\n\n\n\n\
             PRESS 5 IF.......YOU WANT THE BEST LOAN WITH LOW INTEREST OF ALL TIME\n\n\n\n\n\
             PRESS 6 IF.......YOU WANT TO EXIT BUT WE DON'T WANT YOU TO DO SO.... COME SOON WE WILL MISS YOU:(\n\n\n\n\n\
             Choice: "))
            print("\n----------------\n")

            if self.choice == 1:
                self.create_account()
            elif self.choice == 2:
                self.cash_deposit()
            elif self.choice == 3:
                self.cash_withdrawl()
            elif self.choice ==4:
                self.check_balance()
            elif self.choice == 5:
                amnt=int(input("enter loan amount"))
                self.loan_amount(amnt)
            elif self.choice == 6:
                print("Thanks you! Exiting . . .")
                break
            else:
                print("\nInvalid choice. Please enter correct choice again.")


    def set_password(self, password):
        self.password_hash = self.get_string_hash(password)


    def create_account(self):
        self.username = input("Enter username: ")
        self.set_password(input("Enter password: "))
        self.name = input("Enter your name: ")
        print("Account created successfully!")

    
    def login(self):
        if self.account_lock==True:
            print("Account has been locked after failed attempts!")
        else:
            userid = input("Enter username: ")
            password = input("Enter password: ")
            password_hash = self.get_string_hash(password)
            if self.username==userid and self.password_hash==password_hash:
                return True
            else:
                self.no_of_attempts -= 1
                print(f"Incorrect ID or Password! Attempt(s) left: {self.no_of_attempts}")
                if self.no_of_attempts == 0:
                    print("You have more than 3 failed attempts. Account has been locked.")
                    self.account_lock = True
        return False

    
    def cash_deposit(self):
        if self.login():
            deposit_amount = int(input("Enter deposit amount: "))
            if deposit_amount <= 300000:
                print("Enter denominations below:")
                self.hundreds += int(input("100: "))
                self.two_hundreds += int(input("200: "))
                self.five_hundreds += int(input("500: "))
                self.two_thousands += int(input("2000: "))
                self.balance += self.hundreds*100 + self.two_hundreds*200 + self.five_hundreds*500 + self.two_thousands*2000
                print("Amount has been added to your account!")
            else:
                print("Maximum deposit limit reached of 3 lakhs.Hence,Amount cannot be Credited........MAXIMUM LIMIT REACHED ._.")
   
    def cash_withdrawl(self):
        if self.login():
            withdrawl_amount = int(input("Enter withdrawl amount: "))
            if withdrawl_amount <= 30000:
                print("Enter denominations below:")
                self.hundreds -= int(input("100: "))
                self.two_hundreds -= int(input("200: "))
                self.five_hundreds -= int(input("500: "))
                self.two_thousands -= int(input("2000: "))
                self.balance -= (self.hundreds*100 + self.two_hundreds*200 + self.five_hundreds*500 + self.two_thousands*2000)- withdrawl_amount
                print("Amount has been debited from your account!")
            else:
                print("Cannot be debited.................MAXIMUM LIMIT REACHED!!! ._.")
                
    def check_balance(self):
        if self.login():
            print(f"Current Balance: {self.balance}")
            print("Denominations:")
            print(f"100: {self.hundreds}")
            print(f"200: {self.two_hundreds}")
            print(f"500: {self.five_hundreds}")
            print(f"2000: {self.two_thousands}")            
    

    def loan_amount(self, amnt):
        print("-" * 8)
        print("Select the Type of loan you need ")
        print("-" * 8)
        print("1 Education loan")
        print("-" * 8)
        print("2 Health loan")
        print("-" * 8)
        print("3 Car loan")
        print("-" * 8)
        print("4 Others")
        loan_type = int(input("Enter loan type: "))
        
        if loan_type == 1:
            interest_rate = 0.03
        elif loan_type == 2:
            interest_rate = 0.03
        elif loan_type == 3:
            interest_rate = 0.05
        else:
            interest_rate = 0.085

        interest_amount = amnt * interest_rate
        total_loan_amount = amnt + interest_amount

        if total_loan_amount <= (self.balance / 2):
            print("Your loan has been granted successfully.")
            self.balance -= total_loan_amount  # Deduct the loan amount from the balance
            print(f"Loan Amount: {amnt}")
            print(f"Interest Amount: {interest_amount}")
            print(f"Total Loan Amount: {total_loan_amount}")
            print(f"Updated Balance: {self.balance}")
        else:
            print("Increase your balance; the loan cannot be granted.")

class Admin:
    def _init_(self):
        self.name = ""
        self.username = "admin"
        self.pwd = "passw0rd"
        self.account_lock = False
        self.no_of_attempts = 3
        self.hundreds = 0
        self.two_hundreds = 0
        self.five_hundreds = 2
        self.two_thousands = 5
        self.balance = 11000

    
    def show_menu(self):
        while True:
            self.choice = int(input("\n###################\n\
Menu: (choose item no. like 1 or 2) \n\
1. Check total balance\n\
2. Cash deposit\n\
3. Notification\n\
4. Exit\n\n\
\
Choice: "))
            print("\n----------------\n")

            if self.choice == 1:
                self.total_balance()
            elif self.choice == 2:
                self.cash_deposit()
            elif self.choice == 3:
                pass
            elif self.choice == 4:
                print("Thanks you! Exiting . . .")
                break
            else:
                print("\nInvalid choice. Please enter correct choice again.")

    
    def login(self):
        if self.account_lock==True:
            print("Account has been locked after failed attempts!")
        else:
            userid = input("Enter username: ")
            password = input("Enter password: ")
            if self.username==userid and self.pwd==password:
                return True
            else:
                self.no_of_attempts -= 1
                print(f"Incorrect ID or Password! Attempt(s) left: {self.no_of_attempts}")
                if self.no_of_attempts == 0:
                    print("You have more than 3 failed attempts. Account has been locked.")
                    self.account_lock = True
        return False
        

    def total_balance(self):
        if self.login():
            print(f"Total balance = {self.balance}")
            print(f"Denominations:\n\
100 = {self.hundreds}\n\
200 = {self.two_hundreds}\n\
500 = {self.five_hundreds}\n\
2000 = {self.two_thousands}")


    def cash_deposit(self):
        if self.login():
            deposit_amount = int(input("Enter deposit amount: "))
            if deposit_amount <= 300000:
                print("Enter denominations below:")
                self.hundreds += int(input("100: "))
                self.two_hundreds += int(input("200: "))
                self.five_hundreds += int(input("500: "))
                self.two_thousands += int(input("2000: "))
                self.balance += self.hundreds*100 + self.two_hundreds*200 + self.five_hundreds*500 + self.two_thousands*2000
                print("Amount has been added to your account!")
            else:
                print("Maximum deposit limit reached of 3 lakhs.")


    def notification():
        pass


if __name__== "__main__":
    while True:
        choice = int(input("Are you a user or admin? (PRESS 1 FOR USER AND 2 FOR ADMIN): "))
        
        if choice == 1:
            # user
            user = User()
            user.show_menu()
            
        elif choice == 2:
            #admin
            admin = Admin()
            admin.show_menu()

        else:
            print("OH NO!!!!!!!!! IT'S AN UNDEFINED INPUT . EXITING.............:(")
            break