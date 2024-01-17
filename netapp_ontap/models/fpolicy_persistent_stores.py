r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

"""

from marshmallow import EXCLUDE, fields as marshmallow_fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["FpolicyPersistentStores", "FpolicyPersistentStoresSchema"]
__pdoc__ = {
    "FpolicyPersistentStoresSchema.resource": False,
    "FpolicyPersistentStoresSchema.opts": False,
    "FpolicyPersistentStores": False,
}


class FpolicyPersistentStoresSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the FpolicyPersistentStores object"""

    name = marshmallow_fields.Str(data_key="name", allow_none=True)
    r""" The name specified for the FPolicy persistent store.

Example: ps1 """

    volume = marshmallow_fields.Str(data_key="volume", allow_none=True)
    r""" The specified volume to store the events for the FPolicy persistent store.

Example: psvol """

    @property
    def resource(self):
        return FpolicyPersistentStores

    gettable_fields = [
        "name",
        "volume",
    ]
    """name,volume,"""

    patchable_fields = [
        "volume",
    ]
    """volume,"""

    postable_fields = [
        "name",
        "volume",
    ]
    """name,volume,"""


class FpolicyPersistentStores(Resource):

    _schema = FpolicyPersistentStoresSchema
