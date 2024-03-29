r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

## Overview
An iSCSI session is one or more TCP connections that link an iSCSI initiator with an iSCSI target. TCP connections can be added and removed from an iSCSI session by the iSCSI initiator. Across all TCP connections within an iSCSI session, an initiator sees one and the same target. After the connection is established, iSCSI control, data, and status messages are communicated over the session.<br/>
The iSCSI sessions REST API provides information about iSCSI initiators that have successfully logged in to ONTAP.
## Examples
### Retrieving all iSCSI sessions
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import IscsiSession

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    print(list(IscsiSession.get_collection()))

```
<div class="try_it_out">
<input id="example0_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example0_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example0_result" class="try_it_out_content">
```
[
    IscsiSession(
        {
            "svm": {
                "_links": {
                    "self": {
                        "href": "/api/svm/svms/a009a9e7-4081-b576-7575-ada21efcaf16"
                    }
                },
                "uuid": "a009a9e7-4081-b576-7575-ada21efcaf16",
                "name": "svm1",
            },
            "target_portal_group": "iscsi_lif1",
            "_links": {
                "self": {
                    "href": "/api/protocols/san/iscsi/sessions/a009a9e7-4081-b576-7575-ada21efcaf16/iscsi_lif1/10"
                }
            },
            "tsih": 10,
        }
    ),
    IscsiSession(
        {
            "svm": {
                "_links": {
                    "self": {
                        "href": "/api/svm/svms/b009a9e7-4081-b576-7575-ada21efcaf16"
                    }
                },
                "uuid": "b009a9e7-4081-b576-7575-ada21efcaf16",
                "name": "svm2",
            },
            "target_portal_group": "iscsi_lif2",
            "_links": {
                "self": {
                    "href": "/api/protocols/san/iscsi/sessions/b009a9e7-4081-b576-7575-ada21efcaf16/iscsi_lif2/11"
                }
            },
            "tsih": 11,
        }
    ),
]

```
</div>
</div>

---
### Retrieving all of the iSCSI sessions under the target portal group _iscsi_lif1_
The `tpgroup` query parameter is used to perform the query.
<br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import IscsiSession

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    print(list(IscsiSession.get_collection(tpgroup="iscsi_lif1")))

```
<div class="try_it_out">
<input id="example1_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example1_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example1_result" class="try_it_out_content">
```
[
    IscsiSession(
        {
            "svm": {
                "_links": {
                    "self": {
                        "href": "/api/svm/svms/a009a9e7-4081-b576-7575-ada21efcaf16"
                    }
                },
                "uuid": "a009a9e7-4081-b576-7575-ada21efcaf16",
                "name": "svm1",
            },
            "target_portal_group": "iscsi_lif1",
            "_links": {
                "self": {
                    "href": "/api/protocols/san/iscsi/sessions/a009a9e7-4081-b576-7575-ada21efcaf16/iscsi_lif1/10"
                }
            },
            "tsih": 10,
        }
    )
]

```
</div>
</div>

---
### Retrieving an iSCSI session
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import IscsiSession

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = IscsiSession(
        tsih=10,
        tpgroup="iscsi_lif1",
        **{"svm.uuid": "a009a9e7-4081-b576-7575-ada21efcaf16"}
    )
    resource.get()
    print(resource)

```
<div class="try_it_out">
<input id="example2_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example2_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example2_result" class="try_it_out_content">
```
IscsiSession(
    {
        "svm": {
            "_links": {
                "self": {"href": "/api/svm/svms/a009a9e7-4081-b576-7575-ada21efcaf16"}
            },
            "uuid": "a009a9e7-4081-b576-7575-ada21efcaf16",
            "name": "svm1",
        },
        "target_portal_group": "iscsi_lif1",
        "connections": [
            {
                "cid": 1,
                "interface": {
                    "_links": {
                        "self": {
                            "href": "/api/network/ip/interfaces/c15439b4-dbb4-11e8-90ac-005056bba882"
                        }
                    },
                    "name": "iscsi_lif1",
                    "ip": {"port": 3260, "address": "192.168.0.1"},
                    "uuid": "c15439b4-dbb4-11e8-90ac-005056bba882",
                },
                "authentication_type": "chap",
                "initiator_address": {"port": 43827, "address": "10.224.123.85"},
            }
        ],
        "target_portal_group_tag": 1027,
        "_links": {
            "self": {
                "href": "/api/protocols/san/iscsi/sessions/a009a9e7-4081-b576-7575-ada21efcaf16/iscsi_lif1/10"
            }
        },
        "igroups": [
            {
                "_links": {
                    "self": {
                        "href": "/api/protocols/san/igroups/af7838cd-f993-4faf-90b7-5524787ae1e8"
                    }
                },
                "name": "igroup1",
                "uuid": "af7838cd-f993-4faf-90b7-5524787ae1e8",
            },
            {
                "_links": {
                    "self": {
                        "href": "/api/protocols/san/igroups/bf7838cd-f993-4faf-90b7-5524787ae1e8"
                    }
                },
                "name": "igroup2",
                "uuid": "bf7838cd-f993-4faf-90b7-5524787ae1e8",
            },
        ],
        "tsih": 10,
        "isid": "61:62:63:64:65:00",
        "initiator": {
            "comment": "Example information about this initiator",
            "name": "iqn.1994-05.com.example:string",
        },
    }
)

```
</div>
</div>
"""

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


__all__ = ["IscsiSession", "IscsiSessionSchema"]
__pdoc__ = {
    "IscsiSessionSchema.resource": False,
    "IscsiSessionSchema.opts": False,
    "IscsiSession.iscsi_session_show": False,
    "IscsiSession.iscsi_session_create": False,
    "IscsiSession.iscsi_session_modify": False,
    "IscsiSession.iscsi_session_delete": False,
}


class IscsiSessionSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the IscsiSession object"""

    links = marshmallow_fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE, allow_none=True)
    r""" The links field of the iscsi_session."""

    connections = marshmallow_fields.List(marshmallow_fields.Nested("netapp_ontap.models.iscsi_connection.IscsiConnectionSchema", unknown=EXCLUDE, allow_none=True), data_key="connections", allow_none=True)
    r""" The iSCSI connections that make up the iSCSI session."""

    igroups = marshmallow_fields.List(marshmallow_fields.Nested("netapp_ontap.models.igroup_nested_records.IgroupNestedRecordsSchema", unknown=EXCLUDE, allow_none=True), data_key="igroups", allow_none=True)
    r""" The initiator groups in which the initiator is a member."""

    initiator = marshmallow_fields.Nested("netapp_ontap.models.iscsi_session_initiator.IscsiSessionInitiatorSchema", data_key="initiator", unknown=EXCLUDE, allow_none=True)
    r""" The initiator field of the iscsi_session."""

    isid = marshmallow_fields.Str(
        data_key="isid",
        allow_none=True,
    )
    r""" The initiator portion of the session identifier specified by the initiator during login.


Example: 61:62:63:64:65:00"""

    svm = marshmallow_fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE, allow_none=True)
    r""" The svm field of the iscsi_session."""

    target_portal_group = marshmallow_fields.Str(
        data_key="target_portal_group",
        allow_none=True,
    )
    r""" The target portal group to which the session belongs.


Example: tpgroup1"""

    target_portal_group_tag = Size(
        data_key="target_portal_group_tag",
        allow_none=True,
    )
    r""" The target portal group tag of the session."""

    tsih = Size(
        data_key="tsih",
        allow_none=True,
    )
    r""" The target session identifier handle (TSIH) of the session."""

    @property
    def resource(self):
        return IscsiSession

    gettable_fields = [
        "links",
        "connections",
        "igroups.links",
        "igroups.name",
        "igroups.uuid",
        "initiator",
        "isid",
        "svm.links",
        "svm.name",
        "svm.uuid",
        "target_portal_group",
        "target_portal_group_tag",
        "tsih",
    ]
    """links,connections,igroups.links,igroups.name,igroups.uuid,initiator,isid,svm.links,svm.name,svm.uuid,target_portal_group,target_portal_group_tag,tsih,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
    ]
    """"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in IscsiSession.get_collection(fields=field)]
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
            raise NetAppRestError("IscsiSession modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class IscsiSession(Resource):
    r""" An iSCSI session is one or more TCP connections that link an iSCSI initiator with an iSCSI target. TCP connections can be added and removed from an iSCSI session by the iSCSI initiator. Across all TCP connections within an iSCSI session, an initiator sees one and the same target. After the connection is established, iSCSI control, data, and status messages are communicated over the session. """

    _schema = IscsiSessionSchema
    _path = "/api/protocols/san/iscsi/sessions"
    _keys = ["svm.uuid", "tpgroup", "tsih"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves iSCSI sessions.
### Related ONTAP commands
* `vserver iscsi connection show`
* `vserver iscsi session parameter show`
* `vserver iscsi session show`
### Learn more
* [`DOC /protocols/san/iscsi/sessions`](#docs-SAN-protocols_san_iscsi_sessions)
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="iscsi session show")
        def iscsi_session_show(
            fields: List[Choices.define(["isid", "target_portal_group", "target_portal_group_tag", "tsih", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of IscsiSession resources

            Args:
                isid: The initiator portion of the session identifier specified by the initiator during login. 
                target_portal_group: The target portal group to which the session belongs. 
                target_portal_group_tag: The target portal group tag of the session. 
                tsih: The target session identifier handle (TSIH) of the session. 
            """

            kwargs = {}
            if isid is not None:
                kwargs["isid"] = isid
            if target_portal_group is not None:
                kwargs["target_portal_group"] = target_portal_group
            if target_portal_group_tag is not None:
                kwargs["target_portal_group_tag"] = target_portal_group_tag
            if tsih is not None:
                kwargs["tsih"] = tsih
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return IscsiSession.get_collection(
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all IscsiSession resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)


    @classmethod
    def fast_get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["RawResource"]:
        """Returns a list of RawResources that represent IscsiSession resources that match the provided query"""
        return super()._get_collection(
            *args, connection=connection, max_records=max_records, raw=True, **kwargs
        )

    fast_get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)




    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves iSCSI sessions.
### Related ONTAP commands
* `vserver iscsi connection show`
* `vserver iscsi session parameter show`
* `vserver iscsi session show`
### Learn more
* [`DOC /protocols/san/iscsi/sessions`](#docs-SAN-protocols_san_iscsi_sessions)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)

    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves an iSCSI session.
### Related ONTAP commands
* `vserver iscsi connection show`
* `vserver iscsi session parameter show`
* `vserver iscsi session show`
### Learn more
* [`DOC /protocols/san/iscsi/sessions`](#docs-SAN-protocols_san_iscsi_sessions)
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)





