class account:
    def __init__(self):
        self.balance = 0
        self.withdrawal_amount = 0
    def getinf(self):
        self.balance, self.withdrawal_amount = map(int, input().split())
    def withdrawal(self):
        if self.withdrawal_amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance = self.balance - self.withdrawal_amount
            print(self.balance)
x = account()
x.getinf()
x.withdrawal()