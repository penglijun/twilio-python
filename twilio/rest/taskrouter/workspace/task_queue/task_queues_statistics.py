# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import serialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class StatisticsList(ListResource):

    def __init__(self, domain, workspace_sid):
        super(StatisticsList, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'workspace_sid': workspace_sid,
        }
        self._uri = "/Workspaces/{workspace_sid}/TaskQueues/Statistics".format(**self._instance_kwargs)

    def read(self, end_date=values.unset, friendly_name=values.unset,
             minutes=values.unset, start_date=values.unset, limit=None,
             page_size=None, **kwargs):
        limits = self._domain.read_limits(limit, page_size)
        
        params = values.of({
            "EndDate": serialize.iso8601_date(end_date),
            "FriendlyName": friendly_name,
            "Minutes": minutes,
            "StartDate": serialize.iso8601_date(start_date),
        })
        params.update(kwargs)
        
        return self._domain.read(
            self,
            StatisticsInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, end_date=values.unset, friendly_name=values.unset,
             minutes=values.unset, start_date=values.unset, page_token=None,
             page=None, page_size=None, **kwargs):
        params = values.of({
            "EndDate": serialize.iso8601_date(end_date),
            "FriendlyName": friendly_name,
            "Minutes": minutes,
        })
        params.update(kwargs)
        
        return self._domain.page(
            self,
            StatisticsInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            params=params,
        )


class StatisticsContext(InstanceContext):

    def __init__(self, domain):
        super(StatisticsContext, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {}
        self._uri = "None".format(**self._instance_kwargs)


class StatisticsInstance(InstanceResource):

    def __init__(self, domain, payload, workspace_sid):
        super(StatisticsInstance, self).__init__(domain)
        
        # Marshaled Properties
        self._account_sid = payload['account_sid']
        self._cumulative = payload['cumulative']
        self._realtime = payload['realtime']
        self._task_queue_sid = payload['task_queue_sid']
        self._worker_sid = payload['worker_sid']
        self._workspace_sid = payload['workspace_sid']
        
        # Context
        self._lazy_context = None
        self._context_workspace_sid = workspace_sid

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = StatisticsContext(
                self._domain,
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._account_sid

    @property
    def cumulative(self):
        """ The cumulative """
        return self._cumulative

    @property
    def realtime(self):
        """ The realtime """
        return self._realtime

    @property
    def task_queue_sid(self):
        """ The task_queue_sid """
        return self._task_queue_sid

    @property
    def worker_sid(self):
        """ The worker_sid """
        return self._worker_sid

    @property
    def workspace_sid(self):
        """ The workspace_sid """
        return self._workspace_sid
