r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

"""

from marshmallow import EXCLUDE, fields as marshmallow_fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["CifsShareAcls", "CifsShareAclsSchema"]
__pdoc__ = {
    "CifsShareAclsSchema.resource": False,
    "CifsShareAclsSchema.opts": False,
    "CifsShareAcls": False,
}


class CifsShareAclsSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the CifsShareAcls object"""

    links = marshmallow_fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links", allow_none=True)
    r""" The links field of the cifs_share_acls. """

    permission = marshmallow_fields.Str(data_key="permission", allow_none=True)
    r""" Specifies the access rights that a user or group has on the defined CIFS Share.
The following values are allowed:

* no_access    - User does not have CIFS share access
* read         - User has only read access
* change       - User has change access
* full_control - User has full_control access


Valid choices:

* no_access
* read
* change
* full_control """

    type = marshmallow_fields.Str(data_key="type", allow_none=True)
    r""" Specifies the type of the user or group to add to the access control
list of a CIFS share. The following values are allowed:

* windows    - Windows user or group
* unix_user  - UNIX user
* unix_group - UNIX group


Valid choices:

* windows
* unix_user
* unix_group """

    user_or_group = marshmallow_fields.Str(data_key="user_or_group", allow_none=True)
    r""" Specifies the user or group name to add to the access control list of a CIFS share.

Example: ENGDOMAIN\ad_user """

    @property
    def resource(self):
        return CifsShareAcls

    gettable_fields = [
        "links",
        "permission",
        "type",
        "user_or_group",
    ]
    """links,permission,type,user_or_group,"""

    patchable_fields = [
        "permission",
    ]
    """permission,"""

    postable_fields = [
        "permission",
        "type",
        "user_or_group",
    ]
    """permission,type,user_or_group,"""


class CifsShareAcls(Resource):

    _schema = CifsShareAclsSchema
