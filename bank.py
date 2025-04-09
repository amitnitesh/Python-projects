
class Atm:
    def __init__(self):
        self.pin=""
        self.balance=0
        self.main()

    def main(self):
        user=int(input("""How Would I assist You
              1. Enter 1 to create pin
              2. Enter 2 to deposite 
              3. Enter 3 to withdraw
              4. Enter 4 to check balance
              5. Enter 5 to exit""")

                   )
        if user==1:
            self.create_pin()
        elif user==2:
            self.deposite()
        elif user==3:
            self.withdraw()
        elif user==4:
            self.check_balance()
        else:
            self.exit()

    def create_pin(self):
        user=input("Enter the pin")
        print("Pin successfully set")
        self.pin=user
        

    def  deposite(self):
        user=input("Enter your pin")
        if user==self.pin:
            balance=int(input("Enter the amount to deposite"))
            self.balance=self.balance+balance
            print("Amount deposite successfully")
        else:
            print("Invalid pin")
        

    def withdraw(self):
        user = input("Enter your pin")
        if user == self.pin:
            balance=int(input("Enter the amount for withdraw"))
            if  balance<self.balance:
                self.balance=self.balance-balance
                print("Withdraw successfully")
            else:
                print("Insufficient funds")
            self.main()
        else:
            print("Invalid pin")
        

    def check_balance(self):
        user = input("Enter your pin")
        if user == self.pin:
            print(self.balance)
            self.main()
        else:
            print("Invalid pin")
        

    def exit(self):
        print("Bye")
