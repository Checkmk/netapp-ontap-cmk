r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

"""

from marshmallow import EXCLUDE, fields as marshmallow_fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["S3ServiceUserPost", "S3ServiceUserPostSchema"]
__pdoc__ = {
    "S3ServiceUserPostSchema.resource": False,
    "S3ServiceUserPostSchema.opts": False,
    "S3ServiceUserPost": False,
}


class S3ServiceUserPostSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the S3ServiceUserPost object"""

    links = marshmallow_fields.Nested("netapp_ontap.models.collection_links.CollectionLinksSchema", unknown=EXCLUDE, data_key="_links", allow_none=True)
    r""" The links field of the s3_service_user_post. """

    access_key = marshmallow_fields.Str(data_key="access_key", allow_none=True)
    r""" Specifies the access key for the user.

Example: HJAKU28M3SXTE2UXUACV """

    name = marshmallow_fields.Str(data_key="name", allow_none=True)
    r""" The name of the user.

Example: user-1 """

    secret_key = marshmallow_fields.Str(data_key="secret_key", allow_none=True)
    r""" Specifies the secret key for the user.

Example: BcA_HX6If458llhnx3n1TCO3mg4roCXG0ddYf_cJ """

    @property
    def resource(self):
        return S3ServiceUserPost

    gettable_fields = [
        "links",
        "access_key",
        "name",
        "secret_key",
    ]
    """links,access_key,name,secret_key,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
    ]
    """"""


class S3ServiceUserPost(Resource):

    _schema = S3ServiceUserPostSchema
