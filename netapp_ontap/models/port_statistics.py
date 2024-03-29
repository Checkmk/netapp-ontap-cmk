r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

"""

from marshmallow import EXCLUDE, fields as marshmallow_fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["PortStatistics", "PortStatisticsSchema"]
__pdoc__ = {
    "PortStatisticsSchema.resource": False,
    "PortStatisticsSchema.opts": False,
    "PortStatistics": False,
}


class PortStatisticsSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the PortStatistics object"""

    device = marshmallow_fields.Nested("netapp_ontap.models.port_statistics_device.PortStatisticsDeviceSchema", unknown=EXCLUDE, data_key="device", allow_none=True)
    r""" The device field of the port_statistics. """

    status = marshmallow_fields.Str(data_key="status", allow_none=True)
    r""" Errors associated with the sample. For example, if the aggregation of data over multiple nodes fails, then any partial errors might return "ok" on success or "error" on an internal uncategorized failure. Whenever a sample collection is missed but done at a later time, it is back filled to the previous 15 second timestamp and tagged with "backfilled_data". "inconsistent_delta_time" is encountered when the time between two collections is not the same for all nodes. Therefore, the aggregated value might be over or under inflated. "Negative_delta" is returned when an expected monotonically increasing value has decreased in value. "inconsistent_old_data" is returned when one or more nodes do not have the latest data.

Valid choices:

* ok
* error
* partial_no_data
* partial_no_uuid
* partial_no_response
* partial_other_error
* negative_delta
* backfilled_data
* inconsistent_delta_time
* inconsistent_old_data """

    throughput_raw = marshmallow_fields.Nested("netapp_ontap.models.performance_metric_io_type_rwt.PerformanceMetricIoTypeRwtSchema", unknown=EXCLUDE, data_key="throughput_raw", allow_none=True)
    r""" The throughput_raw field of the port_statistics. """

    timestamp = ImpreciseDateTime(data_key="timestamp", allow_none=True)
    r""" The timestamp of the throughput_raw performance data.

Example: 2017-01-25T11:20:13.000+0000 """

    @property
    def resource(self):
        return PortStatistics

    gettable_fields = [
        "device",
        "status",
        "throughput_raw.read",
        "throughput_raw.total",
        "throughput_raw.write",
        "timestamp",
    ]
    """device,status,throughput_raw.read,throughput_raw.total,throughput_raw.write,timestamp,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
    ]
    """"""


class PortStatistics(Resource):

    _schema = PortStatisticsSchema
