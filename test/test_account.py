import unittest

from src.account import Account, NoFundsAvailableException


class TestAccount(unittest.TestCase):

    def test_withdrawFunds_smallAmount_nativeClient(self):
        account = Account(1000)
        self.assertEquals(account.withdrawFunds(amount=100, native_client=True), [100])
    def test_withdrawFunds_bigAmount_nativeClient(self):
        account = Account(1000)
        self.assertEquals(account.withdrawFunds(amount=999, native_client=True), [200, 200, 200, 200, 100, 50, 20, 20])
    def test_withdrawFunds_mediumAmount_otherClient(self):
        account = Account(1000)
        self.assertEquals(account.withdrawFunds(amount=450, native_client=False), [200, 200, 50])
    def test_withdrawFunds_bigAmount_otherClient(self):
        account = Account(1000)
        self.assertRaises(NoFundsAvailableException, account.withdrawFunds, amount=999, native_client=False)