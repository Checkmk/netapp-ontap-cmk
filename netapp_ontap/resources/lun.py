r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

## Overview
A LUN is the logical representation of storage in a storage area network (SAN).<br/>
The LUN REST API allows you to create, update, delete, and discover LUNs.<br/>
A LUN is located within a volume. Optionally, it can be located within a qtree in a volume.<br/>
A LUN can be created to a specified size using thin or thick provisioning. A LUN can then be renamed, resized, cloned, moved to a different volume and copied. LUNs support the assignment of a quality of service (QoS) policy for performance management or a QoS policy can be assigned to the volume containing the LUN. See the LUN object model to learn more about each of the properties supported by the LUN REST API.<br/>
A LUN must be mapped to an initiator group to grant access to the initiator group's initiators (client hosts). Initiators can then access the LUN and perform I/O over a Fibre Channel (FC) fabric using the FC Protocol or a TCP/IP network using iSCSI.
## Performance monitoring
Performance of a LUN can be monitored by observing the `metric.*` and `statistics.*` properties. These properties show the performance of a LUN in terms of IOPS, latency and throughput. The `metric.*` properties denote an average whereas `statistics.*` properties denote a real-time monotonically increasing value aggregated across all nodes.
## Examples
### Creating a LUN
This example creates a 300 gigabyte, thin-provisioned LUN in SVM _svm1_, volume _vol1_, configured for use by _linux_ initiators. The `return_records` query parameter is used to retrieve properties of the newly created LUN in the POST response.<br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Lun

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Lun()
    resource.svm = {"name": "svm1"}
    resource.os_type = "linux"
    resource.space = {"size": "300G"}
    resource.name = "/vol/vol1/lun1"
    resource.post(hydrate=True)
    print(resource)

```
<div class="try_it_out">
<input id="example0_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example0_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example0_result" class="try_it_out_content">
```
Lun(
    {
        "enabled": True,
        "status": {"container_state": "online", "read_only": False, "state": "online"},
        "class": "regular",
        "_links": {
            "self": {"href": "/api/storage/luns/5a24ae5b-28af-47fb-b129-5adf6cfba0a6"}
        },
        "serial_number": "wf0Iq+N4uck3",
        "location": {
            "logical_unit": "lun1",
            "volume": {
                "_links": {
                    "self": {
                        "href": "/api/storage/volumes/71cd0dba-2a1c-11e9-b682-005056bbc17d"
                    }
                },
                "uuid": "71cd0dba-2a1c-11e9-b682-005056bbc17d",
                "name": "vol1",
            },
        },
        "os_type": "linux",
        "space": {
            "guarantee": {"requested": False, "reserved": False},
            "size": 322163441664,
            "used": 0,
            "scsi_thin_provisioning_support_enabled": False,
        },
        "uuid": "5a24ae5b-28af-47fb-b129-5adf6cfba0a6",
        "svm": {
            "_links": {
                "self": {"href": "/api/svm/svms/6bf967fd-2a1c-11e9-b682-005056bbc17d"}
            },
            "uuid": "6bf967fd-2a1c-11e9-b682-005056bbc17d",
            "name": "svm1",
        },
        "name": "/vol/vol1/lun1",
    }
)

```
</div>
</div>

### Updating a LUN
This example sets the `comment` property of a LUN.<br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Lun

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Lun(uuid="5a24ae5b-28af-47fb-b129-5adf6cfba0a6")
    resource.comment = "Data for the finance department."
    resource.patch()

```

### Retrieving LUNs
This example retrieves summary information for all online LUNs in SVM _svm1_. The `svm.name` and `status.state` query parameters are used to find the desired LUNs.<br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Lun

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    print(list(Lun.get_collection(**{"svm.name": "svm1", "status.state": "online"})))

```
<div class="try_it_out">
<input id="example2_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example2_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example2_result" class="try_it_out_content">
```
[
    Lun(
        {
            "status": {"state": "online"},
            "_links": {
                "self": {
                    "href": "/api/storage/luns/5a24ae5b-28af-47fb-b129-5adf6cfba0a6"
                }
            },
            "uuid": "5a24ae5b-28af-47fb-b129-5adf6cfba0a6",
            "svm": {"name": "svm1"},
            "name": "/vol/vol1/lun1",
        }
    ),
    Lun(
        {
            "status": {"state": "online"},
            "_links": {
                "self": {
                    "href": "/api/storage/luns/c903a978-9bac-4ce9-8237-4a3ba8b13f08"
                }
            },
            "uuid": "c903a978-9bac-4ce9-8237-4a3ba8b13f08",
            "svm": {"name": "svm1"},
            "name": "/vol/vol1/lun2",
        }
    ),
    Lun(
        {
            "status": {"state": "online"},
            "_links": {
                "self": {
                    "href": "/api/storage/luns/7faf0a9e-0a47-4876-8318-3638d5da16bf"
                }
            },
            "uuid": "7faf0a9e-0a47-4876-8318-3638d5da16bf",
            "svm": {"name": "svm1"},
            "name": "/vol/vol2/lun3",
        }
    ),
]

```
</div>
</div>

### Retrieving details for a specific LUN
In this example, the `fields` query parameter is used to request all fields, including advanced fields, that would not otherwise be returned by default for the LUN.<br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Lun

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Lun(uuid="5a24ae5b-28af-47fb-b129-5adf6cfba0a6")
    resource.get(fields="**")
    print(resource)

```
<div class="try_it_out">
<input id="example3_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example3_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example3_result" class="try_it_out_content">
```
Lun(
    {
        "enabled": True,
        "status": {
            "container_state": "online",
            "read_only": False,
            "mapped": True,
            "state": "online",
        },
        "class": "vvol",
        "_links": {
            "self": {
                "href": "/api/storage/luns/5a24ae5b-28af-47fb-b129-5adf6cfba0a6?fields=**"
            }
        },
        "consistency_group": {
            "_links": {
                "self": {
                    "href": "/api/application/consistency-groups/6d657aaf-b57a-5396-82ea-c01329e46c79"
                }
            },
            "name": "vol1",
            "uuid": "6d657aaf-b57a-5396-82ea-c01329e46c79",
        },
        "statistics": {
            "timestamp": "2019-04-09T05:50:42+00:00",
            "latency_raw": {"other": 38298, "total": 38298, "read": 0, "write": 0},
            "status": "ok",
            "iops_raw": {"other": 3, "total": 3, "read": 0, "write": 0},
            "throughput_raw": {"other": 0, "total": 0, "read": 0, "write": 0},
        },
        "auto_delete": False,
        "serial_number": "wf0Iq+N4uck3",
        "location": {
            "logical_unit": "lun1",
            "volume": {
                "_links": {
                    "self": {
                        "href": "/api/storage/volumes/71cd0dba-2a1c-11e9-b682-005056bbc17d"
                    }
                },
                "uuid": "71cd0dba-2a1c-11e9-b682-005056bbc17d",
                "name": "vol1",
            },
        },
        "os_type": "linux",
        "space": {
            "guarantee": {"requested": False, "reserved": False},
            "size": 322163441664,
            "used": 0,
            "scsi_thin_provisioning_support_enabled": False,
        },
        "uuid": "5a24ae5b-28af-47fb-b129-5adf6cfba0a6",
        "metric": {
            "timestamp": "2019-04-09T05:50:15+00:00",
            "throughput": {"other": 0, "total": 0, "read": 0, "write": 0},
            "status": "ok",
            "iops": {"other": 0, "total": 0, "read": 0, "write": 0},
            "duration": "PT15S",
            "latency": {"other": 0, "total": 0, "read": 0, "write": 0},
        },
        "comment": "Data for the finance department.",
        "svm": {
            "_links": {
                "self": {"href": "/api/svm/svms/6bf967fd-2a1c-11e9-b682-005056bbc17d"}
            },
            "uuid": "6bf967fd-2a1c-11e9-b682-005056bbc17d",
            "name": "svm1",
        },
        "vvol": {
            "bindings": [
                {
                    "_links": {
                        "self": {
                            "href": "/api/protocols/san/vvol-bindings/353c7262-be4b-4176-acf3-f1021faa8b64/5a24ae5b-28af-47fb-b129-5adf6cfba0a6"
                        }
                    },
                    "partner": {
                        "_links": {
                            "self": {
                                "href": "/api/storage/luns/353c7262-be4b-4176-acf3-f1021faa8b64"
                            }
                        },
                        "name": "/vol/vol1/pelun1",
                        "uuid": "353c7262-be4b-4176-acf3-f1021faa8b64",
                    },
                    "id": 4304512,
                }
            ],
            "is_bound": True,
        },
        "lun_maps": [
            {
                "_links": {
                    "self": {
                        "href": "/api/protocols/san/lun-maps/5a24ae5b-28af-47fb-b129-5adf6cfba0a6/2b9d57e1-2a66-11e9-b682-005056bbc17d"
                    }
                },
                "igroup": {
                    "_links": {
                        "self": {
                            "href": "/api/protocols/san/igroups/2b9d57e1-2a66-11e9-b682-005056bbc17d"
                        }
                    },
                    "name": "ig1",
                    "uuid": "2b9d57e1-2a66-11e9-b682-005056bbc17d",
                },
                "logical_unit_number": 0,
            }
        ],
        "name": "/vol/vol1/lun1",
    }
)

```
</div>
</div>

### Deleting a LUN
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Lun

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Lun(uuid="c903a978-9bac-4ce9-8237-4a3ba8b13f08")
    resource.delete()

```

---
## LUN data
The LUN REST API also supports reading data from and writing data to a LUN via the REST API as multipart/form-data.</br>
Reading data is performed using a GET request on the LUN endpoint. The request header must include `Accept: multipart/form-data`. When this header entry is provided, query parameters `data.offset` and `data.size` are required and used to specify the portion of the LUN's data to read; no other query parameters are allowed. Reads are limited to one megabyte (1MB) per request. Data is returned as `multipart/form-data` content with exactly one form entry containing the data. The form entry has content type `application/octet-stream`.<br/>
Writing data is performed using a PATCH request on the LUN endpoint. The request header must include `Content-Type: multipart/form-data`. When this header entry is provided, query parameter `data.offset` is required and used to specify the location within the LUN at which to write the data; no other query parameters are allowed. The request body must be `multipart/form-data` content with exactly one form entry containing the data to write. The content type entry of the form data is ignored and always treated as `application/octet-stream`. Writes are limited to one megabyte (1MB) per request.
### Reading data from a LUN
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Lun

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Lun(uuid="c903a978-9bac-4ce9-8237-4a3ba8b13f08")
    resource.get(**{"data.offset": "0", "data.size": "9"})
    print(resource)

```

### Writing data to a LUN
This example writes the contents of a file to a LUN starting at offset 1024.<br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Lun

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Lun(uuid="c903a978-9bac-4ce9-8237-4a3ba8b13f08")
    resource.patch(
        hydrate=True,
        data="@file;type=application/octet-stream",
        **{"data.offset": "1024"}
    )

```

---
## Cloning LUNs
A clone of a LUN is an independent "copy" of the LUN that shares unchanged data blocks with the original. As blocks of the source and clone are modified, unique blocks are written for each. LUN clones can be created quickly and consume very little space initially. They can be created for the purpose of back-up, or to replicate data for multiple consumers.<br/>
Space reservations can be set for the LUN clone independent of the source LUN by setting the `space.guarantee.requested` property in a POST or PATCH request.<br/>
A LUN clone can be set to auto-delete by setting the `auto_delete` property. If the LUN's volume is configured for automatic deletion, LUNs that have auto-delete enabled are deleted when a volume is nearly full to reclaim a target amount of free space in the volume.<br/>
The value of property `space.scsi_thin_provisioning_support_enabled` is not propagated to the destination when a LUN is cloned as a new LUN; it is reset to false. The value of this property is maintained from the destination LUN when a LUN is overwritten as a clone.
### Creating a new LUN clone
You create a new LUN clone as you create any LUN - a POST request to [`/storage/luns`](#/SAN/lun_create). Set `clone.source.uuid` or `clone.source.name` to identify the source LUN from which the clone is created. The LUN clone and its source must reside in the same volume.<br/>
The source LUN can reside in a Snapshot copy, in which case the `clone.source.name` field must be used to identify it. Add `/.snapshot/<snapshot_name>` to the path after the volume name to identify the Snapshot copy. For example `/vol/vol1/.snapshot/snap1/lun1`.<br/>
By default, new LUN clones do not inherit the QoS policy of the source LUN; a QoS policy should be set for the clone by setting the `qos_policy` property.<br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Lun

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Lun()
    resource.svm = {"name": "svm1"}
    resource.name = "/vol/vol1/lun2clone1"
    resource.clone = {"source": {"name": "/vol/vol1/lun2"}}
    resource.qos_policy = {"name": "qos1"}
    resource.post(hydrate=True)
    print(resource)

```

### Over-writing an existing LUN's data as a clone of another
You can overwrite an existing LUN as a clone of another, using a PATCH request to [`/storage/luns/{uuid}`](#/SAN/lun_modify). Set the `clone.source.uuid` or `clone.source.name` property to identify the source LUN from which the clone data is taken. The LUN clone and its source must reside in the same volume.<br/>
When used in a PATCH request, the patched LUN's data is overwritten as a clone of the source. The following properties are preserved from the patched LUN unless otherwise specified as part of the PATCH: `class`, `auto_delete`, `lun_maps`, `vvol`, `serial_number`, `status.state`, and `uuid`.<br/>
Persistent reservations for the updated LUN are also preserved.<br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Lun

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Lun(uuid="5a24ae5b-28af-47fb-b129-5adf6cfba0a6")
    resource.clone = {"source": {"name": "/vol/vol1/lun2"}}
    resource.patch()

```

---
## Converting an NVMe namespace into a LUN
An existing NVMe namespace can be converted in-place to a LUN with no modification to the data blocks. In other words, there is no additional copy created for the data blocks. There are certain requirements for converting an NVMe namespace to a LUN. For instance, the namespace should not be mapped to an NVMe subsystem. Additionally, the namespace should not have a block size other than 512 bytes.<br/>
The conversion process updates the metadata to the NVMe namespace, making it a LUN. The conversion is both time and space efficient. After conversion, the new LUN behaves as a regular LUN and may be mapped to an initiator group.
### Convert an NVMe namespace into a LUN
You convert an NVMe namespace into a LUN by calling a POST to [`/storage/luns`](#/SAN/lun_create). Set `convert.namespace.uuid` or `convert.namespace.name` to identify the source NVMe namespace which is to be converted in-place into a LUN.<br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Lun

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Lun()
    resource.svm = {"name": "svm1"}
    resource.convert = {"namespace": {"name": "/vol/vol1/namespace1"}}
    resource.post(hydrate=True)
    print(resource)

```

---
## Moving LUNs between volumes
You move a LUN between volumes by using a PATCH request to [`/storage/luns/{uuid}`](#/SAN/lun_modify). Set the volume portion of the fully qualified LUN path `name` property, `path.volume.uuid`, or `path.volume.name` property to a different volume than the LUN's current volume. Moving a LUN between volumes is an asynchronous activity. A successful request returns a response of 200 synchronously, which indicates that the movement has been successfully queued. The LUN object can then be further polled with a GET request to [`/storage/luns/{uuid}`](#lun_get) to monitor the status of the movement.<br/>
The `movement` sub-object of the LUN object is populated while a LUN movement is in progress and for two minutes following completion of a movement.
### Starting a LUN movement
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Lun

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Lun(uuid="7faf0a9e-0a47-4876-8318-3638d5da16bf")
    resource.name = "/vol/vol1/lun3"
    resource.patch()

```

### Checking on the status of the LUN movement
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Lun

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Lun(uuid="7faf0a9e-0a47-4876-8318-3638d5da16bf")
    resource.get(fields="movement")
    print(resource)

```
<div class="try_it_out">
<input id="example11_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example11_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example11_result" class="try_it_out_content">
```
Lun(
    {
        "_links": {
            "self": {"href": "/api/storage/luns/7faf0a9e-0a47-4876-8318-3638d5da16bf"}
        },
        "uuid": "7faf0a9e-0a47-4876-8318-3638d5da16bf",
        "name": "/vol/vol1/lun3",
        "movement": {
            "paths": {"destination": "/vol/vol1/lun3", "source": "/vol/vol2/lun3"},
            "progress": {
                "state": "preparing",
                "elapsed": 1,
                "volume_snapshot_blocked": False,
                "percent_complete": 0,
            },
        },
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


__all__ = ["Lun", "LunSchema"]
__pdoc__ = {
    "LunSchema.resource": False,
    "LunSchema.opts": False,
    "Lun.lun_show": False,
    "Lun.lun_create": False,
    "Lun.lun_modify": False,
    "Lun.lun_delete": False,
}


class LunSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the Lun object"""

    links = marshmallow_fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE, allow_none=True)
    r""" The links field of the lun."""

    attributes = marshmallow_fields.List(marshmallow_fields.Nested("netapp_ontap.models.lun_attributes.LunAttributesSchema", unknown=EXCLUDE, allow_none=True), data_key="attributes", allow_none=True)
    r""" An array of name/value pairs optionally stored with the LUN. Attributes are available to callers to persist small amounts of application-specific metadata. They are in no way interpreted by ONTAP.<br/>
Attribute names and values must be at least one byte and no more than 4091 bytes in length. The sum of the name and value lengths must be no more than 4092 bytes.<br/>
Valid in POST except when creating a LUN clone. A cloned can already have attributes from its source. You can add, modify, and delete the attributes of a LUN clone in separate requests after creation of the LUN.<br/>
Attributes may be added/modified/removed for an existing LUN using the /api/storage/luns/{lun.uuid}/attributes endpoint. For further information, see [`DOC /storage/luns/{lun.uuid}/attributes`](#docs-SAN-storage_luns_{lun.uuid}_attributes).<br/>
There is an added computational cost to retrieving property values for `attributes`. They are not populated for either a collection GET or an instance GET unless explicitly requested using the `fields` query parameter. See [`Requesting specific fields`](#Requesting_specific_fields) to learn more."""

    auto_delete = marshmallow_fields.Boolean(
        data_key="auto_delete",
        allow_none=True,
    )
    r""" This property marks the LUN for auto deletion when the volume containing the LUN runs out of space. This is most commonly set on LUN clones.<br/>
When set to _true_, the LUN becomes eligible for automatic deletion when the volume runs out of space. Auto deletion only occurs when the volume containing the LUN is also configured for auto deletion and free space in the volume decreases below a particular threshold.<br/>
This property is optional in POST and PATCH. The default value for a new LUN is _false_.<br/>
There is an added computational cost to retrieving this property's value. It is not populated for either a collection GET or an instance GET unless it is explicitly requested using the `fields` query parameter. See [`Requesting specific fields`](#Requesting_specific_fields) to learn more."""

    class_ = marshmallow_fields.Str(
        data_key="class",
        validate=enum_validation(['regular', 'protocol_endpoint', 'vvol']),
        allow_none=True,
    )
    r""" The class of LUN.<br/>
Optional in POST.


Valid choices:

* regular
* protocol_endpoint
* vvol"""

    clone = marshmallow_fields.Nested("netapp_ontap.models.consistency_group_consistency_groups_luns_clone.ConsistencyGroupConsistencyGroupsLunsCloneSchema", data_key="clone", unknown=EXCLUDE, allow_none=True)
    r""" The clone field of the lun."""

    comment = marshmallow_fields.Str(
        data_key="comment",
        validate=len_validation(minimum=0, maximum=254),
        allow_none=True,
    )
    r""" A configurable comment available for use by the administrator. Valid in POST and PATCH."""

    consistency_group = marshmallow_fields.Nested("netapp_ontap.models.lun_consistency_group.LunConsistencyGroupSchema", data_key="consistency_group", unknown=EXCLUDE, allow_none=True)
    r""" The consistency_group field of the lun."""

    convert = marshmallow_fields.Nested("netapp_ontap.models.lun_convert.LunConvertSchema", data_key="convert", unknown=EXCLUDE, allow_none=True)
    r""" The convert field of the lun."""

    copy = marshmallow_fields.Nested("netapp_ontap.models.lun_copy.LunCopySchema", data_key="copy", unknown=EXCLUDE, allow_none=True)
    r""" The copy field of the lun."""

    create_time = ImpreciseDateTime(
        data_key="create_time",
        allow_none=True,
    )
    r""" The time the LUN was created.

Example: 2018-06-04T19:00:00.000+0000"""

    enabled = marshmallow_fields.Boolean(
        data_key="enabled",
        allow_none=True,
    )
    r""" The enabled state of the LUN. LUNs can be disabled to prevent access to the LUN. Certain error conditions also cause the LUN to become disabled. If the LUN is disabled, you can consult the `state` property to determine if the LUN is administratively disabled (_offline_) or has become disabled as a result of an error. A LUN in an error condition can be brought online by setting the `enabled` property to _true_ or brought administratively offline by setting the `enabled` property to _false_. Upon creation, a LUN is enabled by default. Valid in PATCH."""

    location = marshmallow_fields.Nested("netapp_ontap.models.lun_location.LunLocationSchema", data_key="location", unknown=EXCLUDE, allow_none=True)
    r""" The location field of the lun."""

    lun_maps = marshmallow_fields.List(marshmallow_fields.Nested("netapp_ontap.models.lun_lun_maps.LunLunMapsSchema", unknown=EXCLUDE, allow_none=True), data_key="lun_maps", allow_none=True)
    r""" The LUN maps with which the LUN is associated.<br/>
There is an added computational cost to retrieving property values for `lun_maps`. They are not populated for either a collection GET or an instance GET unless explicitly requested using the `fields` query parameter. See [`Requesting specific fields`](#Requesting_specific_fields) to learn more."""

    metric = marshmallow_fields.Nested("netapp_ontap.resources.performance_metric.PerformanceMetricSchema", data_key="metric", unknown=EXCLUDE, allow_none=True)
    r""" The metric field of the lun."""

    movement = marshmallow_fields.Nested("netapp_ontap.models.lun_movement.LunMovementSchema", data_key="movement", unknown=EXCLUDE, allow_none=True)
    r""" The movement field of the lun."""

    name = marshmallow_fields.Str(
        data_key="name",
        allow_none=True,
    )
    r""" The fully qualified path name of the LUN composed of a "/vol" prefix, the volume name, the (optional) qtree name, and base name of the LUN. Valid in POST and PATCH.<br/>
A PATCH that modifies the qtree and/or base name portion of the LUN path is considered a rename operation.<br/>
A PATCH that modifies the volume portion of the LUN path begins an asynchronous LUN movement operation.


Example: /vol/volume1/qtree1/lun1"""

    os_type = marshmallow_fields.Str(
        data_key="os_type",
        validate=enum_validation(['aix', 'hpux', 'hyper_v', 'linux', 'netware', 'openvms', 'solaris', 'solaris_efi', 'vmware', 'windows', 'windows_2008', 'windows_gpt', 'xen']),
        allow_none=True,
    )
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
* xen"""

    qos_policy = marshmallow_fields.Nested("netapp_ontap.models.lun_qos_policy.LunQosPolicySchema", data_key="qos_policy", unknown=EXCLUDE, allow_none=True)
    r""" The qos_policy field of the lun."""

    serial_number = marshmallow_fields.Str(
        data_key="serial_number",
        validate=len_validation(minimum=12, maximum=12),
        allow_none=True,
    )
    r""" The LUN serial number. The serial number is generated by ONTAP when the LUN is created."""

    space = marshmallow_fields.Nested("netapp_ontap.models.lun_space.LunSpaceSchema", data_key="space", unknown=EXCLUDE, allow_none=True)
    r""" The space field of the lun."""

    statistics = marshmallow_fields.Nested("netapp_ontap.models.performance_metric_raw.PerformanceMetricRawSchema", data_key="statistics", unknown=EXCLUDE, allow_none=True)
    r""" The statistics field of the lun."""

    status = marshmallow_fields.Nested("netapp_ontap.models.lun_status.LunStatusSchema", data_key="status", unknown=EXCLUDE, allow_none=True)
    r""" The status field of the lun."""

    svm = marshmallow_fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE, allow_none=True)
    r""" The svm field of the lun."""

    uuid = marshmallow_fields.Str(
        data_key="uuid",
        allow_none=True,
    )
    r""" The unique identifier of the LUN.  The UUID is generated by ONTAP when the LUN is created.


Example: 1cd8a442-86d1-11e0-ae1c-123478563412"""

    vvol = marshmallow_fields.Nested("netapp_ontap.models.lun_vvol.LunVvolSchema", data_key="vvol", unknown=EXCLUDE, allow_none=True)
    r""" The vvol field of the lun."""

    @property
    def resource(self):
        return Lun

    gettable_fields = [
        "links",
        "attributes",
        "auto_delete",
        "class_",
        "comment",
        "consistency_group",
        "copy",
        "create_time",
        "enabled",
        "location",
        "lun_maps",
        "metric",
        "movement",
        "name",
        "os_type",
        "qos_policy",
        "serial_number",
        "space",
        "statistics.iops_raw",
        "statistics.latency_raw",
        "statistics.status",
        "statistics.throughput_raw",
        "statistics.timestamp",
        "status",
        "svm.links",
        "svm.name",
        "svm.uuid",
        "uuid",
        "vvol",
    ]
    """links,attributes,auto_delete,class_,comment,consistency_group,copy,create_time,enabled,location,lun_maps,metric,movement,name,os_type,qos_policy,serial_number,space,statistics.iops_raw,statistics.latency_raw,statistics.status,statistics.throughput_raw,statistics.timestamp,status,svm.links,svm.name,svm.uuid,uuid,vvol,"""

    patchable_fields = [
        "auto_delete",
        "clone",
        "comment",
        "copy",
        "enabled",
        "location",
        "movement",
        "name",
        "qos_policy",
        "space",
        "svm.name",
        "svm.uuid",
    ]
    """auto_delete,clone,comment,copy,enabled,location,movement,name,qos_policy,space,svm.name,svm.uuid,"""

    postable_fields = [
        "attributes",
        "auto_delete",
        "class_",
        "clone",
        "comment",
        "convert",
        "copy",
        "location",
        "movement",
        "name",
        "os_type",
        "qos_policy",
        "space",
        "svm.name",
        "svm.uuid",
    ]
    """attributes,auto_delete,class_,clone,comment,convert,copy,location,movement,name,os_type,qos_policy,space,svm.name,svm.uuid,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in Lun.get_collection(fields=field)]
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
            raise NetAppRestError("Lun modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class Lun(Resource):
    r""" A LUN is the logical representation of storage in a storage area network (SAN).<br/>
In ONTAP, a LUN is located within a volume. Optionally, it can be located within a qtree in a volume.<br/>
A LUN can be created to a specified size using thin or thick provisioning. A LUN can then be renamed, resized, cloned, and moved to a different volume. LUNs support the assignment of a quality of service (QoS) policy for performance management or a QoS policy can be assigned to the volume containing the LUN. See the LUN object model to learn more about each of the properties supported by the LUN REST API.<br/>
A LUN must be mapped to an initiator group to grant access to the initiator group's initiators (client hosts). Initiators can then access the LUN and perform I/O over a Fibre Channel (FC) fabric using the Fibre Channel Protocol or a TCP/IP network using iSCSI. """

    _schema = LunSchema
    _path = "/api/storage/luns"
    _keys = ["uuid"]
    _patch_form_data_parameters = { 'data':'string', }

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves LUNs.
### Expensive properties
There is an added computational cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`Requesting specific fields`](#Requesting_specific_fields) to learn more.
* `attributes.*`
* `auto_delete`
* `copy.*`
* `lun_maps.*`
* `movement.*`
* `statistics.*`
* `vvol.bindings.*`
* `metric.*`
### Related ONTAP commands
* `lun bind show`
* `lun copy show`
* `lun mapping show`
* `lun move show`
* `lun show`
* `volume file clone show-autodelete`
### Learn more
* [`DOC /storage/luns`](#docs-SAN-storage_luns)
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="lun show")
        def lun_show(
            fields: List[Choices.define(["auto_delete", "class_", "comment", "create_time", "enabled", "name", "os_type", "serial_number", "uuid", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of Lun resources

            Args:
                auto_delete: This property marks the LUN for auto deletion when the volume containing the LUN runs out of space. This is most commonly set on LUN clones.<br/> When set to _true_, the LUN becomes eligible for automatic deletion when the volume runs out of space. Auto deletion only occurs when the volume containing the LUN is also configured for auto deletion and free space in the volume decreases below a particular threshold.<br/> This property is optional in POST and PATCH. The default value for a new LUN is _false_.<br/> There is an added computational cost to retrieving this property's value. It is not populated for either a collection GET or an instance GET unless it is explicitly requested using the `fields` query parameter. See [`Requesting specific fields`](#Requesting_specific_fields) to learn more. 
                class_: The class of LUN.<br/> Optional in POST. 
                comment: A configurable comment available for use by the administrator. Valid in POST and PATCH. 
                create_time: The time the LUN was created.
                enabled: The enabled state of the LUN. LUNs can be disabled to prevent access to the LUN. Certain error conditions also cause the LUN to become disabled. If the LUN is disabled, you can consult the `state` property to determine if the LUN is administratively disabled (_offline_) or has become disabled as a result of an error. A LUN in an error condition can be brought online by setting the `enabled` property to _true_ or brought administratively offline by setting the `enabled` property to _false_. Upon creation, a LUN is enabled by default. Valid in PATCH. 
                name: The fully qualified path name of the LUN composed of a \"/vol\" prefix, the volume name, the (optional) qtree name, and base name of the LUN. Valid in POST and PATCH.<br/> A PATCH that modifies the qtree and/or base name portion of the LUN path is considered a rename operation.<br/> A PATCH that modifies the volume portion of the LUN path begins an asynchronous LUN movement operation. 
                os_type: The operating system type of the LUN.<br/> Required in POST when creating a LUN that is not a clone of another. Disallowed in POST when creating a LUN clone. 
                serial_number: The LUN serial number. The serial number is generated by ONTAP when the LUN is created. 
                uuid: The unique identifier of the LUN.  The UUID is generated by ONTAP when the LUN is created. 
            """

            kwargs = {}
            if auto_delete is not None:
                kwargs["auto_delete"] = auto_delete
            if class_ is not None:
                kwargs["class_"] = class_
            if comment is not None:
                kwargs["comment"] = comment
            if create_time is not None:
                kwargs["create_time"] = create_time
            if enabled is not None:
                kwargs["enabled"] = enabled
            if name is not None:
                kwargs["name"] = name
            if os_type is not None:
                kwargs["os_type"] = os_type
            if serial_number is not None:
                kwargs["serial_number"] = serial_number
            if uuid is not None:
                kwargs["uuid"] = uuid
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return Lun.get_collection(
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all Lun resources that match the provided query"""
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
        """Returns a list of RawResources that represent Lun resources that match the provided query"""
        return super()._get_collection(
            *args, connection=connection, max_records=max_records, raw=True, **kwargs
        )

    fast_get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    @classmethod
    def patch_collection(
        cls,
        body: dict,
        *args,
        records: Iterable["Lun"] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates an existing LUN in one of several ways:
- Updates the properties of a LUN.
- Writes data to a LUN. LUN data write requests are distinguished by the header entry `Content-Type: multipart/form-data`. When this header entry is provided, query parameter `data.offset` is required and used to specify the location within the LUN at which to write the data; no other query parameters are allowed. The request body must be `multipart/form-data` content with exactly one form entry containing the data to write. The content type entry of the form data is ignored and always treated as `application/octet-stream`. Writes are limited to one megabyte (1MB) per request.
- Overwrites the contents of a LUN as a clone of another.
- Begins the movement of a LUN between volumes. PATCH can also pause and resume the movement of a LUN between volumes that is already in active.
### Related ONTAP commands
* `lun copy modify`
* `lun copy pause`
* `lun copy resume`
* `lun modify`
* `lun move-in-volume`
* `lun move modify`
* `lun move pause`
* `lun move resume`
* `lun move start`
* `lun resize`
* `volume file clone autodelete`
### Learn more
* [`DOC /storage/luns`](#docs-SAN-storage_luns)
"""
        return super()._patch_collection(
            body, *args, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    patch_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch_collection.__doc__)

    @classmethod
    def post_collection(
        cls,
        records: Iterable["Lun"],
        *args,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> Union[List["Lun"], NetAppResponse]:
        r"""Creates a LUN.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create the LUN.
* `name`, `location.volume.name` or `location.volume.uuid` - Existing volume in which to create the LUN.
* `name` or `location.logical_unit` - Base name of the LUN.
* `os_type` - Operating system from which the LUN will be accessed. Required when creating a non-clone LUN and disallowed when creating a clone of an existing LUN. A clone's `os_type` is taken from the source LUN.
* `space.size` - Size of the LUN. Required when creating a non-clone LUN and disallowed when creating a clone of an existing LUN. A clone's size is taken from the source LUN.
### Recommended optional properties
* `qos_policy.name` or `qos_policy.uuid` - Existing traditional or adaptive QoS policy to be applied to the LUN. All LUNs should be managed by a QoS policy at the volume or LUN level.
### Default property values
If not specified in POST, the follow default property values are assigned.
* `auto_delete` - _false_
### Related ONTAP commands
* `lun create`
* `lun convert-from-namespace`
* `lun copy start`
* `volume file clone autodelete`
* `volume file clone create`
### Learn more
* [`DOC /storage/luns`](#docs-SAN-storage_luns)
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
        records: Iterable["Lun"] = None,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes a LUN.
### Related ONTAP commands
* `lun copy cancel`
* `lun delete`
### Learn more
* [`DOC /storage/luns`](#docs-SAN-storage_luns)
"""
        return super()._delete_collection(
            *args, body=body, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)

    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves LUNs.
### Expensive properties
There is an added computational cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`Requesting specific fields`](#Requesting_specific_fields) to learn more.
* `attributes.*`
* `auto_delete`
* `copy.*`
* `lun_maps.*`
* `movement.*`
* `statistics.*`
* `vvol.bindings.*`
* `metric.*`
### Related ONTAP commands
* `lun bind show`
* `lun copy show`
* `lun mapping show`
* `lun move show`
* `lun show`
* `volume file clone show-autodelete`
### Learn more
* [`DOC /storage/luns`](#docs-SAN-storage_luns)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)

    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a LUN's properties or a LUN's data.<br/>
LUN data read requests are distinguished by the header entry `Accept: multipart/form-data`. When this header entry is provided, query parameters `data.offset` and `data.size` are required and used to specify the portion of the LUN's data to read; no other query parameters are allowed. Reads are limited to one megabyte (1MB) per request. Data is returned as `multipart/form-data` content with exactly one form entry containing the data. The form entry has content type `application/octet-stream`.
### Expensive properties
There is an added computational cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter. See [`Requesting specific fields`](#Requesting_specific_fields) to learn more.
* `attributes.*`
* `auto_delete`
* `copy.*`
* `lun_maps.*`
* `movement.*`
* `statistics.*`
* `vvol.bindings.*`
* `metric.*`
### Related ONTAP commands
* `lun bind show`
* `lun copy show`
* `lun mapping show`
* `lun move show`
* `lun show`
* `volume file clone show-autodelete`
### Learn more
* [`DOC /storage/luns`](#docs-SAN-storage_luns)
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
        r"""Creates a LUN.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create the LUN.
* `name`, `location.volume.name` or `location.volume.uuid` - Existing volume in which to create the LUN.
* `name` or `location.logical_unit` - Base name of the LUN.
* `os_type` - Operating system from which the LUN will be accessed. Required when creating a non-clone LUN and disallowed when creating a clone of an existing LUN. A clone's `os_type` is taken from the source LUN.
* `space.size` - Size of the LUN. Required when creating a non-clone LUN and disallowed when creating a clone of an existing LUN. A clone's size is taken from the source LUN.
### Recommended optional properties
* `qos_policy.name` or `qos_policy.uuid` - Existing traditional or adaptive QoS policy to be applied to the LUN. All LUNs should be managed by a QoS policy at the volume or LUN level.
### Default property values
If not specified in POST, the follow default property values are assigned.
* `auto_delete` - _false_
### Related ONTAP commands
* `lun create`
* `lun convert-from-namespace`
* `lun copy start`
* `volume file clone autodelete`
* `volume file clone create`
### Learn more
* [`DOC /storage/luns`](#docs-SAN-storage_luns)
"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="lun create")
        async def lun_create(
        ) -> ResourceTable:
            """Create an instance of a Lun resource

            Args:
                links: 
                attributes: An array of name/value pairs optionally stored with the LUN. Attributes are available to callers to persist small amounts of application-specific metadata. They are in no way interpreted by ONTAP.<br/> Attribute names and values must be at least one byte and no more than 4091 bytes in length. The sum of the name and value lengths must be no more than 4092 bytes.<br/> Valid in POST except when creating a LUN clone. A cloned can already have attributes from its source. You can add, modify, and delete the attributes of a LUN clone in separate requests after creation of the LUN.<br/> Attributes may be added/modified/removed for an existing LUN using the /api/storage/luns/{lun.uuid}/attributes endpoint. For further information, see [`DOC /storage/luns/{lun.uuid}/attributes`](#docs-SAN-storage_luns_{lun.uuid}_attributes).<br/> There is an added computational cost to retrieving property values for `attributes`. They are not populated for either a collection GET or an instance GET unless explicitly requested using the `fields` query parameter. See [`Requesting specific fields`](#Requesting_specific_fields) to learn more. 
                auto_delete: This property marks the LUN for auto deletion when the volume containing the LUN runs out of space. This is most commonly set on LUN clones.<br/> When set to _true_, the LUN becomes eligible for automatic deletion when the volume runs out of space. Auto deletion only occurs when the volume containing the LUN is also configured for auto deletion and free space in the volume decreases below a particular threshold.<br/> This property is optional in POST and PATCH. The default value for a new LUN is _false_.<br/> There is an added computational cost to retrieving this property's value. It is not populated for either a collection GET or an instance GET unless it is explicitly requested using the `fields` query parameter. See [`Requesting specific fields`](#Requesting_specific_fields) to learn more. 
                class_: The class of LUN.<br/> Optional in POST. 
                clone: 
                comment: A configurable comment available for use by the administrator. Valid in POST and PATCH. 
                consistency_group: 
                convert: 
                copy: 
                create_time: The time the LUN was created.
                enabled: The enabled state of the LUN. LUNs can be disabled to prevent access to the LUN. Certain error conditions also cause the LUN to become disabled. If the LUN is disabled, you can consult the `state` property to determine if the LUN is administratively disabled (_offline_) or has become disabled as a result of an error. A LUN in an error condition can be brought online by setting the `enabled` property to _true_ or brought administratively offline by setting the `enabled` property to _false_. Upon creation, a LUN is enabled by default. Valid in PATCH. 
                location: 
                lun_maps: The LUN maps with which the LUN is associated.<br/> There is an added computational cost to retrieving property values for `lun_maps`. They are not populated for either a collection GET or an instance GET unless explicitly requested using the `fields` query parameter. See [`Requesting specific fields`](#Requesting_specific_fields) to learn more. 
                metric: 
                movement: 
                name: The fully qualified path name of the LUN composed of a \"/vol\" prefix, the volume name, the (optional) qtree name, and base name of the LUN. Valid in POST and PATCH.<br/> A PATCH that modifies the qtree and/or base name portion of the LUN path is considered a rename operation.<br/> A PATCH that modifies the volume portion of the LUN path begins an asynchronous LUN movement operation. 
                os_type: The operating system type of the LUN.<br/> Required in POST when creating a LUN that is not a clone of another. Disallowed in POST when creating a LUN clone. 
                qos_policy: 
                serial_number: The LUN serial number. The serial number is generated by ONTAP when the LUN is created. 
                space: 
                statistics: 
                status: 
                svm: 
                uuid: The unique identifier of the LUN.  The UUID is generated by ONTAP when the LUN is created. 
                vvol: 
            """

            kwargs = {}
            if links is not None:
                kwargs["links"] = links
            if attributes is not None:
                kwargs["attributes"] = attributes
            if auto_delete is not None:
                kwargs["auto_delete"] = auto_delete
            if class_ is not None:
                kwargs["class_"] = class_
            if clone is not None:
                kwargs["clone"] = clone
            if comment is not None:
                kwargs["comment"] = comment
            if consistency_group is not None:
                kwargs["consistency_group"] = consistency_group
            if convert is not None:
                kwargs["convert"] = convert
            if copy is not None:
                kwargs["copy"] = copy
            if create_time is not None:
                kwargs["create_time"] = create_time
            if enabled is not None:
                kwargs["enabled"] = enabled
            if location is not None:
                kwargs["location"] = location
            if lun_maps is not None:
                kwargs["lun_maps"] = lun_maps
            if metric is not None:
                kwargs["metric"] = metric
            if movement is not None:
                kwargs["movement"] = movement
            if name is not None:
                kwargs["name"] = name
            if os_type is not None:
                kwargs["os_type"] = os_type
            if qos_policy is not None:
                kwargs["qos_policy"] = qos_policy
            if serial_number is not None:
                kwargs["serial_number"] = serial_number
            if space is not None:
                kwargs["space"] = space
            if statistics is not None:
                kwargs["statistics"] = statistics
            if status is not None:
                kwargs["status"] = status
            if svm is not None:
                kwargs["svm"] = svm
            if uuid is not None:
                kwargs["uuid"] = uuid
            if vvol is not None:
                kwargs["vvol"] = vvol

            resource = Lun(
                **kwargs
            )
            try:
                response = resource.post(hydrate=True, poll=False)
                await _wait_for_job(response)
                resource.get()
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to create Lun: %s" % err)
            return [resource]

    def patch(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates an existing LUN in one of several ways:
- Updates the properties of a LUN.
- Writes data to a LUN. LUN data write requests are distinguished by the header entry `Content-Type: multipart/form-data`. When this header entry is provided, query parameter `data.offset` is required and used to specify the location within the LUN at which to write the data; no other query parameters are allowed. The request body must be `multipart/form-data` content with exactly one form entry containing the data to write. The content type entry of the form data is ignored and always treated as `application/octet-stream`. Writes are limited to one megabyte (1MB) per request.
- Overwrites the contents of a LUN as a clone of another.
- Begins the movement of a LUN between volumes. PATCH can also pause and resume the movement of a LUN between volumes that is already in active.
### Related ONTAP commands
* `lun copy modify`
* `lun copy pause`
* `lun copy resume`
* `lun modify`
* `lun move-in-volume`
* `lun move modify`
* `lun move pause`
* `lun move resume`
* `lun move start`
* `lun resize`
* `volume file clone autodelete`
### Learn more
* [`DOC /storage/luns`](#docs-SAN-storage_luns)
"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="lun modify")
        async def lun_modify(
        ) -> ResourceTable:
            """Modify an instance of a Lun resource

            Args:
                auto_delete: This property marks the LUN for auto deletion when the volume containing the LUN runs out of space. This is most commonly set on LUN clones.<br/> When set to _true_, the LUN becomes eligible for automatic deletion when the volume runs out of space. Auto deletion only occurs when the volume containing the LUN is also configured for auto deletion and free space in the volume decreases below a particular threshold.<br/> This property is optional in POST and PATCH. The default value for a new LUN is _false_.<br/> There is an added computational cost to retrieving this property's value. It is not populated for either a collection GET or an instance GET unless it is explicitly requested using the `fields` query parameter. See [`Requesting specific fields`](#Requesting_specific_fields) to learn more. 
                query_auto_delete: This property marks the LUN for auto deletion when the volume containing the LUN runs out of space. This is most commonly set on LUN clones.<br/> When set to _true_, the LUN becomes eligible for automatic deletion when the volume runs out of space. Auto deletion only occurs when the volume containing the LUN is also configured for auto deletion and free space in the volume decreases below a particular threshold.<br/> This property is optional in POST and PATCH. The default value for a new LUN is _false_.<br/> There is an added computational cost to retrieving this property's value. It is not populated for either a collection GET or an instance GET unless it is explicitly requested using the `fields` query parameter. See [`Requesting specific fields`](#Requesting_specific_fields) to learn more. 
                class_: The class of LUN.<br/> Optional in POST. 
                query_class_: The class of LUN.<br/> Optional in POST. 
                comment: A configurable comment available for use by the administrator. Valid in POST and PATCH. 
                query_comment: A configurable comment available for use by the administrator. Valid in POST and PATCH. 
                create_time: The time the LUN was created.
                query_create_time: The time the LUN was created.
                enabled: The enabled state of the LUN. LUNs can be disabled to prevent access to the LUN. Certain error conditions also cause the LUN to become disabled. If the LUN is disabled, you can consult the `state` property to determine if the LUN is administratively disabled (_offline_) or has become disabled as a result of an error. A LUN in an error condition can be brought online by setting the `enabled` property to _true_ or brought administratively offline by setting the `enabled` property to _false_. Upon creation, a LUN is enabled by default. Valid in PATCH. 
                query_enabled: The enabled state of the LUN. LUNs can be disabled to prevent access to the LUN. Certain error conditions also cause the LUN to become disabled. If the LUN is disabled, you can consult the `state` property to determine if the LUN is administratively disabled (_offline_) or has become disabled as a result of an error. A LUN in an error condition can be brought online by setting the `enabled` property to _true_ or brought administratively offline by setting the `enabled` property to _false_. Upon creation, a LUN is enabled by default. Valid in PATCH. 
                name: The fully qualified path name of the LUN composed of a \"/vol\" prefix, the volume name, the (optional) qtree name, and base name of the LUN. Valid in POST and PATCH.<br/> A PATCH that modifies the qtree and/or base name portion of the LUN path is considered a rename operation.<br/> A PATCH that modifies the volume portion of the LUN path begins an asynchronous LUN movement operation. 
                query_name: The fully qualified path name of the LUN composed of a \"/vol\" prefix, the volume name, the (optional) qtree name, and base name of the LUN. Valid in POST and PATCH.<br/> A PATCH that modifies the qtree and/or base name portion of the LUN path is considered a rename operation.<br/> A PATCH that modifies the volume portion of the LUN path begins an asynchronous LUN movement operation. 
                os_type: The operating system type of the LUN.<br/> Required in POST when creating a LUN that is not a clone of another. Disallowed in POST when creating a LUN clone. 
                query_os_type: The operating system type of the LUN.<br/> Required in POST when creating a LUN that is not a clone of another. Disallowed in POST when creating a LUN clone. 
                serial_number: The LUN serial number. The serial number is generated by ONTAP when the LUN is created. 
                query_serial_number: The LUN serial number. The serial number is generated by ONTAP when the LUN is created. 
                uuid: The unique identifier of the LUN.  The UUID is generated by ONTAP when the LUN is created. 
                query_uuid: The unique identifier of the LUN.  The UUID is generated by ONTAP when the LUN is created. 
            """

            kwargs = {}
            changes = {}
            if query_auto_delete is not None:
                kwargs["auto_delete"] = query_auto_delete
            if query_class_ is not None:
                kwargs["class_"] = query_class_
            if query_comment is not None:
                kwargs["comment"] = query_comment
            if query_create_time is not None:
                kwargs["create_time"] = query_create_time
            if query_enabled is not None:
                kwargs["enabled"] = query_enabled
            if query_name is not None:
                kwargs["name"] = query_name
            if query_os_type is not None:
                kwargs["os_type"] = query_os_type
            if query_serial_number is not None:
                kwargs["serial_number"] = query_serial_number
            if query_uuid is not None:
                kwargs["uuid"] = query_uuid

            if auto_delete is not None:
                changes["auto_delete"] = auto_delete
            if class_ is not None:
                changes["class_"] = class_
            if comment is not None:
                changes["comment"] = comment
            if create_time is not None:
                changes["create_time"] = create_time
            if enabled is not None:
                changes["enabled"] = enabled
            if name is not None:
                changes["name"] = name
            if os_type is not None:
                changes["os_type"] = os_type
            if serial_number is not None:
                changes["serial_number"] = serial_number
            if uuid is not None:
                changes["uuid"] = uuid

            if hasattr(Lun, "find"):
                resource = Lun.find(
                    **kwargs
                )
            else:
                resource = Lun()
            try:
                for key, value in changes.items():
                    setattr(resource, key, value)
                response = resource.patch(poll=False)
                await _wait_for_job(response)
                resource.get(fields=",".join(changes.keys()))
                return [resource]
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to modify Lun: %s" % err)

    def delete(
        self,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes a LUN.
### Related ONTAP commands
* `lun copy cancel`
* `lun delete`
### Learn more
* [`DOC /storage/luns`](#docs-SAN-storage_luns)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="lun delete")
        async def lun_delete(
        ) -> None:
            """Delete an instance of a Lun resource

            Args:
                auto_delete: This property marks the LUN for auto deletion when the volume containing the LUN runs out of space. This is most commonly set on LUN clones.<br/> When set to _true_, the LUN becomes eligible for automatic deletion when the volume runs out of space. Auto deletion only occurs when the volume containing the LUN is also configured for auto deletion and free space in the volume decreases below a particular threshold.<br/> This property is optional in POST and PATCH. The default value for a new LUN is _false_.<br/> There is an added computational cost to retrieving this property's value. It is not populated for either a collection GET or an instance GET unless it is explicitly requested using the `fields` query parameter. See [`Requesting specific fields`](#Requesting_specific_fields) to learn more. 
                class_: The class of LUN.<br/> Optional in POST. 
                comment: A configurable comment available for use by the administrator. Valid in POST and PATCH. 
                create_time: The time the LUN was created.
                enabled: The enabled state of the LUN. LUNs can be disabled to prevent access to the LUN. Certain error conditions also cause the LUN to become disabled. If the LUN is disabled, you can consult the `state` property to determine if the LUN is administratively disabled (_offline_) or has become disabled as a result of an error. A LUN in an error condition can be brought online by setting the `enabled` property to _true_ or brought administratively offline by setting the `enabled` property to _false_. Upon creation, a LUN is enabled by default. Valid in PATCH. 
                name: The fully qualified path name of the LUN composed of a \"/vol\" prefix, the volume name, the (optional) qtree name, and base name of the LUN. Valid in POST and PATCH.<br/> A PATCH that modifies the qtree and/or base name portion of the LUN path is considered a rename operation.<br/> A PATCH that modifies the volume portion of the LUN path begins an asynchronous LUN movement operation. 
                os_type: The operating system type of the LUN.<br/> Required in POST when creating a LUN that is not a clone of another. Disallowed in POST when creating a LUN clone. 
                serial_number: The LUN serial number. The serial number is generated by ONTAP when the LUN is created. 
                uuid: The unique identifier of the LUN.  The UUID is generated by ONTAP when the LUN is created. 
            """

            kwargs = {}
            if auto_delete is not None:
                kwargs["auto_delete"] = auto_delete
            if class_ is not None:
                kwargs["class_"] = class_
            if comment is not None:
                kwargs["comment"] = comment
            if create_time is not None:
                kwargs["create_time"] = create_time
            if enabled is not None:
                kwargs["enabled"] = enabled
            if name is not None:
                kwargs["name"] = name
            if os_type is not None:
                kwargs["os_type"] = os_type
            if serial_number is not None:
                kwargs["serial_number"] = serial_number
            if uuid is not None:
                kwargs["uuid"] = uuid

            if hasattr(Lun, "find"):
                resource = Lun.find(
                    **kwargs
                )
            else:
                resource = Lun()
            try:
                response = resource.delete(poll=False)
                await _wait_for_job(response)
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to delete Lun: %s" % err)


