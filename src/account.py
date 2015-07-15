__author__ = 'krzysztofduda'


class NoFundsAvailableException(Exception):

    def __init__(self, *args, **kwargs):
        super(NoFundsAvailableException, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "No funds available at this time, sorry!"


class Account():

    def __init__(self):
        self.available_bills = (10, 20, 50, 100, 200)
        self.balance = 1000
        self.interest = 0.05

    def withdrawFunds(self, amount=None, native_client=None):
        received_bill = list()
        amount_with_interest = amount*self.interest
        for x in reversed(self.available_bills):
            if amount-x>=0 :
                received_bill.append(x)
                if native_client:
                    amount -= x
                else:
                    amount -= (x+amount_with_interest)
                    if amount <=0:
                        raise NoFundsAvailableException
                print amount_with_interest

        return received_bill

