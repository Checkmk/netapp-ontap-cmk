r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

"""

from marshmallow import EXCLUDE, fields as marshmallow_fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["ConsistencyGroupConsistencyGroupsLuns", "ConsistencyGroupConsistencyGroupsLunsSchema"]
__pdoc__ = {
    "ConsistencyGroupConsistencyGroupsLunsSchema.resource": False,
    "ConsistencyGroupConsistencyGroupsLunsSchema.opts": False,
    "ConsistencyGroupConsistencyGroupsLuns": False,
}


class ConsistencyGroupConsistencyGroupsLunsSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the ConsistencyGroupConsistencyGroupsLuns object"""

    clone = marshmallow_fields.Nested("netapp_ontap.models.consistency_group_consistency_groups_luns_clone.ConsistencyGroupConsistencyGroupsLunsCloneSchema", unknown=EXCLUDE, data_key="clone", allow_none=True)
    r""" The clone field of the consistency_group_consistency_groups_luns. """

    comment = marshmallow_fields.Str(data_key="comment", allow_none=True)
    r""" A configurable comment available for use by the administrator. Valid in POST and PATCH. """

    create_time = ImpreciseDateTime(data_key="create_time", allow_none=True)
    r""" The time the LUN was created.

Example: 2018-06-04T19:00:00.000+0000 """

    enabled = marshmallow_fields.Boolean(data_key="enabled", allow_none=True)
    r""" The enabled state of the LUN. LUNs can be disabled to prevent access to the LUN. Certain error conditions also cause the LUN to become disabled. If the LUN is disabled, you can consult the `state` property to determine if the LUN is administratively disabled (_offline_) or has become disabled as a result of an error. A LUN in an error condition can be brought online by setting the `enabled` property to _true_ or brought administratively offline by setting the `enabled` property to _false_. Upon creation, a LUN is enabled by default. Valid in PATCH. """

    lun_maps = marshmallow_fields.List(marshmallow_fields.Nested("netapp_ontap.models.consistency_group_lun_map.ConsistencyGroupLunMapSchema", unknown=EXCLUDE, allow_none=True), data_key="lun_maps", allow_none=True)
    r""" An array of LUN maps.<br/>
A LUN map is an association between a LUN and an initiator group. When a LUN is mapped to an initiator group, the initiator group's initiators are granted access to the LUN. The relationship between a LUN and an initiator group is many LUNs to many initiator groups. """

    name = marshmallow_fields.Str(data_key="name", allow_none=True)
    r""" The fully qualified path name of the LUN composed of the "/vol" prefix, the volume name, the qtree name (optional), and the base name of the LUN. Valid in POST and PATCH.


Example: /vol/volume1/lun1 """

    os_type = marshmallow_fields.Str(data_key="os_type", allow_none=True)
    r""" The operating system type of the LUN.<br/>
Required in POST when creating a LUN that is not a clone of another. Disallowed in POST when creating a LUN clone.


Valid choices:

* aix
* hpux
* hyper_v
* linux
* netware
* openvms
* solaris
* solaris_efi
* vmware
* windows
* windows_2008
* windows_gpt
* xen """

    provisioning_options = marshmallow_fields.Nested("netapp_ontap.models.consistency_group_vdisk_provisioning_options.ConsistencyGroupVdiskProvisioningOptionsSchema", unknown=EXCLUDE, data_key="provisioning_options", allow_none=True)
    r""" The provisioning_options field of the consistency_group_consistency_groups_luns. """

    qos = marshmallow_fields.Nested("netapp_ontap.models.consistency_group_qos.ConsistencyGroupQosSchema", unknown=EXCLUDE, data_key="qos", allow_none=True)
    r""" The qos field of the consistency_group_consistency_groups_luns. """

    serial_number = marshmallow_fields.Str(data_key="serial_number", allow_none=True)
    r""" The LUN serial number. The serial number is generated by ONTAP when the LUN is created. """

    space = marshmallow_fields.Nested("netapp_ontap.models.consistency_group_lun_space.ConsistencyGroupLunSpaceSchema", unknown=EXCLUDE, data_key="space", allow_none=True)
    r""" The space field of the consistency_group_consistency_groups_luns. """

    uuid = marshmallow_fields.Str(data_key="uuid", allow_none=True)
    r""" The unique identifier of the LUN.  The UUID is generated by ONTAP when the LUN is created.


Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return ConsistencyGroupConsistencyGroupsLuns

    gettable_fields = [
        "comment",
        "create_time",
        "enabled",
        "lun_maps",
        "name",
        "os_type",
        "qos.policy",
        "serial_number",
        "space",
        "uuid",
    ]
    """comment,create_time,enabled,lun_maps,name,os_type,qos.policy,serial_number,space,uuid,"""

    patchable_fields = [
        "clone",
        "comment",
        "lun_maps",
        "provisioning_options",
        "qos.policy",
        "space",
    ]
    """clone,comment,lun_maps,provisioning_options,qos.policy,space,"""

    postable_fields = [
        "clone",
        "comment",
        "lun_maps",
        "name",
        "os_type",
        "provisioning_options",
        "qos.policy",
        "space",
    ]
    """clone,comment,lun_maps,name,os_type,provisioning_options,qos.policy,space,"""


class ConsistencyGroupConsistencyGroupsLuns(Resource):

    _schema = ConsistencyGroupConsistencyGroupsLunsSchema
