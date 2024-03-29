r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

## Overview
FPolicy is an infrastructure component of ONTAP that enables partner applications to connect to ONTAP in order to monitor and set file access permissions. Every time a client accesses a file from a storage system, based on the configuration of FPolicy, the partner application is notified about file access. This enables partners to set restrictions on files that are created or accessed on the storage system. FPolicy also allows you to create file policies that specify file operation permissions according to file type. For example, you can restrict certain file types, such as .jpeg and .mp3 files, from being stored on the storage system. FPolicy can monitor file access from CIFS and NFS clients.</br>
As part of FPolicy configuration, you can specify an FPolicy engine which defines the external FPolicy server, FPolicy events, which defines the protocol and file operations to monitor and the FPolicy policy that acts as a container for the FPolicy engine and FPolicy events. It provides a way for policy management functions, such as policy enabling and disabling.
## Examples
### Creating an FPolicy configuration
To create an FPolicy for an SVM use the following API. Note that the <i>return_records=true</i> query parameter is used to obtain the newly created entry in the response.
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Fpolicy

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Fpolicy()
    resource.engines = [
        {
            "name": "engine1",
            "port": 9876,
            "primary_servers": ["10.132.145.22", "10.140.101.109"],
            "secondary_servers": ["10.132.145.20", "10.132.145.21"],
            "type": "synchronous",
            "format": "xml",
        }
    ]
    resource.events = [
        {
            "file_operations": {"read": True, "write": True},
            "filters": {"monitor_ads": True},
            "name": "event_cifs",
            "protocol": "cifs",
            "volume_monitoring": True,
        }
    ]
    resource.policies = [
        {
            "engine": {"name": "engine1"},
            "events": [{"name": "event_cifs"}],
            "mandatory": True,
            "name": "pol0",
            "priority": 1,
            "scope": {"include_volumes": ["vol1"]},
        }
    ]
    resource.persistent_stores = [{"name": "ps1", "volume": "psvol"}]
    resource.svm = {"name": "vs1", "uuid": "b34f5e3d-01d0-11e9-8f63-0050568ea311"}
    resource.post(hydrate=True)
    print(resource)

```
<div class="try_it_out">
<input id="example0_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example0_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example0_result" class="try_it_out_content">
```
Fpolicy(
    {
        "svm": {"uuid": "b34f5e3d-01d0-11e9-8f63-0050568ea311", "name": "vs1"},
        "engines": [
            {
                "port": 9876,
                "type": "synchronous",
                "primary_servers": ["10.132.145.22", "10.140.101.109"],
                "secondary_servers": ["10.132.145.20", "10.132.145.21"],
                "name": "engine1",
                "format": "xml",
            }
        ],
        "persistent_stores": [{"name": "ps1", "volume": "psvol"}],
        "events": [
            {
                "file_operations": {"read": True, "write": True},
                "protocol": "cifs",
                "volume_monitoring": True,
                "filters": {"monitor_ads": True},
                "name": "event_cifs",
            }
        ],
        "policies": [
            {
                "engine": {"name": "engine1"},
                "priority": 1,
                "events": [{"name": "event_cifs"}],
                "mandatory": True,
                "name": "pol0",
                "scope": {"include_volumes": ["vol1"]},
            }
        ],
    }
)

```
</div>
</div>

---
### Retrieving the FPolicy configuration for all the SVMs in the cluster
---
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Fpolicy

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    print(list(Fpolicy.get_collection(fields="*", return_timeout=15)))

```
<div class="try_it_out">
<input id="example1_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example1_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example1_result" class="try_it_out_content">
```
[
    Fpolicy(
        {
            "svm": {"uuid": "b34f5e3d-01d0-11e9-8f63-0050568ea311", "name": "vs1"},
            "engines": [
                {
                    "port": 9876,
                    "type": "synchronous",
                    "primary_servers": ["10.132.145.22", "10.140.101.109"],
                    "secondary_servers": ["10.132.145.20", "10.132.145.21"],
                    "name": "engine1",
                    "format": "xml",
                }
            ],
            "persistent_stores": [{"name": "ps1", "volume": "psvol"}],
            "events": [
                {
                    "file_operations": {
                        "rename": False,
                        "open": False,
                        "read": True,
                        "create": False,
                        "link": False,
                        "write": True,
                        "delete": False,
                        "close": False,
                        "setattr": False,
                        "create_dir": False,
                        "delete_dir": False,
                        "rename_dir": False,
                        "getattr": False,
                        "symlink": False,
                        "lookup": False,
                    },
                    "protocol": "cifs",
                    "volume_monitoring": True,
                    "filters": {
                        "setattr_with_sacl_change": False,
                        "monitor_ads": True,
                        "setattr_with_size_change": False,
                        "close_with_modification": False,
                        "setattr_with_owner_change": False,
                        "write_with_size_change": False,
                        "setattr_with_group_change": False,
                        "first_read": False,
                        "first_write": False,
                        "setattr_with_mode_change": False,
                        "close_without_modification": False,
                        "setattr_with_dacl_change": False,
                        "setattr_with_creation_time_change": False,
                        "exclude_directory": False,
                        "offline_bit": False,
                        "setattr_with_access_time_change": False,
                        "close_with_read": False,
                        "setattr_with_allocation_size_change": False,
                        "open_with_write_intent": False,
                        "open_with_delete_intent": False,
                        "setattr_with_modify_time_change": False,
                    },
                    "name": "event_cifs",
                }
            ],
            "policies": [
                {
                    "allow_privileged_access": False,
                    "engine": {"name": "engine1"},
                    "priority": 1,
                    "events": [{"name": "event_cifs"}],
                    "enabled": True,
                    "persistent_store": "ps1",
                    "mandatory": True,
                    "passthrough_read": False,
                    "name": "pol0",
                    "scope": {"include_volumes": ["vol1"]},
                }
            ],
        }
    )
]

```
</div>
</div>

---
### Retrieving an FPolicy configuration for a particular SVM
---
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Fpolicy

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Fpolicy(**{"svm.uuid": "b34f5e3d-01d0-11e9-8f63-0050568ea311"})
    resource.get(fields="*", return_timeout=15)
    print(resource)

```
<div class="try_it_out">
<input id="example2_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example2_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example2_result" class="try_it_out_content">
```
Fpolicy(
    {
        "svm": {"uuid": "b34f5e3d-01d0-11e9-8f63-0050568ea311", "name": "vs1"},
        "engines": [
            {
                "port": 9876,
                "type": "synchronous",
                "primary_servers": ["10.132.145.22", "10.140.101.109"],
                "secondary_servers": ["10.132.145.20", "10.132.145.21"],
                "name": "engine1",
                "format": "xml",
            }
        ],
        "persistent_stores": [{"name": "ps1", "volume": "psvol"}],
        "events": [
            {
                "file_operations": {
                    "rename": False,
                    "open": False,
                    "read": True,
                    "create": False,
                    "link": False,
                    "write": True,
                    "delete": False,
                    "close": False,
                    "setattr": False,
                    "create_dir": False,
                    "delete_dir": False,
                    "rename_dir": False,
                    "getattr": False,
                    "symlink": False,
                    "lookup": False,
                },
                "protocol": "cifs",
                "volume_monitoring": True,
                "filters": {
                    "setattr_with_sacl_change": False,
                    "monitor_ads": True,
                    "setattr_with_size_change": False,
                    "close_with_modification": False,
                    "setattr_with_owner_change": False,
                    "write_with_size_change": False,
                    "setattr_with_group_change": False,
                    "first_read": False,
                    "first_write": False,
                    "setattr_with_mode_change": False,
                    "close_without_modification": False,
                    "setattr_with_dacl_change": False,
                    "setattr_with_creation_time_change": False,
                    "exclude_directory": False,
                    "offline_bit": False,
                    "setattr_with_access_time_change": False,
                    "close_with_read": False,
                    "setattr_with_allocation_size_change": False,
                    "open_with_write_intent": False,
                    "open_with_delete_intent": False,
                    "setattr_with_modify_time_change": False,
                },
                "name": "event_cifs",
            }
        ],
        "policies": [
            {
                "allow_privileged_access": False,
                "engine": {"name": "engine1"},
                "priority": 1,
                "events": [{"name": "event_cifs"}],
                "enabled": True,
                "persistent_store": "ps1",
                "mandatory": True,
                "passthrough_read": False,
                "name": "pol0",
                "scope": {"include_volumes": ["vol1"]},
            }
        ],
    }
)

```
</div>
</div>

---
### Deleting an FPolicy configuration for a particular SVM
---
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Fpolicy

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Fpolicy(**{"svm.uuid": "b34f5e3d-01d0-11e9-8f63-0050568ea311"})
    resource.delete()

```

---"""

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


__all__ = ["Fpolicy", "FpolicySchema"]
__pdoc__ = {
    "FpolicySchema.resource": False,
    "FpolicySchema.opts": False,
    "Fpolicy.fpolicy_show": False,
    "Fpolicy.fpolicy_create": False,
    "Fpolicy.fpolicy_modify": False,
    "Fpolicy.fpolicy_delete": False,
}


class FpolicySchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the Fpolicy object"""

    links = marshmallow_fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE, allow_none=True)
    r""" The links field of the fpolicy."""

    engines = marshmallow_fields.List(marshmallow_fields.Nested("netapp_ontap.models.fpolicy_engines.FpolicyEnginesSchema", unknown=EXCLUDE, allow_none=True), data_key="engines", allow_none=True)
    r""" The engines field of the fpolicy."""

    events = marshmallow_fields.List(marshmallow_fields.Nested("netapp_ontap.models.fpolicy_events.FpolicyEventsSchema", unknown=EXCLUDE, allow_none=True), data_key="events", allow_none=True)
    r""" The events field of the fpolicy."""

    persistent_stores = marshmallow_fields.List(marshmallow_fields.Nested("netapp_ontap.models.fpolicy_persistent_stores.FpolicyPersistentStoresSchema", unknown=EXCLUDE, allow_none=True), data_key="persistent_stores", allow_none=True)
    r""" The persistent_stores field of the fpolicy."""

    policies = marshmallow_fields.List(marshmallow_fields.Nested("netapp_ontap.models.fpolicy_policies.FpolicyPoliciesSchema", unknown=EXCLUDE, allow_none=True), data_key="policies", allow_none=True)
    r""" The policies field of the fpolicy."""

    svm = marshmallow_fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE, allow_none=True)
    r""" The svm field of the fpolicy."""

    @property
    def resource(self):
        return Fpolicy

    gettable_fields = [
        "links",
        "engines",
        "events",
        "persistent_stores",
        "policies",
        "svm.links",
        "svm.name",
        "svm.uuid",
    ]
    """links,engines,events,persistent_stores,policies,svm.links,svm.name,svm.uuid,"""

    patchable_fields = [
        "svm.name",
        "svm.uuid",
    ]
    """svm.name,svm.uuid,"""

    postable_fields = [
        "engines",
        "events",
        "persistent_stores",
        "policies",
        "svm.name",
        "svm.uuid",
    ]
    """engines,events,persistent_stores,policies,svm.name,svm.uuid,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in Fpolicy.get_collection(fields=field)]
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
            raise NetAppRestError("Fpolicy modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class Fpolicy(Resource):
    r""" FPolicy is an infrastructure component of ONTAP that enables partner applications connected to your storage systems to monitor and set file access permissions. Every time a client accesses a file from a storage system, based on the configuration of FPolicy, the partner application is notified about file access. """

    _schema = FpolicySchema
    _path = "/api/protocols/fpolicy"
    _keys = ["svm.uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves an FPolicy configuration.
### Related ONTAP commands
* `fpolicy show`
* `fpolicy policy show`
* `fpolicy policy scope show`
* `fpolicy policy event show`
* `fpolicy policy external-engine show`
* `fpolicy persistent-store show`
### Learn more
* [`DOC /protocols/fpolicy`](#docs-NAS-protocols_fpolicy)
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="fpolicy show")
        def fpolicy_show(
            fields: List[Choices.define(["*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of Fpolicy resources

            Args:
            """

            kwargs = {}
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return Fpolicy.get_collection(
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all Fpolicy resources that match the provided query"""
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
        """Returns a list of RawResources that represent Fpolicy resources that match the provided query"""
        return super()._get_collection(
            *args, connection=connection, max_records=max_records, raw=True, **kwargs
        )

    fast_get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)


    @classmethod
    def post_collection(
        cls,
        records: Iterable["Fpolicy"],
        *args,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> Union[List["Fpolicy"], NetAppResponse]:
        r"""Creates an FPolicy configuration.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create the FPolicy configuration.
### Recommended optional properties
* `engines` -  External server to which the notifications will be sent.
* `events` - File operations to monitor.
* `policies` - Policy configuration which acts as a container for FPolicy event and FPolicy engine.
* `scope` - Scope of the policy. Can be limited to exports, volumes, shares or file extensions.
### Default property values
If not specified in POST, the following default property values are assigned:
* `engines.type` - _synchronous_
* `policies.engine` - _native_
* `policies.mandatory` -  _true_
* `events.volume_monitoring` - _false_
* `events.file_operations.*` - _false_
* `events.filters.*` - _false_
* `events.monitor_fileop_failure.*` - _false_
### Related ONTAP commands
* `fpolicy policy event create`
* `fpolicy policy external-engine create`
* `fpolicy policy create`
* `fpolicy policy scope create`
* `fpolicy enable`
* `fpolicy persistent-store create`
### Learn more
* [`DOC /protocols/fpolicy`](#docs-NAS-protocols_fpolicy)
"""
        return super()._post_collection(
            records, *args, hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    post_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post_collection.__doc__)

    @classmethod
    def delete_collection(
        cls,
        *args,
        records: Iterable["Fpolicy"] = None,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes the FPolicy configuration for the specified SVM. Before deleting the FPolicy configuration, ensure that all policies belonging to the SVM are disabled.
### Related ONTAP commands
* `fpolicy delete`
* `fpolicy policy scope delete`
* `fpolicy policy delete`
* `fpolicy policy event delete`
* `fpolicy policy external-engine delete`
* `fpolicy persistent-store delete`
### Learn more
* [`DOC /protocols/fpolicy`](#docs-NAS-protocols_fpolicy)
"""
        return super()._delete_collection(
            *args, body=body, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)

    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves an FPolicy configuration.
### Related ONTAP commands
* `fpolicy show`
* `fpolicy policy show`
* `fpolicy policy scope show`
* `fpolicy policy event show`
* `fpolicy policy external-engine show`
* `fpolicy persistent-store show`
### Learn more
* [`DOC /protocols/fpolicy`](#docs-NAS-protocols_fpolicy)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)

    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves an FPolicy configuration of an SVM.
### Related ONTAP commands
* `fpolicy show`
* `fpolicy policy show`
* `fpolicy policy scope show`
* `fpolicy policy event show`
* `fpolicy policy external-engine show`
* `fpolicy persistent-store show`
### Learn more
* [`DOC /protocols/fpolicy`](#docs-NAS-protocols_fpolicy)
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)

    def post(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Creates an FPolicy configuration.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create the FPolicy configuration.
### Recommended optional properties
* `engines` -  External server to which the notifications will be sent.
* `events` - File operations to monitor.
* `policies` - Policy configuration which acts as a container for FPolicy event and FPolicy engine.
* `scope` - Scope of the policy. Can be limited to exports, volumes, shares or file extensions.
### Default property values
If not specified in POST, the following default property values are assigned:
* `engines.type` - _synchronous_
* `policies.engine` - _native_
* `policies.mandatory` -  _true_
* `events.volume_monitoring` - _false_
* `events.file_operations.*` - _false_
* `events.filters.*` - _false_
* `events.monitor_fileop_failure.*` - _false_
### Related ONTAP commands
* `fpolicy policy event create`
* `fpolicy policy external-engine create`
* `fpolicy policy create`
* `fpolicy policy scope create`
* `fpolicy enable`
* `fpolicy persistent-store create`
### Learn more
* [`DOC /protocols/fpolicy`](#docs-NAS-protocols_fpolicy)
"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="fpolicy create")
        async def fpolicy_create(
        ) -> ResourceTable:
            """Create an instance of a Fpolicy resource

            Args:
                links: 
                engines: 
                events: 
                persistent_stores: 
                policies: 
                svm: 
            """

            kwargs = {}
            if links is not None:
                kwargs["links"] = links
            if engines is not None:
                kwargs["engines"] = engines
            if events is not None:
                kwargs["events"] = events
            if persistent_stores is not None:
                kwargs["persistent_stores"] = persistent_stores
            if policies is not None:
                kwargs["policies"] = policies
            if svm is not None:
                kwargs["svm"] = svm

            resource = Fpolicy(
                **kwargs
            )
            try:
                response = resource.post(hydrate=True, poll=False)
                await _wait_for_job(response)
                resource.get()
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to create Fpolicy: %s" % err)
            return [resource]


    def delete(
        self,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes the FPolicy configuration for the specified SVM. Before deleting the FPolicy configuration, ensure that all policies belonging to the SVM are disabled.
### Related ONTAP commands
* `fpolicy delete`
* `fpolicy policy scope delete`
* `fpolicy policy delete`
* `fpolicy policy event delete`
* `fpolicy policy external-engine delete`
* `fpolicy persistent-store delete`
### Learn more
* [`DOC /protocols/fpolicy`](#docs-NAS-protocols_fpolicy)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="fpolicy delete")
        async def fpolicy_delete(
        ) -> None:
            """Delete an instance of a Fpolicy resource

            Args:
            """

            kwargs = {}

            if hasattr(Fpolicy, "find"):
                resource = Fpolicy.find(
                    **kwargs
                )
            else:
                resource = Fpolicy()
            try:
                response = resource.delete(poll=False)
                await _wait_for_job(response)
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to delete Fpolicy: %s" % err)


