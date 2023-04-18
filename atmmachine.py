class ATM:
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number

    def check_balance(self):
        print("Your balance is $5000.")

    def withdraw(self, amount):
        new_amount = 5000 - amount
        print("You have withdrawn "+str(amount) +". Your remaining balance is "+ str(new_amount))

def main():
    card_number = input("Insert your card number: ")
    pin_number = input("Enter your pin number: ")

    new_user =  ATM(card_number,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.Withdraw")
    activity = int(input("Enter activity number: "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("Enter the amount to withdraw: "))
        new_user.withdraw(amount)
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()
