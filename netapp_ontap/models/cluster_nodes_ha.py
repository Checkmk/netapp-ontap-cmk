r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

"""

from marshmallow import EXCLUDE, fields as marshmallow_fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["ClusterNodesHa", "ClusterNodesHaSchema"]
__pdoc__ = {
    "ClusterNodesHaSchema.resource": False,
    "ClusterNodesHaSchema.opts": False,
    "ClusterNodesHa": False,
}


class ClusterNodesHaSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the ClusterNodesHa object"""

    auto_giveback = marshmallow_fields.Boolean(data_key="auto_giveback", allow_none=True)
    r""" Specifies whether giveback is automatically initiated when the node that owns the storage is ready. """

    enabled = marshmallow_fields.Boolean(data_key="enabled", allow_none=True)
    r""" Specifies whether or not storage failover is enabled. """

    giveback = marshmallow_fields.Nested("netapp_ontap.models.cluster_nodes_ha_giveback.ClusterNodesHaGivebackSchema", unknown=EXCLUDE, data_key="giveback", allow_none=True)
    r""" The giveback field of the cluster_nodes_ha. """

    interconnect = marshmallow_fields.Nested("netapp_ontap.models.cluster_nodes_ha_interconnect.ClusterNodesHaInterconnectSchema", unknown=EXCLUDE, data_key="interconnect", allow_none=True)
    r""" The interconnect field of the cluster_nodes_ha. """

    partners = marshmallow_fields.List(marshmallow_fields.Nested("netapp_ontap.resources.node.NodeSchema", unknown=EXCLUDE, allow_none=True), data_key="partners", allow_none=True)
    r""" Nodes in this node's High Availability (HA) group. """

    ports = marshmallow_fields.List(marshmallow_fields.Nested("netapp_ontap.models.cluster_nodes_ha_ports.ClusterNodesHaPortsSchema", unknown=EXCLUDE, allow_none=True), data_key="ports", allow_none=True)
    r""" The ports field of the cluster_nodes_ha. """

    takeover = marshmallow_fields.Nested("netapp_ontap.models.cluster_nodes_ha_takeover.ClusterNodesHaTakeoverSchema", unknown=EXCLUDE, data_key="takeover", allow_none=True)
    r""" The takeover field of the cluster_nodes_ha. """

    takeover_check = marshmallow_fields.Nested("netapp_ontap.models.cluster_nodes_ha_takeover_check.ClusterNodesHaTakeoverCheckSchema", unknown=EXCLUDE, data_key="takeover_check", allow_none=True)
    r""" The takeover_check field of the cluster_nodes_ha. """

    @property
    def resource(self):
        return ClusterNodesHa

    gettable_fields = [
        "auto_giveback",
        "enabled",
        "giveback",
        "interconnect",
        "partners.links",
        "partners.name",
        "partners.uuid",
        "ports",
        "takeover",
        "takeover_check",
    ]
    """auto_giveback,enabled,giveback,interconnect,partners.links,partners.name,partners.uuid,ports,takeover,takeover_check,"""

    patchable_fields = [
        "auto_giveback",
        "enabled",
    ]
    """auto_giveback,enabled,"""

    postable_fields = [
        "auto_giveback",
        "enabled",
    ]
    """auto_giveback,enabled,"""


class ClusterNodesHa(Resource):

    _schema = ClusterNodesHaSchema
