r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

"""

from marshmallow import EXCLUDE, fields as marshmallow_fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["ClusterNodesHaGiveback", "ClusterNodesHaGivebackSchema"]
__pdoc__ = {
    "ClusterNodesHaGivebackSchema.resource": False,
    "ClusterNodesHaGivebackSchema.opts": False,
    "ClusterNodesHaGiveback": False,
}


class ClusterNodesHaGivebackSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the ClusterNodesHaGiveback object"""

    failure = marshmallow_fields.Nested("netapp_ontap.models.cluster_nodes_ha_giveback_failure.ClusterNodesHaGivebackFailureSchema", unknown=EXCLUDE, data_key="failure", allow_none=True)
    r""" The failure field of the cluster_nodes_ha_giveback. """

    state = marshmallow_fields.Str(data_key="state", allow_none=True)
    r""" The state field of the cluster_nodes_ha_giveback.

Valid choices:

* nothing_to_giveback
* not_attempted
* in_progress
* failed """

    status = marshmallow_fields.List(marshmallow_fields.Nested("netapp_ontap.models.giveback_status.GivebackStatusSchema", unknown=EXCLUDE, allow_none=True), data_key="status", allow_none=True)
    r""" Giveback status of each aggregate. """

    @property
    def resource(self):
        return ClusterNodesHaGiveback

    gettable_fields = [
        "failure",
        "state",
        "status",
    ]
    """failure,state,status,"""

    patchable_fields = [
        "failure",
        "state",
    ]
    """failure,state,"""

    postable_fields = [
        "failure",
        "state",
    ]
    """failure,state,"""


class ClusterNodesHaGiveback(Resource):

    _schema = ClusterNodesHaGivebackSchema
