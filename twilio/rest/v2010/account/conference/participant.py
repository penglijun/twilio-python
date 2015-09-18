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


class ParticipantList(ListResource):

    def __init__(self, domain, account_sid, conference_sid):
        super(ParticipantList, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'account_sid': account_sid,
            'conference_sid': conference_sid,
        }
        self._uri = "/Accounts/{account_sid}/Conferences/{conference_sid}/Participants.json".format(**self._instance_kwargs)

    def read(self, muted=values.unset, limit=None, page_size=None, **kwargs):
        limits = self._domain.read_limits(limit, page_size)
        
        params = values.of({
            "Muted": muted,
        })
        params.update(kwargs)
        
        return self._domain.read(
            self,
            ParticipantInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, muted=values.unset, page_token=None, page=None, page_size=None,
             **kwargs):
        params = values.of({})
        params.update(kwargs)
        
        return self._domain.page(
            self,
            ParticipantInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            params=params,
        )


class ParticipantContext(InstanceContext):

    def __init__(self, domain, account_sid, conference_sid, call_sid):
        super(ParticipantContext, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'account_sid': account_sid,
            'conference_sid': conference_sid,
            'call_sid': call_sid,
        }
        self._uri = "/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid}.json".format(**self._instance_kwargs)

    def fetch(self):
        return self._domain.fetch(
            ParticipantInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
        )

    def update(self, muted):
        data = values.of({
            "Muted": muted,
        })
        
        return self._domain.update(
            ParticipantInstance,
            self._instance_kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def delete(self):
        return self._domain.delete("delete", self._uri)


class ParticipantInstance(InstanceResource):

    def __init__(self, domain, payload, account_sid, conference_sid, call_sid=None):
        super(ParticipantInstance, self).__init__(domain)
        
        # Marshaled Properties
        self._account_sid = payload['account_sid']
        self._call_sid = payload['call_sid']
        self._conference_sid = payload['conference_sid']
        self._date_created = deserialize.iso8601_datetime(payload['date_created'])
        self._date_updated = deserialize.iso8601_datetime(payload['date_updated'])
        self._end_conference_on_exit = payload['end_conference_on_exit']
        self._muted = payload['muted']
        self._parent_sid = payload['parent_sid']
        self._sid = payload['sid']
        self._start_conference_on_enter = payload['start_conference_on_enter']
        self._uri = payload['uri']
        
        # Context
        self._lazy_context = None
        self._context_account_sid = account_sid
        self._context_conference_sid = conference_sid
        self._context_call_sid = call_sid or self._call_sid

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = ParticipantContext(
                self._domain,
                self._context_account_sid,
                self._context_conference_sid,
                self._context_call_sid,
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The unique sid that identifies this account """
        return self._account_sid

    @property
    def call_sid(self):
        """ A string that uniquely identifies this call """
        return self._call_sid

    @property
    def conference_sid(self):
        """ A string that uniquely identifies this conference """
        return self._conference_sid

    @property
    def date_created(self):
        """ The date this resource was created """
        return self._date_created

    @property
    def date_updated(self):
        """ The date this resource was last updated """
        return self._date_updated

    @property
    def end_conference_on_exit(self):
        """ Indicates if the endConferenceOnExit was set """
        return self._end_conference_on_exit

    @property
    def muted(self):
        """ Indicates if the participant is muted """
        return self._muted

    @property
    def parent_sid(self):
        """ The parent_sid """
        return self._parent_sid

    @property
    def sid(self):
        """ The sid """
        return self._sid

    @property
    def start_conference_on_enter(self):
        """ Indicates if the startConferenceOnEnter attribute was set """
        return self._start_conference_on_enter

    @property
    def uri(self):
        """ The URI for this resource """
        return self._uri

    def fetch(self):
        self._context.fetch()

    def update(self, muted):
        self._context.update(
            muted,
        )

    def delete(self):
        self._context.delete()
