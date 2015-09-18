# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource


class SipContext(InstanceContext):

    def __init__(self, domain):
        super(SipContext, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {}
        self._uri = "None".format(**self._instance_kwargs)


class SipInstance(InstanceResource):

    def __init__(self, domain, payload, account_sid):
        super(SipInstance, self).__init__(domain)
        # Context
        self._lazy_context = None
        self._context_account_sid = account_sid

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = SipContext(
                self._domain,
            )
        return self._lazy_context
