r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

## Overview
You can use this API to retrieve a list of files with the most IO activity for FlexVol and FlexGroup volumes belonging to a specified SVM. To obtain this list, only the volumes which have the activity tracking feature enabled are considered. </br>
This API is used to provide insight into IO activity and supports ordering by IO activity types, namely `iops` and `throughput` metrics. Use the `top_metric` parameter to specify which type of IO activity to filter for. This API supports returning only one IO activity type per request.</br>
## Enabling and disabling activity tracking feature
The following APIs can be used to enable, disable, and retrieve the activity tracking state for a FlexVol or a FlexGroup volume.

* PATCH  /api/storage/volumes/{uuid} -d '{"activity_tracking.state":"on"}'
* PATCH  /api/storage/volumes/{uuid} -d '{"activity_tracking.state":"off"}'
* GET    /api/storage/volumes/{uuid}/?fields=activity_tracking
## Excluded volumes list
Optionally, the API returns an excluded list of activity tracking-enabled volumes, which were not accounted for when obtaining the list of clients with the most IO activity for the SVM. This excluded list contains both the volume information and the reason for exclusion.
## Failure to return list of files with most IO activity
The API can sometimes fail to return the list of files with the most IO activity, due to the following reasons.

* The volumes belonging to the SVM do not have the activity tracking feature enabled.
* The volumes belonging to the SVM do not have read/write traffic.
* The read traffic is served by the NFS/CIFS client filesystem cache.
* On rare occasions, the incoming traffic pattern is not suitable to obtain the list of files with the most IO activity.
## Failure to return the pathnames
The API can sometimes fail to obtain the filesystem pathnames for the list of file entries, due to internal transient errors.
In such cases, instead of the pathname, the API will return "<volume_instance_uuid>.<fileid>" for every file entry.
You can get more information about the file entry by invoking the GET on the below API using the above obtained fileid.
"GET /api/storage/volumes/{<volume_instance_uuid>}/files/{path}?inode_number=<fileid>"
## Retrieve a list of the files with the most IO activity
For a report on the files with the most IO activity returned in descending order, specify the IO activity type you want to filter for by passing the `iops` or `throughput` property into the top_metric parameter. If the IO activity type is not specified, by default the API returns a list of the files with the greatest number of the average read operations per second. The maximum number of files returned by the API for an IO activity type is 25.

* GET   /api/svm/svms/{svm.uuid}/top-metrics/files
## Examples
### Retrieving a list of the files with the greatest average number of write bytes received per second:
---
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import TopMetricsSvmFile

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    print(
        list(
            TopMetricsSvmFile.get_collection(
                "{svm.uuid}", top_metric="throughput.write"
            )
        )
    )

```
<div class="try_it_out">
<input id="example0_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example0_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example0_result" class="try_it_out_content">
```
[
    TopMetricsSvmFile(
        {
            "svm": {"name": "vs1"},
            "volume": {
                "_links": {
                    "self": {
                        "href": "/api/storage/volumes/73b293df-e9d7-46cc-a9ce-2df8e52ef864"
                    }
                },
                "uuid": "73b293df-e9d7-46cc-a9ce-2df8e52ef864",
                "name": "fv1",
            },
            "throughput": {
                "write": 24,
                "error": {"upper_bound": 29, "lower_bound": 24},
            },
            "junction-path": "/fv1",
            "path": "/vol/fv1/d5/f5",
            "_links": {
                "metadata": {
                    "href": "/api/storage/volumes/73b293df-e9d7-46cc-a9ce-2df8e52ef864/files/d5%2Ff5?return_metadata=true"
                }
            },
        }
    ),
    TopMetricsSvmFile(
        {
            "svm": {"name": "vs1"},
            "volume": {
                "_links": {
                    "self": {
                        "href": "/api/storage/volumes/2ea74c3e-d5ca-11eb-8fbb-005056ac0f33"
                    }
                },
                "uuid": "2ea74c3e-d5ca-11eb-8fbb-005056ac0f33",
                "name": "fv2",
            },
            "throughput": {
                "write": 12,
                "error": {"upper_bound": 22, "lower_bound": 12},
            },
            "junction-path": "/fv2",
            "path": "/vol/fv2/d6/f6",
            "_links": {
                "metadata": {
                    "href": "/api/storage/volumes/2ea74c3e-d5ca-11eb-8fbb-005056ac0f33/files/d6%2Ff6?return_metadata=true"
                }
            },
        }
    ),
    TopMetricsSvmFile(
        {
            "svm": {"name": "vs1"},
            "volume": {
                "_links": {
                    "self": {
                        "href": "/api/storage/volumes/1ca74c3e-d5ca-11eb-8fbb-005056ac0f88"
                    }
                },
                "uuid": "1ca74c3e-d5ca-11eb-8fbb-005056ac0f88",
                "name": "fv3",
            },
            "throughput": {"write": 8, "error": {"upper_bound": 10, "lower_bound": 8}},
            "junction-path": "/fv3",
            "path": "/vol/fv3/d3/f3",
            "_links": {
                "metadata": {
                    "href": "/api/storage/volumes/1ca74c3e-d5ca-11eb-8fbb-005056ac0f88/files/d3%2Ff3?return_metadata=true"
                }
            },
        }
    ),
]

```
</div>
</div>

---
### Retrieving a list of the files with the most read traffic, with failure to obtain pathnames
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import TopMetricsSvmFile

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    print(list(TopMetricsSvmFile.get_collection("{svm.uuid}", top_metric="iops.read")))

```
<div class="try_it_out">
<input id="example1_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example1_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example1_result" class="try_it_out_content">
```
[
    TopMetricsSvmFile(
        {
            "svm": {"name": "vs1"},
            "volume": {
                "_links": {
                    "self": {
                        "href": "/api/storage/volumes/73b293df-e9d7-46cc-a9ce-2df8e52ef86"
                    }
                },
                "uuid": "73b293df-e9d7-46cc-a9ce-2df8e52ef86",
                "name": "fv1",
            },
            "junction-path": "/fv1",
            "path": "73b293df-e9d7-46cc-a9ce-2df8e52ef86.1232",
            "iops": {"read": 1495, "error": {"upper_bound": 1505, "lower_bound": 1495}},
        }
    ),
    TopMetricsSvmFile(
        {
            "svm": {"name": "vs1"},
            "volume": {
                "_links": {
                    "self": {
                        "href": "/api/storage/volumes/11b293df-e9d7-46cc-a9ce-2df8e52ef811"
                    }
                },
                "uuid": "11b293df-e9d7-46cc-a9ce-2df8e52ef811",
                "name": "fv2",
            },
            "junction-path": "/fv2",
            "path": "11b293df-e9d7-46cc-a9ce-2df8e52ef811.6574",
            "iops": {"read": 1022, "error": {"upper_bound": 1032, "lower_bound": 1022}},
        }
    ),
    TopMetricsSvmFile(
        {
            "svm": {"name": "vs1"},
            "volume": {
                "_links": {
                    "self": {
                        "href": "/api/storage/volumes/73b293df-e9d7-46cc-a9ce-2df8e52ef864"
                    }
                },
                "uuid": "73b293df-e9d7-46cc-a9ce-2df8e52ef864",
                "name": "fv1",
            },
            "junction-path": "/fv1",
            "path": "73b293df-e9d7-46cc-a9ce-2df8e52ef864.7844",
            "iops": {"read": 345, "error": {"upper_bound": 355, "lower_bound": 345}},
        }
    ),
]

```
</div>
</div>

---
### Example showing the behavior of the API where there is no read/write traffic:
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import TopMetricsSvmFile

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    print(
        list(
            TopMetricsSvmFile.get_collection(
                "{svm.uuid}", top_metric="throughput.write"
            )
        )
    )

```
<div class="try_it_out">
<input id="example2_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example2_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example2_result" class="try_it_out_content">
```
[]

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


__all__ = ["TopMetricsSvmFile", "TopMetricsSvmFileSchema"]
__pdoc__ = {
    "TopMetricsSvmFileSchema.resource": False,
    "TopMetricsSvmFileSchema.opts": False,
    "TopMetricsSvmFile.top_metrics_svm_file_show": False,
    "TopMetricsSvmFile.top_metrics_svm_file_create": False,
    "TopMetricsSvmFile.top_metrics_svm_file_modify": False,
    "TopMetricsSvmFile.top_metrics_svm_file_delete": False,
}


class TopMetricsSvmFileSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the TopMetricsSvmFile object"""

    links = marshmallow_fields.Nested("netapp_ontap.models.file_info_links.FileInfoLinksSchema", data_key="_links", unknown=EXCLUDE, allow_none=True)
    r""" The links field of the top_metrics_svm_file."""

    iops = marshmallow_fields.Nested("netapp_ontap.models.top_metrics_file_iops.TopMetricsFileIopsSchema", data_key="iops", unknown=EXCLUDE, allow_none=True)
    r""" The iops field of the top_metrics_svm_file."""

    junction_path = marshmallow_fields.Str(
        data_key="junction-path",
        allow_none=True,
    )
    r""" Junction path of the file.

Example: /fv"""

    path = marshmallow_fields.Str(
        data_key="path",
        allow_none=True,
    )
    r""" Path of the file.

Example: /vol/fv/dir_abc/dir_123/file_1"""

    svm = marshmallow_fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE, allow_none=True)
    r""" The svm field of the top_metrics_svm_file."""

    throughput = marshmallow_fields.Nested("netapp_ontap.models.top_metrics_file_throughput.TopMetricsFileThroughputSchema", data_key="throughput", unknown=EXCLUDE, allow_none=True)
    r""" The throughput field of the top_metrics_svm_file."""

    volume = marshmallow_fields.Nested("netapp_ontap.resources.volume.VolumeSchema", data_key="volume", unknown=EXCLUDE, allow_none=True)
    r""" The volume field of the top_metrics_svm_file."""

    @property
    def resource(self):
        return TopMetricsSvmFile

    gettable_fields = [
        "links",
        "iops",
        "junction_path",
        "path",
        "svm.links",
        "svm.name",
        "svm.uuid",
        "throughput",
        "volume.links",
        "volume.name",
        "volume.uuid",
    ]
    """links,iops,junction_path,path,svm.links,svm.name,svm.uuid,throughput,volume.links,volume.name,volume.uuid,"""

    patchable_fields = [
        "iops",
        "throughput",
    ]
    """iops,throughput,"""

    postable_fields = [
        "iops",
        "throughput",
    ]
    """iops,throughput,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in TopMetricsSvmFile.get_collection(fields=field)]
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
            raise NetAppRestError("TopMetricsSvmFile modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class TopMetricsSvmFile(Resource):
    r""" Information about a file's IO activity. """

    _schema = TopMetricsSvmFileSchema
    _path = "/api/svm/svms/{svm[uuid]}/top-metrics/files"
    _keys = ["svm.uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves a list of files with the most IO activity.
### Learn more
* [`DOC /svm/svms/{svm.uuid}/top-metrics/files`](#docs-svm-svm_svms_{svm.uuid}_top-metrics_files)"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="top metrics svm file show")
        def top_metrics_svm_file_show(
            svm_uuid,
            junction_path: Choices.define(_get_field_list("junction_path"), cache_choices=True, inexact=True)=None,
            path: Choices.define(_get_field_list("path"), cache_choices=True, inexact=True)=None,
            fields: List[Choices.define(["junction_path", "path", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of TopMetricsSvmFile resources

            Args:
                junction_path: Junction path of the file.
                path: Path of the file.
            """

            kwargs = {}
            if junction_path is not None:
                kwargs["junction_path"] = junction_path
            if path is not None:
                kwargs["path"] = path
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return TopMetricsSvmFile.get_collection(
                svm_uuid,
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all TopMetricsSvmFile resources that match the provided query"""
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
        """Returns a list of RawResources that represent TopMetricsSvmFile resources that match the provided query"""
        return super()._get_collection(
            *args, connection=connection, max_records=max_records, raw=True, **kwargs
        )

    fast_get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)




    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a list of files with the most IO activity.
### Learn more
* [`DOC /svm/svms/{svm.uuid}/top-metrics/files`](#docs-svm-svm_svms_{svm.uuid}_top-metrics_files)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)






