# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest import serialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class MediaList(ListResource):

    def __init__(self, domain, account_sid, message_sid):
        super(MediaList, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'account_sid': account_sid,
            'message_sid': message_sid,
        }
        self._uri = "/Accounts/{account_sid}/Messages/{message_sid}/Media.json".format(**self._instance_kwargs)

    def read(self, date_created=values.unset, limit=None, page_size=None, **kwargs):
        limits = self._domain.read_limits(limit, page_size)
        
        params = values.of({
            "DateCreated": serialize.iso8601_date(date_created),
        })
        params.update(kwargs)
        
        return self._domain.read(
            self,
            MediaInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, date_created=values.unset, page_token=None, page=None,
             page_size=None, **kwargs):
        params = values.of({})
        params.update(kwargs)
        
        return self._domain.page(
            self,
            MediaInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            params=params,
        )


class MediaContext(InstanceContext):

    def __init__(self, domain, account_sid, message_sid, sid):
        super(MediaContext, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'account_sid': account_sid,
            'message_sid': message_sid,
            'sid': sid,
        }
        self._uri = "/Accounts/{account_sid}/Messages/{message_sid}/Media/{sid}.json".format(**self._instance_kwargs)

    def delete(self):
        return self._domain.delete("delete", self._uri)

    def fetch(self):
        return self._domain.fetch(
            MediaInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
        )


class MediaInstance(InstanceResource):

    def __init__(self, domain, payload, account_sid, message_sid, sid=None):
        super(MediaInstance, self).__init__(domain)
        
        # Marshaled Properties
        self._account_sid = payload['account_sid']
        self._content_type = payload['content_type']
        self._date_created = deserialize.iso8601_datetime(payload['date_created'])
        self._date_updated = deserialize.iso8601_datetime(payload['date_updated'])
        self._parent_sid = payload['parent_sid']
        self._sid = payload['sid']
        self._uri = payload['uri']
        
        # Context
        self._lazy_context = None
        self._context_account_sid = account_sid
        self._context_message_sid = message_sid
        self._context_sid = sid or self._sid

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = MediaContext(
                self._domain,
                self._context_account_sid,
                self._context_message_sid,
                self._context_sid,
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The unique sid that identifies this account """
        return self._account_sid

    @property
    def content_type(self):
        """ The default mime-type of the media """
        return self._content_type

    @property
    def date_created(self):
        """ The date this resource was created """
        return self._date_created

    @property
    def date_updated(self):
        """ The date this resource was last updated """
        return self._date_updated

    @property
    def parent_sid(self):
        """ The unique id of the resource that created the media. """
        return self._parent_sid

    @property
    def sid(self):
        """ A string that uniquely identifies this media """
        return self._sid

    @property
    def uri(self):
        """ The URI for this resource """
        return self._uri

    def delete(self):
        self._context.delete()

    def fetch(self):
        self._context.fetch()
