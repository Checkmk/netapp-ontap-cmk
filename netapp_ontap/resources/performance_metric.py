r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

## Overview
The Storage Aggregate Metrics API provides historical performance metrics for the specified aggregate.
The collection GET operation retrieves read, write, other and total metrics for a given aggregate, in terms of IOPS, latency and throughput. The read and write categories display the I/O operations that service user reads and writes across all the hosted volumes on a given aggregate. The other category encompasses background I/O operations that implement data protection services currently running on the aggregate. IOPs are the number of I/O operations reported per second, throughput is the amount of I/O operations measured in bytes per second and latency is the average response time for an IOP, reported in microseconds.
Without a specified time interval, the output is limited to statistics collected at 15 second intervals over the last hour.
## Examples
### Retrieving metrics for an aggregate
In this example, the API returns a set of records that exist for the aggregate with the given UUID for the last hour.
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import PerformanceMetric

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    print(
        list(
            PerformanceMetric.get_collection(
                "538bf337-1b2c-11e8-bad0-005056b48388", max_records=4
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
    PerformanceMetric({"timestamp": "2019-01-14T23:33:45+00:00"}),
    PerformanceMetric({"timestamp": "2019-01-14T23:33:30+00:00"}),
    PerformanceMetric({"timestamp": "2019-01-14T23:33:15+00:00"}),
    PerformanceMetric({"timestamp": "2019-01-14T23:33:00+00:00"}),
]

```
</div>
</div>

### Retrieving metrics for an aggregate with a set timestamp
In this example, the API returns metric values for latency, IOPS, and throughput properties such as read, write and total. The status and duration
for which the metrics are requested are also returned.
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import PerformanceMetric

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    print(
        list(
            PerformanceMetric.get_collection(
                "538bf337-1b2c-11e8-bad0-005056b48388", timestamp="2019-01-1T23:33:00Z"
            )
        )
    )

```
<div class="try_it_out">
<input id="example1_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example1_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example1_result" class="try_it_out_content">
```
[
    PerformanceMetric(
        {
            "timestamp": "2019-01-01T23:33:00+00:00",
            "throughput": {"other": 0, "total": 212718, "read": 6826, "write": 205892},
            "status": "ok",
            "iops": {"other": 0, "total": 6, "read": 1, "write": 5},
            "duration": "PT15S",
            "latency": {"other": 0, "total": 199, "read": 148, "write": 216},
        }
    )
]

```
</div>
</div>

### Retrieving metrics for an aggregate for a set time interval
In this example, the API returns the requested metrics for the given time interval of 1 week. The interval value can be
1 hour, 1 day, 1 week, 1 month or 1 year. If the interval value is not set, a default value of 1 hour is used.
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import PerformanceMetric

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    print(
        list(
            PerformanceMetric.get_collection(
                "538bf337-1b2c-11e8-bad0-005056b48388",
                return_timeout=15,
                fields="*",
                interval="1w",
                max_records=4,
            )
        )
    )

```
<div class="try_it_out">
<input id="example2_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example2_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example2_result" class="try_it_out_content">
```
[
    PerformanceMetric(
        {
            "timestamp": "2019-01-01T23:30:00+00:00",
            "throughput": {
                "other": 0,
                "total": 5824584,
                "read": 268328,
                "write": 5556255,
            },
            "status": "ok",
            "iops": {"other": 0, "total": 45, "read": 18, "write": 26},
            "duration": "PT30M",
            "latency": {"other": 0, "total": 318, "read": 156, "write": 430},
        }
    ),
    PerformanceMetric(
        {
            "timestamp": "2019-01-01T23:00:00+00:00",
            "throughput": {
                "other": 0,
                "total": 6596175,
                "read": 474266,
                "write": 6121908,
            },
            "status": "ok",
            "iops": {"other": 0, "total": 76, "read": 48, "write": 28},
            "duration": "PT30M",
            "latency": {"other": 0, "total": 262, "read": 154, "write": 448},
        }
    ),
    PerformanceMetric(
        {
            "timestamp": "2019-01-01T22:30:00+00:00",
            "throughput": {
                "other": 26244685,
                "total": 29196206,
                "read": 540164,
                "write": 2411356,
            },
            "status": "ok",
            "iops": {"other": 437, "total": 548, "read": 94, "write": 16},
            "duration": "PT30M",
            "latency": {"other": 192, "total": 193, "read": 159, "write": 394},
        }
    ),
    PerformanceMetric(
        {
            "timestamp": "2019-01-01T22:00:00+00:00",
            "throughput": {
                "other": 0,
                "total": 2768249,
                "read": 2842,
                "write": 2765407,
            },
            "status": "ok",
            "iops": {"other": 0, "total": 13, "read": 0, "write": 13},
            "duration": "PT30M",
            "latency": {"other": 0, "total": 523, "read": 189, "write": 540},
        }
    ),
]

```
</div>
</div>

### Related ONTAP commands

* `statistics aggregate show`"""

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


__all__ = ["PerformanceMetric", "PerformanceMetricSchema"]
__pdoc__ = {
    "PerformanceMetricSchema.resource": False,
    "PerformanceMetricSchema.opts": False,
    "PerformanceMetric.performance_metric_show": False,
    "PerformanceMetric.performance_metric_create": False,
    "PerformanceMetric.performance_metric_modify": False,
    "PerformanceMetric.performance_metric_delete": False,
}


class PerformanceMetricSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the PerformanceMetric object"""

    links = marshmallow_fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE, allow_none=True)
    r""" The links field of the performance_metric."""

    duration = marshmallow_fields.Str(
        data_key="duration",
        validate=enum_validation(['PT15S', 'PT4M', 'PT30M', 'PT2H', 'P1D', 'PT5M']),
        allow_none=True,
    )
    r""" The duration over which this sample is calculated. The time durations are represented in the ISO-8601 standard format. Samples can be calculated over the following durations:


Valid choices:

* PT15S
* PT4M
* PT30M
* PT2H
* P1D
* PT5M"""

    iops = marshmallow_fields.Nested("netapp_ontap.models.performance_metric_io_type.PerformanceMetricIoTypeSchema", data_key="iops", unknown=EXCLUDE, allow_none=True)
    r""" The iops field of the performance_metric."""

    latency = marshmallow_fields.Nested("netapp_ontap.models.performance_metric_io_type.PerformanceMetricIoTypeSchema", data_key="latency", unknown=EXCLUDE, allow_none=True)
    r""" The latency field of the performance_metric."""

    status = marshmallow_fields.Str(
        data_key="status",
        validate=enum_validation(['ok', 'error', 'partial_no_data', 'partial_no_response', 'partial_other_error', 'negative_delta', 'not_found', 'backfilled_data', 'inconsistent_delta_time', 'inconsistent_old_data', 'partial_no_uuid']),
        allow_none=True,
    )
    r""" Errors associated with the sample. For example, if the aggregation of data over multiple nodes fails, then any partial errors might return "ok" on success or "error" on an internal uncategorized failure. Whenever a sample collection is missed but done at a later time, it is back filled to the previous 15 second timestamp and tagged with "backfilled_data". "Inconsistent_ delta_time" is encountered when the time between two collections is not the same for all nodes. Therefore, the aggregated value might be over or under inflated. "Negative_delta" is returned when an expected monotonically increasing value has decreased in value. "Inconsistent_old_data" is returned when one or more nodes do not have the latest data.

Valid choices:

* ok
* error
* partial_no_data
* partial_no_response
* partial_other_error
* negative_delta
* not_found
* backfilled_data
* inconsistent_delta_time
* inconsistent_old_data
* partial_no_uuid"""

    throughput = marshmallow_fields.Nested("netapp_ontap.models.performance_metric_io_type.PerformanceMetricIoTypeSchema", data_key="throughput", unknown=EXCLUDE, allow_none=True)
    r""" The throughput field of the performance_metric."""

    timestamp = ImpreciseDateTime(
        data_key="timestamp",
        allow_none=True,
    )
    r""" The timestamp of the performance data.

Example: 2017-01-25T11:20:13.000+0000"""

    @property
    def resource(self):
        return PerformanceMetric

    gettable_fields = [
        "links",
        "duration",
        "iops.other",
        "iops.read",
        "iops.total",
        "iops.write",
        "latency.other",
        "latency.read",
        "latency.total",
        "latency.write",
        "status",
        "throughput.other",
        "throughput.read",
        "throughput.total",
        "throughput.write",
        "timestamp",
    ]
    """links,duration,iops.other,iops.read,iops.total,iops.write,latency.other,latency.read,latency.total,latency.write,status,throughput.other,throughput.read,throughput.total,throughput.write,timestamp,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
    ]
    """"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in PerformanceMetric.get_collection(fields=field)]
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
            raise NetAppRestError("PerformanceMetric modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class PerformanceMetric(Resource):
    r""" Performance numbers, such as IOPS latency and throughput. """

    _schema = PerformanceMetricSchema
    _path = "/api/storage/aggregates/{aggregate[uuid]}/metrics"
    _keys = ["aggregate.uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves historical performance metrics for an aggregate.
### Learn more
* [`DOC /storage/aggregates/{uuid}/metrics`](#docs-storage-storage_aggregates_{uuid}_metrics)"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="performance metric show")
        def performance_metric_show(
            uuid,
            duration: Choices.define(_get_field_list("duration"), cache_choices=True, inexact=True)=None,
            status: Choices.define(_get_field_list("status"), cache_choices=True, inexact=True)=None,
            timestamp: Choices.define(_get_field_list("timestamp"), cache_choices=True, inexact=True)=None,
            fields: List[Choices.define(["duration", "status", "timestamp", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of PerformanceMetric resources

            Args:
                duration: The duration over which this sample is calculated. The time durations are represented in the ISO-8601 standard format. Samples can be calculated over the following durations: 
                status: Errors associated with the sample. For example, if the aggregation of data over multiple nodes fails, then any partial errors might return \"ok\" on success or \"error\" on an internal uncategorized failure. Whenever a sample collection is missed but done at a later time, it is back filled to the previous 15 second timestamp and tagged with \"backfilled_data\". \"Inconsistent_ delta_time\" is encountered when the time between two collections is not the same for all nodes. Therefore, the aggregated value might be over or under inflated. \"Negative_delta\" is returned when an expected monotonically increasing value has decreased in value. \"Inconsistent_old_data\" is returned when one or more nodes do not have the latest data.
                timestamp: The timestamp of the performance data.
            """

            kwargs = {}
            if duration is not None:
                kwargs["duration"] = duration
            if status is not None:
                kwargs["status"] = status
            if timestamp is not None:
                kwargs["timestamp"] = timestamp
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return PerformanceMetric.get_collection(
                uuid,
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all PerformanceMetric resources that match the provided query"""
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
        """Returns a list of RawResources that represent PerformanceMetric resources that match the provided query"""
        return super()._get_collection(
            *args, connection=connection, max_records=max_records, raw=True, **kwargs
        )

    fast_get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)




    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves historical performance metrics for an aggregate.
### Learn more
* [`DOC /storage/aggregates/{uuid}/metrics`](#docs-storage-storage_aggregates_{uuid}_metrics)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)






