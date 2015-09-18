# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio.rest.base import Domain
from twilio.rest.v2010.account import AccountList


class V2010(Domain):

    def __init__(self, twilio):
        super(V2010, self).__init__(twilio)
        self._accounts = None

    @property
    def accounts(self):
        if self._accounts is None:
            self._accounts = AccountList(self)
        return self._accounts
