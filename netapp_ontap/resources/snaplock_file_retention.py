r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

This API manages the SnapLock retention time of a file. You can perform a privileged-delete operation by executing this API.
### Examples
1. Sets the SnapLock retention time of a file:
   <br/>
   ```
   PATCH "/api/storage/snaplock/file/000dc5fd-4175-11e9-b937-0050568e3f82/%2Ffile2.txt" '{"expiry_time": "2030-02-14T18:30:00+5:30"}'
   ```
   <br/>
2. Extends the retention time of a WORM file:
   <br/>
   ```
   PATCH "/api/storage/snaplock/file/000dc5fd-4175-11e9-b937-0050568e3f82/%2Ffile2.txt" '{"expiry_time": "infinite"}'
   ```
   <br/>
3. Extends the retention time of a WORM file:
   <br/>
   ```
   PATCH "/api/storage/snaplock/file/000dc5fd-4175-11e9-b937-0050568e3f82/%2Ffile2.txt" '{"retention_period": "P1M"}'
   ```
   <br/>
4. Extends the retention time of a WORM file:
   <br/>
   ```
   PATCH "/api/storage/snaplock/file/000dc5fd-4175-11e9-b937-0050568e3f82/%2Ffile2.txt" '{"retention_period": "infinite"}'
   ```
   <br/>"""

import asyncio
from datetime import datetime
import inspect
from typing import Callable, Iterable, List, Optional, Union

try:
    RECLINE_INSTALLED = False
    import recline
    from recline.arg_types.choices import Choices
    from recline.commands import ReclineCommandError
    from netapp_ontap.resource_table import ResourceTable
    RECLINE_INSTALLED = True
except ImportError:
    pass

from marshmallow import fields as marshmallow_fields, EXCLUDE  # type: ignore

import netapp_ontap
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size
from netapp_ontap.raw_resource import RawResource

from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["SnaplockFileRetention", "SnaplockFileRetentionSchema"]
__pdoc__ = {
    "SnaplockFileRetentionSchema.resource": False,
    "SnaplockFileRetentionSchema.opts": False,
    "SnaplockFileRetention.snaplock_file_retention_show": False,
    "SnaplockFileRetention.snaplock_file_retention_create": False,
    "SnaplockFileRetention.snaplock_file_retention_modify": False,
    "SnaplockFileRetention.snaplock_file_retention_delete": False,
}


class SnaplockFileRetentionSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the SnaplockFileRetention object"""

    links = marshmallow_fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE, allow_none=True)
    r""" The links field of the snaplock_file_retention."""

    expiry_time = marshmallow_fields.Str(
        data_key="expiry_time",
        allow_none=True,
    )
    r""" Expiry time of the file in date-time format, "infinite", "indefinite", or "unspecified". An "infinite" retention time indicates that the file will be retained forever. An "unspecified" retention time indicates that the file will be retained forever; however, the retention time of the file can be changed to an absolute value. An "indefinite" retention time indicates that the file is under Legal-Hold.

Example: 2058-06-04T19:00:00.000+0000"""

    file_path = marshmallow_fields.Str(
        data_key="file_path",
        allow_none=True,
    )
    r""" Specifies the volume relative path of the file

Example: /dir1/file"""

    is_expired = marshmallow_fields.Boolean(
        data_key="is_expired",
        allow_none=True,
    )
    r""" This indicates if the file is under active retention or if the file is past its expiry time.

Example: true"""

    retention_period = marshmallow_fields.Str(
        data_key="retention_period",
        allow_none=True,
    )
    r""" Duration of retention time file to be locked with,  An "infinite" retention period indicates that the file will be retained forever.

Example: P2M"""

    seconds_until_expiry = Size(
        data_key="seconds_until_expiry",
        allow_none=True,
    )
    r""" Specifies the number of seconds until the expiration time of the file.

Example: 168"""

    svm = marshmallow_fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE, allow_none=True)
    r""" The svm field of the snaplock_file_retention."""

    volume = marshmallow_fields.Nested("netapp_ontap.resources.volume.VolumeSchema", data_key="volume", unknown=EXCLUDE, allow_none=True)
    r""" The volume field of the snaplock_file_retention."""

    @property
    def resource(self):
        return SnaplockFileRetention

    gettable_fields = [
        "links",
        "expiry_time",
        "file_path",
        "is_expired",
        "seconds_until_expiry",
        "svm.links",
        "svm.name",
        "svm.uuid",
        "volume.links",
        "volume.name",
        "volume.uuid",
    ]
    """links,expiry_time,file_path,is_expired,seconds_until_expiry,svm.links,svm.name,svm.uuid,volume.links,volume.name,volume.uuid,"""

    patchable_fields = [
        "expiry_time",
        "retention_period",
    ]
    """expiry_time,retention_period,"""

    postable_fields = [
        "file_path",
        "retention_period",
        "svm.name",
        "svm.uuid",
        "volume.name",
        "volume.uuid",
    ]
    """file_path,retention_period,svm.name,svm.uuid,volume.name,volume.uuid,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in SnaplockFileRetention.get_collection(fields=field)]
    return getter

async def _wait_for_job(response: NetAppResponse) -> None:
    """Examine the given response. If it is a job, asynchronously wait for it to
    complete. While polling, prints the current status message of the job.
    """

    if not response.is_job:
        return
    from netapp_ontap.resources import Job
    job = Job(**response.http_response.json()["job"])
    while True:
        job.get(fields="state,message")
        if hasattr(job, "message"):
            print("[%s]: %s" % (job.state, job.message))
        if job.state == "failure":
            raise NetAppRestError("SnaplockFileRetention modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class SnaplockFileRetention(Resource):
    """Allows interaction with SnaplockFileRetention objects on the host"""

    _schema = SnaplockFileRetentionSchema
    _path = "/api/storage/snaplock/file"
    _keys = ["volume.uuid", "path"]


    @classmethod
    def patch_collection(
        cls,
        body: dict,
        *args,
        records: Iterable["SnaplockFileRetention"] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates the SnapLock retention time of a file or extends the retention time of a WORM file. Input parameters "expiry_time" or "retention_period" can be used to set or extend the retention time of file. Both "expiry_time" and "retention_period" parameters expect the date in ISO 8601 format. Additionally, the "expiry_time" parameter can also be set to "infinite" or "unspecified" and the "retention_period" parameter can also be set to "infinite". The input parameters are mutually exclusive.
### Related ONTAP commands
* `volume file retention set`
### Learn more
* [`DOC /storage/snaplock/file/{volume.uuid}/{path}`](#docs-snaplock-storage_snaplock_file_{volume.uuid}_{path})
"""
        return super()._patch_collection(
            body, *args, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    patch_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch_collection.__doc__)


    @classmethod
    def delete_collection(
        cls,
        *args,
        records: Iterable["SnaplockFileRetention"] = None,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes unexpired WORM files of a SnapLock Enterprise volume. This is a privileged-delete operation. The only built-in role that has access to the command is vsadmin-snaplock.
### Related ONTAP commands
* `volume file privileged-delete`
### Learn more
* [`DOC /storage/snaplock/file/{volume.uuid}/{path}`](#docs-snaplock-storage_snaplock_file_{volume.uuid}_{path})
"""
        return super()._delete_collection(
            *args, body=body, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)


    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the SnapLock retention details of the specified file. An indefinite expiry time indicates the file is under a Legal-Hold.
### Related ONTAP commands
* `volume file retention show`
### Learn more
* [`DOC /storage/snaplock/file/{volume.uuid}/{path}`](#docs-snaplock-storage_snaplock_file_{volume.uuid}_{path})
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="snaplock file retention show")
        def snaplock_file_retention_show(
            fields: List[str] = None,
        ) -> ResourceTable:
            """Fetch a single SnaplockFileRetention resource

            Args:
                expiry_time: Expiry time of the file in date-time format, \"infinite\", \"indefinite\", or \"unspecified\". An \"infinite\" retention time indicates that the file will be retained forever. An \"unspecified\" retention time indicates that the file will be retained forever; however, the retention time of the file can be changed to an absolute value. An \"indefinite\" retention time indicates that the file is under Legal-Hold.
                file_path: Specifies the volume relative path of the file
                is_expired: This indicates if the file is under active retention or if the file is past its expiry time.
                retention_period: Duration of retention time file to be locked with,  An \"infinite\" retention period indicates that the file will be retained forever.
                seconds_until_expiry: Specifies the number of seconds until the expiration time of the file.
            """

            kwargs = {}
            if expiry_time is not None:
                kwargs["expiry_time"] = expiry_time
            if file_path is not None:
                kwargs["file_path"] = file_path
            if is_expired is not None:
                kwargs["is_expired"] = is_expired
            if retention_period is not None:
                kwargs["retention_period"] = retention_period
            if seconds_until_expiry is not None:
                kwargs["seconds_until_expiry"] = seconds_until_expiry
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            resource = SnaplockFileRetention(
                **kwargs
            )
            resource.get()
            return [resource]


    def patch(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates the SnapLock retention time of a file or extends the retention time of a WORM file. Input parameters "expiry_time" or "retention_period" can be used to set or extend the retention time of file. Both "expiry_time" and "retention_period" parameters expect the date in ISO 8601 format. Additionally, the "expiry_time" parameter can also be set to "infinite" or "unspecified" and the "retention_period" parameter can also be set to "infinite". The input parameters are mutually exclusive.
### Related ONTAP commands
* `volume file retention set`
### Learn more
* [`DOC /storage/snaplock/file/{volume.uuid}/{path}`](#docs-snaplock-storage_snaplock_file_{volume.uuid}_{path})
"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="snaplock file retention modify")
        async def snaplock_file_retention_modify(
        ) -> ResourceTable:
            """Modify an instance of a SnaplockFileRetention resource

            Args:
                expiry_time: Expiry time of the file in date-time format, \"infinite\", \"indefinite\", or \"unspecified\". An \"infinite\" retention time indicates that the file will be retained forever. An \"unspecified\" retention time indicates that the file will be retained forever; however, the retention time of the file can be changed to an absolute value. An \"indefinite\" retention time indicates that the file is under Legal-Hold.
                query_expiry_time: Expiry time of the file in date-time format, \"infinite\", \"indefinite\", or \"unspecified\". An \"infinite\" retention time indicates that the file will be retained forever. An \"unspecified\" retention time indicates that the file will be retained forever; however, the retention time of the file can be changed to an absolute value. An \"indefinite\" retention time indicates that the file is under Legal-Hold.
                file_path: Specifies the volume relative path of the file
                query_file_path: Specifies the volume relative path of the file
                is_expired: This indicates if the file is under active retention or if the file is past its expiry time.
                query_is_expired: This indicates if the file is under active retention or if the file is past its expiry time.
                retention_period: Duration of retention time file to be locked with,  An \"infinite\" retention period indicates that the file will be retained forever.
                query_retention_period: Duration of retention time file to be locked with,  An \"infinite\" retention period indicates that the file will be retained forever.
                seconds_until_expiry: Specifies the number of seconds until the expiration time of the file.
                query_seconds_until_expiry: Specifies the number of seconds until the expiration time of the file.
            """

            kwargs = {}
            changes = {}
            if query_expiry_time is not None:
                kwargs["expiry_time"] = query_expiry_time
            if query_file_path is not None:
                kwargs["file_path"] = query_file_path
            if query_is_expired is not None:
                kwargs["is_expired"] = query_is_expired
            if query_retention_period is not None:
                kwargs["retention_period"] = query_retention_period
            if query_seconds_until_expiry is not None:
                kwargs["seconds_until_expiry"] = query_seconds_until_expiry

            if expiry_time is not None:
                changes["expiry_time"] = expiry_time
            if file_path is not None:
                changes["file_path"] = file_path
            if is_expired is not None:
                changes["is_expired"] = is_expired
            if retention_period is not None:
                changes["retention_period"] = retention_period
            if seconds_until_expiry is not None:
                changes["seconds_until_expiry"] = seconds_until_expiry

            if hasattr(SnaplockFileRetention, "find"):
                resource = SnaplockFileRetention.find(
                    **kwargs
                )
            else:
                resource = SnaplockFileRetention()
            try:
                for key, value in changes.items():
                    setattr(resource, key, value)
                response = resource.patch(poll=False)
                await _wait_for_job(response)
                resource.get(fields=",".join(changes.keys()))
                return [resource]
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to modify SnaplockFileRetention: %s" % err)

    def delete(
        self,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes unexpired WORM files of a SnapLock Enterprise volume. This is a privileged-delete operation. The only built-in role that has access to the command is vsadmin-snaplock.
### Related ONTAP commands
* `volume file privileged-delete`
### Learn more
* [`DOC /storage/snaplock/file/{volume.uuid}/{path}`](#docs-snaplock-storage_snaplock_file_{volume.uuid}_{path})
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="snaplock file retention delete")
        async def snaplock_file_retention_delete(
        ) -> None:
            """Delete an instance of a SnaplockFileRetention resource

            Args:
                expiry_time: Expiry time of the file in date-time format, \"infinite\", \"indefinite\", or \"unspecified\". An \"infinite\" retention time indicates that the file will be retained forever. An \"unspecified\" retention time indicates that the file will be retained forever; however, the retention time of the file can be changed to an absolute value. An \"indefinite\" retention time indicates that the file is under Legal-Hold.
                file_path: Specifies the volume relative path of the file
                is_expired: This indicates if the file is under active retention or if the file is past its expiry time.
                retention_period: Duration of retention time file to be locked with,  An \"infinite\" retention period indicates that the file will be retained forever.
                seconds_until_expiry: Specifies the number of seconds until the expiration time of the file.
            """

            kwargs = {}
            if expiry_time is not None:
                kwargs["expiry_time"] = expiry_time
            if file_path is not None:
                kwargs["file_path"] = file_path
            if is_expired is not None:
                kwargs["is_expired"] = is_expired
            if retention_period is not None:
                kwargs["retention_period"] = retention_period
            if seconds_until_expiry is not None:
                kwargs["seconds_until_expiry"] = seconds_until_expiry

            if hasattr(SnaplockFileRetention, "find"):
                resource = SnaplockFileRetention.find(
                    **kwargs
                )
            else:
                resource = SnaplockFileRetention()
            try:
                response = resource.delete(poll=False)
                await _wait_for_job(response)
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to delete SnaplockFileRetention: %s" % err)


