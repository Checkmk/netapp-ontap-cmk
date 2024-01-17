r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

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


__all__ = ["PerformanceS3Metric", "PerformanceS3MetricSchema"]
__pdoc__ = {
    "PerformanceS3MetricSchema.resource": False,
    "PerformanceS3MetricSchema.opts": False,
    "PerformanceS3Metric.performance_s3_metric_show": False,
    "PerformanceS3Metric.performance_s3_metric_create": False,
    "PerformanceS3Metric.performance_s3_metric_modify": False,
    "PerformanceS3Metric.performance_s3_metric_delete": False,
}


class PerformanceS3MetricSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the PerformanceS3Metric object"""

    links = marshmallow_fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE, allow_none=True)
    r""" The links field of the performance_s3_metric."""

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
    r""" The iops field of the performance_s3_metric."""

    latency = marshmallow_fields.Nested("netapp_ontap.models.performance_metric_io_type.PerformanceMetricIoTypeSchema", data_key="latency", unknown=EXCLUDE, allow_none=True)
    r""" The latency field of the performance_s3_metric."""

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
    r""" The throughput field of the performance_s3_metric."""

    timestamp = ImpreciseDateTime(
        data_key="timestamp",
        allow_none=True,
    )
    r""" The timestamp of the performance data.

Example: 2017-01-25T11:20:13.000+0000"""

    @property
    def resource(self):
        return PerformanceS3Metric

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
        return [getattr(r, field) for r in PerformanceS3Metric.get_collection(fields=field)]
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
            raise NetAppRestError("PerformanceS3Metric modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class PerformanceS3Metric(Resource):
    r""" Performance numbers, such as IOPS latency and throughput. """

    _schema = PerformanceS3MetricSchema
    _path = "/api/protocols/s3/services/{svm[uuid]}/metrics"
    _keys = ["svm.uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves historical performance metrics for the S3 protocol of an SVM."""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="performance s3 metric show")
        def performance_s3_metric_show(
            svm_uuid,
            duration: Choices.define(_get_field_list("duration"), cache_choices=True, inexact=True)=None,
            status: Choices.define(_get_field_list("status"), cache_choices=True, inexact=True)=None,
            timestamp: Choices.define(_get_field_list("timestamp"), cache_choices=True, inexact=True)=None,
            fields: List[Choices.define(["duration", "status", "timestamp", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of PerformanceS3Metric resources

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

            return PerformanceS3Metric.get_collection(
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
        """Returns a count of all PerformanceS3Metric resources that match the provided query"""
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
        """Returns a list of RawResources that represent PerformanceS3Metric resources that match the provided query"""
        return super()._get_collection(
            *args, connection=connection, max_records=max_records, raw=True, **kwargs
        )

    fast_get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)




    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves historical performance metrics for the S3 protocol of an SVM."""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)





