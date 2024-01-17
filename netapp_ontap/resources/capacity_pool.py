r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

## Overview
Capacity pool licenses are installed on and managed by the license manager. Each ONTAP node that is using the capacity pools licensing model is associated with a capacity pool license from which capacity is leased for data aggregates. </br>
This API is used to retrieve information about associations between ONTAP nodes in the cluster and capacity pool licenses. It also reports how much capacity each node is consuming from the capacity pool. </br>
---
## Examples
### Retrieving a collection of capacity pools associated with the cluster
This example retrieves a collection that contains two capacity pool licenses, each of which is associated with an HA pair of nodes in a four-node cluster.
####
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import CapacityPool

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    print(list(CapacityPool.get_collection()))

```
<div class="try_it_out">
<input id="example0_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example0_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example0_result" class="try_it_out_content">
```
[
    CapacityPool(
        {
            "_links": {
                "self": {"href": "/api/cluster/licensing/capacity-pools/390000100"}
            },
            "nodes": [
                {
                    "used_size": 1099511627776,
                    "node": {
                        "uuid": "4ea7a442-86d1-11e0-ae1c-123478563411",
                        "name": "node-1",
                    },
                },
                {
                    "used_size": 1099511627776,
                    "node": {
                        "uuid": "4ea7a442-86d1-11e0-ae1c-123478563412",
                        "name": "node-2",
                    },
                },
            ],
            "serial_number": "390000100",
            "license_manager": {
                "_links": {
                    "self": {
                        "href": "/api/cluster/licensing/license-managers/4ea7a442-86d1-11e0-ae1c-112233445566"
                    }
                },
                "uuid": "4ea7a442-86d1-11e0-ae1c-112233445566",
            },
        }
    ),
    CapacityPool(
        {
            "_links": {
                "self": {"href": "/api/cluster/licensing/capacity-pools/390000101"}
            },
            "nodes": [
                {
                    "used_size": 2199023255552,
                    "node": {
                        "uuid": "4ea7a442-86d1-11e0-ae1c-123478563413",
                        "name": "node-3",
                    },
                },
                {
                    "used_size": 2199023255552,
                    "node": {
                        "uuid": "4ea7a442-86d1-11e0-ae1c-123478563414",
                        "name": "node-4",
                    },
                },
            ],
            "serial_number": "390000101",
            "license_manager": {
                "_links": {
                    "self": {
                        "href": "/api/cluster/licensing/license-managers/4ea7a442-86d1-11e0-ae1c-112233445566"
                    }
                },
                "uuid": "4ea7a442-86d1-11e0-ae1c-112233445566",
            },
        }
    ),
]

```
</div>
</div>

### Retrieving information about nodes associated with a specific capacity pool license
This example retrieves information about the nodes that are associated with a capacity pool license of the serial number 390000100.
####
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import CapacityPool

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = CapacityPool(serial_number=390000100)
    resource.get()
    print(resource)

```
<div class="try_it_out">
<input id="example1_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example1_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example1_result" class="try_it_out_content">
```
CapacityPool(
    {
        "_links": {"self": {"href": "/api/cluster/licensing/capacity-pools/390000100"}},
        "nodes": [
            {
                "used_size": 1099511627776,
                "node": {
                    "uuid": "4ea7a442-86d1-11e0-ae1c-123478563411",
                    "name": "node-1",
                },
            },
            {
                "used_size": 1099511627776,
                "node": {
                    "uuid": "4ea7a442-86d1-11e0-ae1c-123478563412",
                    "name": "node-2",
                },
            },
        ],
        "serial_number": "390000100",
        "license_manager": {
            "_links": {
                "self": {
                    "href": "/api/cluster/licensing/license-managers/4ea7a442-86d1-11e0-ae1c-112233445566"
                }
            },
            "uuid": "4ea7a442-86d1-11e0-ae1c-112233445566",
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


__all__ = ["CapacityPool", "CapacityPoolSchema"]
__pdoc__ = {
    "CapacityPoolSchema.resource": False,
    "CapacityPoolSchema.opts": False,
    "CapacityPool.capacity_pool_show": False,
    "CapacityPool.capacity_pool_create": False,
    "CapacityPool.capacity_pool_modify": False,
    "CapacityPool.capacity_pool_delete": False,
}


class CapacityPoolSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the CapacityPool object"""

    links = marshmallow_fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE, allow_none=True)
    r""" The links field of the capacity_pool."""

    license_manager = marshmallow_fields.Nested("netapp_ontap.resources.license_manager.LicenseManagerSchema", data_key="license_manager", unknown=EXCLUDE, allow_none=True)
    r""" The license_manager field of the capacity_pool."""

    nodes = marshmallow_fields.List(marshmallow_fields.Nested("netapp_ontap.models.capacity_pool_node.CapacityPoolNodeSchema", unknown=EXCLUDE, allow_none=True), data_key="nodes", allow_none=True)
    r""" Nodes in the cluster associated with this capacity pool."""

    serial_number = marshmallow_fields.Str(
        data_key="serial_number",
        allow_none=True,
    )
    r""" Serial number of the capacity pool license.

Example: 390000100"""

    @property
    def resource(self):
        return CapacityPool

    gettable_fields = [
        "links",
        "license_manager.links",
        "license_manager.uuid",
        "nodes",
        "serial_number",
    ]
    """links,license_manager.links,license_manager.uuid,nodes,serial_number,"""

    patchable_fields = [
        "license_manager.links",
        "license_manager.uuid",
        "nodes",
        "serial_number",
    ]
    """license_manager.links,license_manager.uuid,nodes,serial_number,"""

    postable_fields = [
        "license_manager.links",
        "license_manager.uuid",
        "nodes",
        "serial_number",
    ]
    """license_manager.links,license_manager.uuid,nodes,serial_number,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in CapacityPool.get_collection(fields=field)]
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
            raise NetAppRestError("CapacityPool modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class CapacityPool(Resource):
    r""" Information on a capacity pool license and how it is associated with the cluster. """

    _schema = CapacityPoolSchema
    _path = "/api/cluster/licensing/capacity-pools"
    _keys = ["serial_number"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves a collection of capacity pools.
### Learn more
* [`DOC /cluster/licensing/capacity-pools`](#docs-cluster-cluster_licensing_capacity-pools)
### Related ONTAP commands
* `system license show-status`
* `system license show`
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="capacity pool show")
        def capacity_pool_show(
            fields: List[Choices.define(["serial_number", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of CapacityPool resources

            Args:
                serial_number: Serial number of the capacity pool license.
            """

            kwargs = {}
            if serial_number is not None:
                kwargs["serial_number"] = serial_number
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return CapacityPool.get_collection(
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all CapacityPool resources that match the provided query"""
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
        """Returns a list of RawResources that represent CapacityPool resources that match the provided query"""
        return super()._get_collection(
            *args, connection=connection, max_records=max_records, raw=True, **kwargs
        )

    fast_get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)




    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a collection of capacity pools.
### Learn more
* [`DOC /cluster/licensing/capacity-pools`](#docs-cluster-cluster_licensing_capacity-pools)
### Related ONTAP commands
* `system license show-status`
* `system license show`
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)

    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves information about the capacity pool.
### Learn more
* [`DOC /cluster/licensing/capacity-pools`](#docs-cluster-cluster_licensing_capacity-pools)
### Related ONTAP commands
* `system license show-status`
* `system license show`
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)





