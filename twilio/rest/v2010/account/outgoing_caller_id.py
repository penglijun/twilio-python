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


class OutgoingCallerIdList(ListResource):

    def __init__(self, domain, account_sid):
        super(OutgoingCallerIdList, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'account_sid': account_sid,
        }
        self._uri = "/Accounts/{account_sid}/OutgoingCallerIds.json".format(**self._instance_kwargs)

    def read(self, phone_number=values.unset, friendly_name=values.unset,
             limit=None, page_size=None, **kwargs):
        limits = self._domain.read_limits(limit, page_size)
        
        params = values.of({
            "PhoneNumber": phone_number,
            "FriendlyName": friendly_name,
        })
        params.update(kwargs)
        
        return self._domain.read(
            self,
            OutgoingCallerIdInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, phone_number=values.unset, friendly_name=values.unset,
             page_token=None, page=None, page_size=None, **kwargs):
        params = values.of({
            "PhoneNumber": phone_number,
        })
        params.update(kwargs)
        
        return self._domain.page(
            self,
            OutgoingCallerIdInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def create(self, phone_number, friendly_name=values.unset,
               call_delay=values.unset, extension=values.unset,
               status_callback=values.unset, status_callback_method=values.unset):
        data = values.of({
            "PhoneNumber": phone_number,
            "FriendlyName": friendly_name,
            "CallDelay": call_delay,
            "Extension": extension,
            "StatusCallback": status_callback,
            "StatusCallbackMethod": status_callback_method,
        })
        
        return self._domain.create(
            OutgoingCallerIdInstance,
            self._instance_kwargs,
            'POST',
            self._uri,
            data=data,
        )


class OutgoingCallerIdContext(InstanceContext):

    def __init__(self, domain, account_sid, sid):
        super(OutgoingCallerIdContext, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = "/Accounts/{account_sid}/OutgoingCallerIds/{sid}.json".format(**self._instance_kwargs)

    def fetch(self):
        return self._domain.fetch(
            OutgoingCallerIdInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
        )

    def update(self, friendly_name=values.unset):
        data = values.of({
            "FriendlyName": friendly_name,
        })
        
        return self._domain.update(
            OutgoingCallerIdInstance,
            self._instance_kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def delete(self):
        return self._domain.delete("delete", self._uri)


class OutgoingCallerIdInstance(InstanceResource):

    def __init__(self, domain, payload, account_sid, sid=None):
        super(OutgoingCallerIdInstance, self).__init__(domain)
        
        # Marshaled Properties
        self._account_sid = payload['account_sid']
        self._call_sid = payload['call_sid']
        self._date_created = deserialize.iso8601_datetime(payload['date_created'])
        self._date_updated = deserialize.iso8601_datetime(payload['date_updated'])
        self._friendly_name = payload['friendly_name']
        self._phone_number = payload['phone_number']
        self._sid = payload['sid']
        self._uri = payload['uri']
        self._validation_code = payload['validation_code']
        
        # Context
        self._lazy_context = None
        self._context_account_sid = account_sid
        self._context_sid = sid or self._sid

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = OutgoingCallerIdContext(
                self._domain,
                self._context_account_sid,
                self._context_sid,
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The unique sid that identifies this account """
        return self._account_sid

    @property
    def call_sid(self):
        """ The call_sid """
        return self._call_sid

    @property
    def date_created(self):
        """ The date this resource was created """
        return self._date_created

    @property
    def date_updated(self):
        """ The date this resource was last updated """
        return self._date_updated

    @property
    def friendly_name(self):
        """ A human readable description for this resource """
        return self._friendly_name

    @property
    def phone_number(self):
        """ The incoming phone number """
        return self._phone_number

    @property
    def sid(self):
        """ A string that uniquely identifies this outgoing-caller-ids """
        return self._sid

    @property
    def uri(self):
        """ The URI for this resource """
        return self._uri

    @property
    def validation_code(self):
        """ The validation_code """
        return self._validation_code

    def fetch(self):
        self._context.fetch()

    def update(self, friendly_name=values.unset):
        self._context.update(
            friendly_name=friendly_name,
        )

    def delete(self):
        self._context.delete()
