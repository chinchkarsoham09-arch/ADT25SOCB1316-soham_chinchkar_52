# STRATEGY CLASSES
class creditcard:
    def pay(self,amount):
        print("paid",amount,"using creditcard")

class UPI:
    def pay(self,amount):
        print("paid",amount,"using upi")

class cash:
    def pay(self,amount):
        print("paid",amount,"using cash")

#context class
class payment:
    def __init__(self,method):
        self.method=method
    def make_payment(self,amount):
        self.method.pay(amount)

#main program

amount=int(input("enter the amount:="))
print("1. credit card")
print("2. upi")
print("3.caash")

choice=int(input("enter the choice:="))
if choice==1:
    payment=payment(creditcard())
elif choice==2:
    payment=payment(UPI())
elif choice==3:
    payment=payment(cash())
else:
    print("invalid choice")
    exit()
payment.make_payment(amount)
