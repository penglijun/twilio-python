# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class CountryList(ListResource):

    def __init__(self, domain):
        super(CountryList, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {}
        self._uri = "/PhoneNumbers/Countries".format(**self._instance_kwargs)

    def read(self, limit=None, page_size=None, **kwargs):
        limits = self._domain.read_limits(limit, page_size)
        
        params = values.of({})
        params.update(kwargs)
        
        return self._domain.read(
            self,
            CountryInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, page_token=None, page=None, page_size=None, **kwargs):
        params = values.of({})
        params.update(kwargs)
        
        return self._domain.page(
            self,
            CountryInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            params=params,
        )


class CountryContext(InstanceContext):

    def __init__(self, domain, iso_country):
        super(CountryContext, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'iso_country': iso_country,
        }
        self._uri = "/PhoneNumbers/Countries/{iso_country}".format(**self._instance_kwargs)

    def fetch(self):
        return self._domain.fetch(
            CountryInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
        )


class CountryInstance(InstanceResource):

    def __init__(self, domain, payload, iso_country=None):
        super(CountryInstance, self).__init__(domain)
        
        # Marshaled Properties
        self._country = payload['country']
        self._iso_country = payload['iso_country']
        self._url = payload['url']
        
        # Context
        self._lazy_context = None
        self._context_iso_country = iso_country or self._iso_country

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = CountryContext(
                self._domain,
                self._context_iso_country,
            )
        return self._lazy_context

    @property
    def country(self):
        """ The country """
        return self._country

    @property
    def iso_country(self):
        """ The iso_country """
        return self._iso_country

    @property
    def url(self):
        """ The url """
        return self._url

    def fetch(self):
        self._context.fetch()
