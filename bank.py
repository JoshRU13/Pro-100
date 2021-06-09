class atm:
    def __init__(self,card,pin):
        self.card=card
        self.pin=pin
    def checkbalance(self):
        print("Your balance is 50000")
    def withdrawl(self,amount):
        newamount = 50000-amount
        print(newamount)
def main():
    card = input("Enter your card number")
    pin = input("Enter your pin number")
    newuser = atm(card,pin)
    print("Choose your activity")
    print("1 Balance inquiry")
    print("2 Witdrawl")
    activity = int(input("Enter activity number"))
    if(activity==1):
        newuser.checkbalance()
    elif (activity==2):
        amount=int(input("Enter the amount"))
        newuser.withdrawl(amount)
if __name__=="__main__":
    main()

