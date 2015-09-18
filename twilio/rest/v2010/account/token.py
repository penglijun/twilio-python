# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class TokenList(ListResource):

    def __init__(self, domain, account_sid):
        super(TokenList, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'account_sid': account_sid,
        }
        self._uri = "/Accounts/{account_sid}/Tokens.json".format(**self._instance_kwargs)

    def create(self, ttl=values.unset):
        data = values.of({
            "Ttl": ttl,
        })
        
        return self._domain.create(
            TokenInstance,
            self._instance_kwargs,
            'POST',
            self._uri,
            data=data,
        )


class TokenContext(InstanceContext):

    def __init__(self, domain):
        super(TokenContext, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {}
        self._uri = "None".format(**self._instance_kwargs)


class TokenInstance(InstanceResource):

    def __init__(self, domain, payload, account_sid):
        super(TokenInstance, self).__init__(domain)
        
        # Marshaled Properties
        self._account_sid = payload['account_sid']
        self._date_created = deserialize.iso8601_datetime(payload['date_created'])
        self._date_updated = deserialize.iso8601_datetime(payload['date_updated'])
        self._ice_servers = payload['ice_servers']
        self._password = payload['password']
        self._ttl = payload['ttl']
        self._username = payload['username']
        
        # Context
        self._lazy_context = None
        self._context_account_sid = account_sid

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = TokenContext(
                self._domain,
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The unique sid that identifies this account """
        return self._account_sid

    @property
    def date_created(self):
        """ The date this resource was created """
        return self._date_created

    @property
    def date_updated(self):
        """ The date this resource was last updated """
        return self._date_updated

    @property
    def ice_servers(self):
        """ An array representing the ephemeral credentials """
        return self._ice_servers

    @property
    def password(self):
        """ The temporary password used for authenticating """
        return self._password

    @property
    def ttl(self):
        """ The duration in seconds the credentials are valid """
        return self._ttl

    @property
    def username(self):
        """ The temporary username that uniquely identifies a Token. """
        return self._username
