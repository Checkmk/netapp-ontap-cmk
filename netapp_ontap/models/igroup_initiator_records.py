r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

"""

from marshmallow import EXCLUDE, fields as marshmallow_fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["IgroupInitiatorRecords", "IgroupInitiatorRecordsSchema"]
__pdoc__ = {
    "IgroupInitiatorRecordsSchema.resource": False,
    "IgroupInitiatorRecordsSchema.opts": False,
    "IgroupInitiatorRecords": False,
}


class IgroupInitiatorRecordsSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the IgroupInitiatorRecords object"""

    links = marshmallow_fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links", allow_none=True)
    r""" The links field of the igroup_initiator_records. """

    comment = marshmallow_fields.Str(data_key="comment", allow_none=True)
    r""" A comment available for use by the administrator. Valid in POST and PATCH. """

    name = marshmallow_fields.Str(data_key="name", allow_none=True)
    r""" The FC WWPN, iSCSI IQN, or iSCSI EUI that identifies the host initiator. Valid in POST only and not allowed when the `records` property is used.<br/>
An FC WWPN consists of 16 hexadecimal digits grouped as 8 pairs separated by colons. The format for an iSCSI IQN is _iqn.yyyy-mm.reverse_domain_name:any_. The iSCSI EUI format consists of the _eui._ prefix followed by 16 hexadecimal characters.


Example: iqn.1998-01.com.corp.iscsi:name1 """

    @property
    def resource(self):
        return IgroupInitiatorRecords

    gettable_fields = [
        "links",
        "comment",
        "name",
    ]
    """links,comment,name,"""

    patchable_fields = [
        "comment",
    ]
    """comment,"""

    postable_fields = [
        "comment",
        "name",
    ]
    """comment,name,"""


class IgroupInitiatorRecords(Resource):

    _schema = IgroupInitiatorRecordsSchema
