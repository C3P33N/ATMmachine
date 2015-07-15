from nose.case import Test
from src.account import Account

__author__ = 'krzysztofduda'

@Test
class withdraw_funds_native_client():
    account = Account()
    account.withdrawFunds(amount=0, native_client=True)
    account.withdrawFunds(amount=200, native_client=True)
    account.withdrawFunds(amount=750, native_client=True)