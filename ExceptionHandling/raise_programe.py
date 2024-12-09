class BalanceException(Exception):

    def checkBalance(self):
        self.money = 10000
        self.withdraw = 9000

        try:
            balance = self.money-self.withdraw
            if balance <= 20000:
                raise BalanceException("insufficient balance")
            print(balance)

        except BalanceException as be:
            print(be)
obj = BalanceException()
obj.checkBalance()
