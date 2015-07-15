from nose.case import Test
from src.account import Account

__author__ = 'krzysztofduda'

@Test
class withdraw_funds():
    account = Account()
    print account.withdrawFunds(230,False)