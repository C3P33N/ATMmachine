__author__ = 'krzysztofduda'


class NoFundsAvailableException(Exception):
    def __init__(self, *args, **kwargs):
        super(NoFundsAvailableException, self).__init__(*args, **kwargs)
        self.amount = args[0]
        self.balance = args[1]

    def __repr__(self):
        return "No funds available at this time, sorry! Amount is %s, and account balance is %s." % (self.amount, self.balance)


class Account():
    def __init__(self, balance=None, interest=0.05):
        self.available_bills = (10, 20, 50, 100, 200)
        self.balance = balance
        self.interest = interest

    def withdrawFunds(self, amount=None, native_client=None):

        bills_from_atm = list()
        amount_with_interest = amount + amount * self.interest
        if amount_with_interest > self.balance and native_client==False:
            raise NoFundsAvailableException(amount_with_interest, self.balance)

        if not native_client:
            self.balance -= amount_with_interest

        self.balance -= amount

        for x in reversed(self.available_bills):
            while amount >= x:
                if amount - x >= 0:
                    bills_from_atm.append(x)
                    amount -= x

        if amount < 0 or self.balance < 0:
            raise NoFundsAvailableException(amount, self.balance)

        return bills_from_atm

