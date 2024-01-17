r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

"""

from marshmallow import EXCLUDE, fields as marshmallow_fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["NvmeNamespaceLocation", "NvmeNamespaceLocationSchema"]
__pdoc__ = {
    "NvmeNamespaceLocationSchema.resource": False,
    "NvmeNamespaceLocationSchema.opts": False,
    "NvmeNamespaceLocation": False,
}


class NvmeNamespaceLocationSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the NvmeNamespaceLocation object"""

    namespace = marshmallow_fields.Str(data_key="namespace", allow_none=True)
    r""" The base name component of the NVMe namespace. Valid in POST.<br/>
If properties `name` and `location.namespace` are specified in the same request, they must refer to the base name.<br/>
NVMe namespaces do not support rename.


Example: namespace1 """

    node = marshmallow_fields.Nested("netapp_ontap.resources.node.NodeSchema", unknown=EXCLUDE, data_key="node", allow_none=True)
    r""" The node field of the nvme_namespace_location. """

    qtree = marshmallow_fields.Nested("netapp_ontap.resources.qtree.QtreeSchema", unknown=EXCLUDE, data_key="qtree", allow_none=True)
    r""" The qtree field of the nvme_namespace_location. """

    volume = marshmallow_fields.Nested("netapp_ontap.resources.volume.VolumeSchema", unknown=EXCLUDE, data_key="volume", allow_none=True)
    r""" The volume field of the nvme_namespace_location. """

    @property
    def resource(self):
        return NvmeNamespaceLocation

    gettable_fields = [
        "namespace",
        "node.links",
        "node.name",
        "node.uuid",
        "qtree.links",
        "qtree.id",
        "qtree.name",
        "volume.links",
        "volume.name",
        "volume.uuid",
    ]
    """namespace,node.links,node.name,node.uuid,qtree.links,qtree.id,qtree.name,volume.links,volume.name,volume.uuid,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
        "namespace",
        "qtree.id",
        "qtree.name",
        "volume.name",
        "volume.uuid",
    ]
    """namespace,qtree.id,qtree.name,volume.name,volume.uuid,"""


class NvmeNamespaceLocation(Resource):

    _schema = NvmeNamespaceLocationSchema
