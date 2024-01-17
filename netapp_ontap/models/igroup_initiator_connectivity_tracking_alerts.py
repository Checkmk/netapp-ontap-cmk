r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

"""

from marshmallow import EXCLUDE, fields as marshmallow_fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["IgroupInitiatorConnectivityTrackingAlerts", "IgroupInitiatorConnectivityTrackingAlertsSchema"]
__pdoc__ = {
    "IgroupInitiatorConnectivityTrackingAlertsSchema.resource": False,
    "IgroupInitiatorConnectivityTrackingAlertsSchema.opts": False,
    "IgroupInitiatorConnectivityTrackingAlerts": False,
}


class IgroupInitiatorConnectivityTrackingAlertsSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the IgroupInitiatorConnectivityTrackingAlerts object"""

    summary = marshmallow_fields.Nested("netapp_ontap.models.error.ErrorSchema", unknown=EXCLUDE, data_key="summary", allow_none=True)
    r""" The summary field of the igroup_initiator_connectivity_tracking_alerts. """

    @property
    def resource(self):
        return IgroupInitiatorConnectivityTrackingAlerts

    gettable_fields = [
        "summary",
    ]
    """summary,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
    ]
    """"""


class IgroupInitiatorConnectivityTrackingAlerts(Resource):

    _schema = IgroupInitiatorConnectivityTrackingAlertsSchema
