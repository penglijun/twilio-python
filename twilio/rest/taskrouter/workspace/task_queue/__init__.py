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
from twilio.rest.v2010.workspace.task_queue.task_queue_statistics import StatisticsContext
from twilio.rest.v2010.workspace.task_queue.task_queues_statistics import StatisticsList


class TaskQueueList(ListResource):

    def __init__(self, domain, workspace_sid):
        super(TaskQueueList, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'workspace_sid': workspace_sid,
        }
        self._uri = "/Workspaces/{workspace_sid}/TaskQueues".format(**self._instance_kwargs)
        
        # Components
        self._statistics = None

    def read(self, friendly_name=values.unset,
             evaluate_worker_attributes=values.unset, limit=None, page_size=None,
             **kwargs):
        limits = self._domain.read_limits(limit, page_size)
        
        params = values.of({
            "FriendlyName": friendly_name,
            "EvaluateWorkerAttributes": evaluate_worker_attributes,
        })
        params.update(kwargs)
        
        return self._domain.read(
            self,
            TaskQueueInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, friendly_name=values.unset,
             evaluate_worker_attributes=values.unset, page_token=None, page=None,
             page_size=None, **kwargs):
        params = values.of({
            "FriendlyName": friendly_name,
        })
        params.update(kwargs)
        
        return self._domain.page(
            self,
            TaskQueueInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def create(self, friendly_name, reservation_activity_sid,
               assignment_activity_sid, target_workers=values.unset,
               max_reserved_workers=values.unset):
        data = values.of({
            "FriendlyName": friendly_name,
            "ReservationActivitySid": reservation_activity_sid,
            "AssignmentActivitySid": assignment_activity_sid,
            "TargetWorkers": target_workers,
            "MaxReservedWorkers": max_reserved_workers,
        })
        
        return self._domain.create(
            TaskQueueInstance,
            self._instance_kwargs,
            'POST',
            self._uri,
            data=data,
        )

    @property
    def statistics(self):
        if self._statistics is None:
            self._statistics = StatisticsList(self._domain, **self._instance_kwargs)
        return self._statistics


class TaskQueueContext(InstanceContext):

    def __init__(self, domain, workspace_sid, sid):
        super(TaskQueueContext, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'workspace_sid': workspace_sid,
            'sid': sid,
        }
        self._uri = "/Workspaces/{workspace_sid}/TaskQueues/{sid}".format(**self._instance_kwargs)
        
        # Dependents
        self._statistics = None

    def fetch(self):
        return self._domain.fetch(
            TaskQueueInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
        )

    def update(self, friendly_name=values.unset, target_workers=values.unset,
               reservation_activity_sid=values.unset,
               assignment_activity_sid=values.unset,
               max_reserved_workers=values.unset):
        data = values.of({
            "FriendlyName": friendly_name,
            "TargetWorkers": target_workers,
            "ReservationActivitySid": reservation_activity_sid,
            "AssignmentActivitySid": assignment_activity_sid,
            "MaxReservedWorkers": max_reserved_workers,
        })
        
        return self._domain.update(
            TaskQueueInstance,
            self._instance_kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def delete(self):
        return self._domain.delete("delete", self._uri)

    @property
    def statistics(self):
        if self._statistics is None:
            self._statistics = StatisticsContext(
                self._domain,
                workspace_sid=self._instance_kwargs['workspace_sid'],
                task_queue_sid=self._instance_kwargs['sid'],
            )
        return self._statistics


class TaskQueueInstance(InstanceResource):

    def __init__(self, domain, payload, workspace_sid, sid=None):
        super(TaskQueueInstance, self).__init__(domain)
        
        # Marshaled Properties
        self._account_sid = payload['account_sid']
        self._assignment_activity_sid = payload['assignment_activity_sid']
        self._assignment_activity_name = payload['assignment_activity_name']
        self._date_created = deserialize.iso8601_datetime(payload['date_created'])
        self._date_updated = deserialize.iso8601_datetime(payload['date_updated'])
        self._friendly_name = payload['friendly_name']
        self._max_reserved_workers = payload['max_reserved_workers']
        self._reservation_activity_sid = payload['reservation_activity_sid']
        self._reservation_activity_name = payload['reservation_activity_name']
        self._sid = payload['sid']
        self._target_workers = payload['target_workers']
        self._url = payload['url']
        self._workspace_sid = payload['workspace_sid']
        
        # Context
        self._lazy_context = None
        self._context_workspace_sid = workspace_sid
        self._context_sid = sid or self._sid

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = TaskQueueContext(
                self._domain,
                self._context_workspace_sid,
                self._context_sid,
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._account_sid

    @property
    def assignment_activity_sid(self):
        """ The assignment_activity_sid """
        return self._assignment_activity_sid

    @property
    def assignment_activity_name(self):
        """ The assignment_activity_name """
        return self._assignment_activity_name

    @property
    def date_created(self):
        """ The date_created """
        return self._date_created

    @property
    def date_updated(self):
        """ The date_updated """
        return self._date_updated

    @property
    def friendly_name(self):
        """ The friendly_name """
        return self._friendly_name

    @property
    def max_reserved_workers(self):
        """ The max_reserved_workers """
        return self._max_reserved_workers

    @property
    def reservation_activity_sid(self):
        """ The reservation_activity_sid """
        return self._reservation_activity_sid

    @property
    def reservation_activity_name(self):
        """ The reservation_activity_name """
        return self._reservation_activity_name

    @property
    def sid(self):
        """ The sid """
        return self._sid

    @property
    def target_workers(self):
        """ The target_workers """
        return self._target_workers

    @property
    def url(self):
        """ The url """
        return self._url

    @property
    def workspace_sid(self):
        """ The workspace_sid """
        return self._workspace_sid

    def fetch(self):
        self._context.fetch()

    def update(self, friendly_name=values.unset, target_workers=values.unset,
               reservation_activity_sid=values.unset,
               assignment_activity_sid=values.unset,
               max_reserved_workers=values.unset):
        self._context.update(
            friendly_name=friendly_name,
            target_workers=target_workers,
            reservation_activity_sid=reservation_activity_sid,
            assignment_activity_sid=assignment_activity_sid,
            max_reserved_workers=max_reserved_workers,
        )

    def delete(self):
        self._context.delete()
