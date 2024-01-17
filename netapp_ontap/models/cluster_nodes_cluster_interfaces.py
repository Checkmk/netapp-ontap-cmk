r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

"""

from marshmallow import EXCLUDE, fields as marshmallow_fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["ClusterNodesClusterInterfaces", "ClusterNodesClusterInterfacesSchema"]
__pdoc__ = {
    "ClusterNodesClusterInterfacesSchema.resource": False,
    "ClusterNodesClusterInterfacesSchema.opts": False,
    "ClusterNodesClusterInterfaces": False,
}


class ClusterNodesClusterInterfacesSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the ClusterNodesClusterInterfaces object"""

    links = marshmallow_fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links", allow_none=True)
    r""" The links field of the cluster_nodes_cluster_interfaces. """

    ip = marshmallow_fields.Nested("netapp_ontap.models.application_san_access_iscsi_endpoint_interface_ip.ApplicationSanAccessIscsiEndpointInterfaceIpSchema", unknown=EXCLUDE, data_key="ip", allow_none=True)
    r""" The ip field of the cluster_nodes_cluster_interfaces. """

    name = marshmallow_fields.Str(data_key="name", allow_none=True)
    r""" The name of the interface. If only the name is provided, the SVM scope
must be provided by the object this object is embedded in.


Example: lif1 """

    uuid = marshmallow_fields.Str(data_key="uuid", allow_none=True)
    r""" The UUID that uniquely identifies the interface.

Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return ClusterNodesClusterInterfaces

    gettable_fields = [
        "links",
        "ip",
        "name",
        "uuid",
    ]
    """links,ip,name,uuid,"""

    patchable_fields = [
        "ip",
        "name",
        "uuid",
    ]
    """ip,name,uuid,"""

    postable_fields = [
        "ip",
        "name",
        "uuid",
    ]
    """ip,name,uuid,"""


class ClusterNodesClusterInterfaces(Resource):

    _schema = ClusterNodesClusterInterfacesSchema
