r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

"""

from marshmallow import EXCLUDE, fields as marshmallow_fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["NodeResponseRecordsHaPartners", "NodeResponseRecordsHaPartnersSchema"]
__pdoc__ = {
    "NodeResponseRecordsHaPartnersSchema.resource": False,
    "NodeResponseRecordsHaPartnersSchema.opts": False,
    "NodeResponseRecordsHaPartners": False,
}


class NodeResponseRecordsHaPartnersSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the NodeResponseRecordsHaPartners object"""

    links = marshmallow_fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links", allow_none=True)
    r""" The links field of the node_response_records_ha_partners. """

    name = marshmallow_fields.Str(data_key="name", allow_none=True)
    r""" The name field of the node_response_records_ha_partners.

Example: node1 """

    uuid = marshmallow_fields.Str(data_key="uuid", allow_none=True)
    r""" The uuid field of the node_response_records_ha_partners.

Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return NodeResponseRecordsHaPartners

    gettable_fields = [
        "links",
        "name",
        "uuid",
    ]
    """links,name,uuid,"""

    patchable_fields = [
        "name",
        "uuid",
    ]
    """name,uuid,"""

    postable_fields = [
        "name",
        "uuid",
    ]
    """name,uuid,"""


class NodeResponseRecordsHaPartners(Resource):

    _schema = NodeResponseRecordsHaPartnersSchema