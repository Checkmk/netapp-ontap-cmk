r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

"""

from marshmallow import EXCLUDE, fields as marshmallow_fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["LunSpace", "LunSpaceSchema"]
__pdoc__ = {
    "LunSpaceSchema.resource": False,
    "LunSpaceSchema.opts": False,
    "LunSpace": False,
}


class LunSpaceSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the LunSpace object"""

    guarantee = marshmallow_fields.Nested("netapp_ontap.models.lun_space_guarantee.LunSpaceGuaranteeSchema", unknown=EXCLUDE, data_key="guarantee", allow_none=True)
    r""" The guarantee field of the lun_space. """

    scsi_thin_provisioning_support_enabled = marshmallow_fields.Boolean(data_key="scsi_thin_provisioning_support_enabled", allow_none=True)
    r""" To leverage the benefits of SCSI thin provisioning, it must be supported by your host. SCSI thin provisioning uses the Logical Block Provisioning feature as defined in the SCSI SBC-3 standard. Only hosts that support this standard can use SCSI thin provisioning in ONTAP.<br/>
When you enable SCSI thin provisioning support in ONTAP, you turn on the following SCSI thin provisioning features:
- Unmapping and reporting space usage for space reclamation
- Reporting resource exhaustion errors
<p/>
The value of this property is not propagated to the destination when a LUN is cloned as a new LUN or copied; it is reset to false. The value of this property is maintained from the destination LUN when a LUN is overwritten as a clone.<br/>
Valid in POST and PATCH. """

    size = Size(data_key="size", allow_none=True)
    r""" The total provisioned size of the LUN. The LUN size can be increased but not be made smaller using the REST interface.<br/>
The maximum and minimum sizes listed here are the absolute maximum and absolute minimum sizes in bytes. The actual minimum and maxiumum sizes vary depending on the ONTAP version, ONTAP platform and the available space in the containing volume and aggregate.<br/>
For more information, see _Size properties_ in the _docs_ section of the ONTAP REST API documentation.


Example: 1073741824 """

    used = Size(data_key="used", allow_none=True)
    r""" The amount of space consumed by the main data stream of the LUN.<br/>
This value is the total space consumed in the volume by the LUN, including filesystem overhead, but excluding prefix and suffix streams. Due to internal filesystem overhead and the many ways SAN filesystems and applications utilize blocks within a LUN, this value does not necessarily reflect actual consumption/availability from the perspective of the filesystem or application. Without specific knowledge of how the LUN blocks are utilized outside of ONTAP, this property should not be used as an indicator for an out-of-space condition.<br/>
For more information, see _Size properties_ in the _docs_ section of the ONTAP REST API documentation. """

    @property
    def resource(self):
        return LunSpace

    gettable_fields = [
        "guarantee",
        "scsi_thin_provisioning_support_enabled",
        "size",
        "used",
    ]
    """guarantee,scsi_thin_provisioning_support_enabled,size,used,"""

    patchable_fields = [
        "guarantee",
        "scsi_thin_provisioning_support_enabled",
        "size",
    ]
    """guarantee,scsi_thin_provisioning_support_enabled,size,"""

    postable_fields = [
        "guarantee",
        "scsi_thin_provisioning_support_enabled",
        "size",
    ]
    """guarantee,scsi_thin_provisioning_support_enabled,size,"""


class LunSpace(Resource):

    _schema = LunSpaceSchema
