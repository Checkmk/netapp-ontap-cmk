r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

## Overview
This API can be used to get the port information for an ethernet switch used in a cluster or storage networks. This API supports GET only. The GET operation returns a list of ports with status and configuration information.
## Examples
### Retrieving the ports for ethernet switches
The following example retrieves the ethernet switch ports for all the ethernet switches used for cluster and/or storage networks.
Note that if the <i>fields=*</i> parameter is not specified, the fields identity.number, statistics, and mac_address are not returned.
Filters can be added on the fields to limit the results.
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import SwitchPort

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    print(list(SwitchPort.get_collection(fields="*")))

```
<div class="try_it_out">
<input id="example0_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example0_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example0_result" class="try_it_out_content">
```
[
    SwitchPort(
        {
            "speed": 100000,
            "statistics": {
                "transmit_raw": {"discards": 0, "errors": 0, "packets": 206717534},
                "receive_raw": {"discards": 0, "errors": 0, "packets": 1616467751},
            },
            "state": "up",
            "switch": {
                "_links": {
                    "self": {
                        "href": "/api/network/ethernet/switches/RTP-CS01-510R11(FOC22092K12)"
                    }
                },
                "name": "RTP-CS01-510R11(FOC22092K12)",
            },
            "isl": False,
            "mtu": 9216,
            "configured": "up",
            "vlan_id": [1, 17, 18, 92],
            "remote_port": {
                "device": {
                    "node": {
                        "_links": {
                            "self": {
                                "href": "/api/cluster/nodes/54c0f036-8a3a-11ea-893d-00a098fd726d"
                            }
                        },
                        "uuid": "54c0f036-8a3a-11ea-893d-00a098fd726d",
                        "name": "stiA400-311",
                    }
                },
                "name": "e3a",
                "mtu": 9000,
            },
            "identity": {"index": 436207616, "number": 1, "name": "Ethernet1/1"},
            "_links": {
                "self": {
                    "href": "/api/network/ethernet/switch/ports/RTP-CS01-510R11%28FOC22092K12%29/Ethernet1%2F1/436207616"
                }
            },
            "mac_address": "00:be:75:ae:2a:d4",
            "duplex_type": "full_duplex",
        }
    ),
    SwitchPort(
        {
            "speed": 100000,
            "statistics": {
                "transmit_raw": {"discards": 0, "errors": 0, "packets": 0},
                "receive_raw": {"discards": 0, "errors": 0, "packets": 0},
            },
            "state": "down",
            "switch": {
                "_links": {
                    "self": {
                        "href": "/api/network/ethernet/switches/RTP-CS01-510R11(FOC22092K12)"
                    }
                },
                "name": "RTP-CS01-510R11(FOC22092K12)",
            },
            "isl": False,
            "mtu": 9216,
            "configured": "up",
            "vlan_id": [1, 17, 18, 92],
            "identity": {"index": 436212736, "number": 11, "name": "Ethernet1/11"},
            "_links": {
                "self": {
                    "href": "/api/network/ethernet/switch/ports/RTP-CS01-510R11%28FOC22092K12%29/Ethernet1%2F11/436212736"
                }
            },
            "mac_address": "00be75ae2afc",
            "duplex_type": "unknown",
        }
    ),
    SwitchPort(
        {
            "speed": 100000,
            "statistics": {
                "transmit_raw": {"discards": 0, "errors": 0, "packets": 2429595607},
                "receive_raw": {"discards": 0, "errors": 0, "packets": 332013844},
            },
            "state": "up",
            "switch": {
                "_links": {
                    "self": {
                        "href": "/api/network/ethernet/switches/RTP-SS01-510R10(FOC22170DFR)"
                    }
                },
                "name": "RTP-SS01-510R10(FOC22170DFR)",
            },
            "isl": False,
            "mtu": 9216,
            "configured": "up",
            "vlan_id": [1, 30],
            "remote_port": {
                "device": {
                    "shelf": {
                        "_links": {
                            "self": {
                                "href": "/api/storage/shelves/12439000444923584512"
                            }
                        },
                        "name": "1.1",
                        "uid": "12439000444923584512",
                        "module": "B",
                    }
                },
                "name": "e0a",
                "mtu": 9000,
            },
            "identity": {"index": 436212224, "number": 10, "name": "Ethernet1/10"},
            "_links": {
                "self": {
                    "href": "/api/network/ethernet/switch/ports/RTP-SS01-510R10%28FOC22170DFR%29/Ethernet1%2F10/436212224"
                }
            },
            "mac_address": "00fcbaead548",
            "duplex_type": "full_duplex",
        }
    ),
]

```
</div>
</div>

---
### Retrieving a ports on an ethernet switch
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import SwitchPort

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = SwitchPort(
        switch="RTP-SS02-510R10(FOC22131U6T)",
        **{"identity.index": "436211712", "identity.name": "Ethernet1/9"}
    )
    resource.get()
    print(resource)

```
<div class="try_it_out">
<input id="example1_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example1_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example1_result" class="try_it_out_content">
```
SwitchPort(
    {
        "speed": 100000,
        "statistics": {
            "transmit_raw": {"discards": 0, "errors": 0, "packets": 337898026},
            "receive_raw": {"discards": 0, "errors": 0, "packets": 4012559315},
        },
        "state": "up",
        "switch": {
            "_links": {
                "self": {
                    "href": "/api/network/ethernet/switches/RTP-SS02-510R10(FOC22131U6T)"
                }
            },
            "name": "RTP-SS02-510R10(FOC22131U6T)",
        },
        "isl": False,
        "mtu": 9216,
        "configured": "up",
        "vlan_id": [1, 30],
        "remote_port": {
            "device": {
                "shelf": {
                    "_links": {
                        "self": {"href": "/api/storage/shelves/12439000444923584512"}
                    },
                    "name": "1.1",
                    "uid": "12439000444923584512",
                    "module": "A",
                }
            },
            "name": "e0a",
            "mtu": 9000,
        },
        "identity": {"index": 436211712, "number": 9, "name": "Ethernet1/9"},
        "_links": {
            "self": {
                "href": "/api/network/ethernet/switch/ports/RTP-SS02-510R10%28FOC22131U6T%29/Ethernet1%2F9/436211712"
            }
        },
        "mac_address": "00fcbaea7228",
        "duplex_type": "full_duplex",
    }
)

```
</div>
</div>

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


__all__ = ["SwitchPort", "SwitchPortSchema"]
__pdoc__ = {
    "SwitchPortSchema.resource": False,
    "SwitchPortSchema.opts": False,
    "SwitchPort.switch_port_show": False,
    "SwitchPort.switch_port_create": False,
    "SwitchPort.switch_port_modify": False,
    "SwitchPort.switch_port_delete": False,
}


class SwitchPortSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the SwitchPort object"""

    links = marshmallow_fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE, allow_none=True)
    r""" The links field of the switch_port."""

    configured = marshmallow_fields.Str(
        data_key="configured",
        validate=enum_validation(['down', 'testing', 'up']),
        allow_none=True,
    )
    r""" Administrative Status.

Valid choices:

* down
* testing
* up"""

    duplex_type = marshmallow_fields.Str(
        data_key="duplex_type",
        validate=enum_validation(['full_duplex', 'half_duplex', 'unknown']),
        allow_none=True,
    )
    r""" Duplex Settings.

Valid choices:

* full_duplex
* half_duplex
* unknown"""

    identity = marshmallow_fields.Nested("netapp_ontap.models.switch_port_identity.SwitchPortIdentitySchema", data_key="identity", unknown=EXCLUDE, allow_none=True)
    r""" The identity field of the switch_port."""

    isl = marshmallow_fields.Boolean(
        data_key="isl",
        allow_none=True,
    )
    r""" Is configured as an ISL link."""

    mac_address = marshmallow_fields.Str(
        data_key="mac_address",
        allow_none=True,
    )
    r""" MAC Address."""

    mtu = Size(
        data_key="mtu",
        allow_none=True,
    )
    r""" MTU."""

    remote_port = marshmallow_fields.Nested("netapp_ontap.models.switch_port_remote_port.SwitchPortRemotePortSchema", data_key="remote_port", unknown=EXCLUDE, allow_none=True)
    r""" The remote_port field of the switch_port."""

    speed = Size(
        data_key="speed",
        allow_none=True,
    )
    r""" Interface Speed(Mbps)."""

    state = marshmallow_fields.Str(
        data_key="state",
        validate=enum_validation(['dormant', 'down', 'lower_layer_down', 'not_present', 'testing', 'unknown', 'up']),
        allow_none=True,
    )
    r""" Operational Status.

Valid choices:

* dormant
* down
* lower_layer_down
* not_present
* testing
* unknown
* up"""

    statistics = marshmallow_fields.Nested("netapp_ontap.models.switch_port_statistics.SwitchPortStatisticsSchema", data_key="statistics", unknown=EXCLUDE, allow_none=True)
    r""" The statistics field of the switch_port."""

    switch = marshmallow_fields.Nested("netapp_ontap.resources.switch.SwitchSchema", data_key="switch", unknown=EXCLUDE, allow_none=True)
    r""" The switch field of the switch_port."""

    type = marshmallow_fields.Str(
        data_key="type",
        validate=enum_validation(['ethernetcsmacd', 'fastetherfx', 'fibrechannel', 'gigabitethernet', 'ieee8023adlag', 'other', 'propvirtual', 'softwareloopback', 'tunnel']),
        allow_none=True,
    )
    r""" Interface Type.

Valid choices:

* ethernetcsmacd
* fastetherfx
* fibrechannel
* gigabitethernet
* ieee8023adlag
* other
* propvirtual
* softwareloopback
* tunnel"""

    vlan_id = marshmallow_fields.List(Size, data_key="vlan_id", allow_none=True)
    r""" The vlan_id field of the switch_port."""

    @property
    def resource(self):
        return SwitchPort

    gettable_fields = [
        "links",
        "configured",
        "duplex_type",
        "identity",
        "isl",
        "mac_address",
        "mtu",
        "remote_port",
        "speed",
        "state",
        "statistics",
        "switch.links",
        "switch.name",
        "type",
        "vlan_id",
    ]
    """links,configured,duplex_type,identity,isl,mac_address,mtu,remote_port,speed,state,statistics,switch.links,switch.name,type,vlan_id,"""

    patchable_fields = [
        "identity",
        "remote_port",
        "vlan_id",
    ]
    """identity,remote_port,vlan_id,"""

    postable_fields = [
        "identity",
        "remote_port",
        "vlan_id",
    ]
    """identity,remote_port,vlan_id,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in SwitchPort.get_collection(fields=field)]
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
            raise NetAppRestError("SwitchPort modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class SwitchPort(Resource):
    r""" Ethernet Switch Port REST API """

    _schema = SwitchPortSchema
    _path = "/api/network/ethernet/switch/ports"
    _keys = ["switch", "identity.name", "identity.index"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves the ethernet switch ports.
### Related ONTAP commands
* `system switch ethernet interface show`
### Learn more
* [`DOC /network/ethernet/switch/ports`](#docs-networking-network_ethernet_switch_ports)
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="switch port show")
        def switch_port_show(
            fields: List[Choices.define(["configured", "duplex_type", "isl", "mac_address", "mtu", "speed", "state", "type", "vlan_id", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of SwitchPort resources

            Args:
                configured: Administrative Status.
                duplex_type: Duplex Settings.
                isl: Is configured as an ISL link.
                mac_address: MAC Address.
                mtu: MTU.
                speed: Interface Speed(Mbps).
                state: Operational Status.
                type: Interface Type.
                vlan_id: 
            """

            kwargs = {}
            if configured is not None:
                kwargs["configured"] = configured
            if duplex_type is not None:
                kwargs["duplex_type"] = duplex_type
            if isl is not None:
                kwargs["isl"] = isl
            if mac_address is not None:
                kwargs["mac_address"] = mac_address
            if mtu is not None:
                kwargs["mtu"] = mtu
            if speed is not None:
                kwargs["speed"] = speed
            if state is not None:
                kwargs["state"] = state
            if type is not None:
                kwargs["type"] = type
            if vlan_id is not None:
                kwargs["vlan_id"] = vlan_id
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return SwitchPort.get_collection(
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all SwitchPort resources that match the provided query"""
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
        """Returns a list of RawResources that represent SwitchPort resources that match the provided query"""
        return super()._get_collection(
            *args, connection=connection, max_records=max_records, raw=True, **kwargs
        )

    fast_get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)




    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the ethernet switch ports.
### Related ONTAP commands
* `system switch ethernet interface show`
### Learn more
* [`DOC /network/ethernet/switch/ports`](#docs-networking-network_ethernet_switch_ports)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)

    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves an ethernet switch port.
### Related ONTAP commands
* `system switch ethernet interface show`

### Learn more
* [`DOC /network/ethernet/switch/ports`](#docs-networking-network_ethernet_switch_ports)"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)





