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


class StatisticsContext(InstanceContext):

    def __init__(self, domain, workspace_sid):
        super(StatisticsContext, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'workspace_sid': workspace_sid,
        }
        self._uri = "/Workspaces/{workspace_sid}/Workers/Statistics".format(**self._instance_kwargs)

    def fetch(self, minutes=values.unset, start_date=values.unset,
              end_date=values.unset, task_queue_sid=values.unset,
              task_queue_name=values.unset, friendly_name=values.unset):
        return self._domain.fetch(
            StatisticsInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
        )


class StatisticsInstance(InstanceResource):

    def __init__(self, domain, payload, workspace_sid=None):
        super(StatisticsInstance, self).__init__(domain)
        
        # Marshaled Properties
        self._account_sid = payload['account_sid']
        self._cumulative = payload['cumulative']
        self._realtime = payload['realtime']
        self._workspace_sid = payload['workspace_sid']
        
        # Context
        self._lazy_context = None
        self._context_workspace_sid = workspace_sid or self._workspace_sid

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = StatisticsContext(
                self._domain,
                self._context_workspace_sid,
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
    def workspace_sid(self):
        """ The workspace_sid """
        return self._workspace_sid

    def fetch(self, minutes=values.unset, start_date=values.unset,
              end_date=values.unset, task_queue_sid=values.unset,
              task_queue_name=values.unset, friendly_name=values.unset):
        self._context.fetch(
            minutes=minutes,
            start_date=start_date,
            end_date=end_date,
            task_queue_sid=task_queue_sid,
            task_queue_name=task_queue_name,
            friendly_name=friendly_name,
        )
