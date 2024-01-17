r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

"""

from marshmallow import EXCLUDE, fields as marshmallow_fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["PerformanceSvmNfsMetric", "PerformanceSvmNfsMetricSchema"]
__pdoc__ = {
    "PerformanceSvmNfsMetricSchema.resource": False,
    "PerformanceSvmNfsMetricSchema.opts": False,
    "PerformanceSvmNfsMetric": False,
}


class PerformanceSvmNfsMetricSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the PerformanceSvmNfsMetric object"""

    v3 = marshmallow_fields.Nested("netapp_ontap.models.performance_metric_svm.PerformanceMetricSvmSchema", unknown=EXCLUDE, data_key="v3", allow_none=True)
    r""" The v3 field of the performance_svm_nfs_metric. """

    v4 = marshmallow_fields.Nested("netapp_ontap.models.performance_metric_svm.PerformanceMetricSvmSchema", unknown=EXCLUDE, data_key="v4", allow_none=True)
    r""" The v4 field of the performance_svm_nfs_metric. """

    v41 = marshmallow_fields.Nested("netapp_ontap.models.performance_metric_svm.PerformanceMetricSvmSchema", unknown=EXCLUDE, data_key="v41", allow_none=True)
    r""" The v41 field of the performance_svm_nfs_metric. """

    @property
    def resource(self):
        return PerformanceSvmNfsMetric

    gettable_fields = [
        "v3.links",
        "v3.duration",
        "v3.iops",
        "v3.latency",
        "v3.status",
        "v3.throughput",
        "v3.timestamp",
        "v4.links",
        "v4.duration",
        "v4.iops",
        "v4.latency",
        "v4.status",
        "v4.throughput",
        "v4.timestamp",
        "v41.links",
        "v41.duration",
        "v41.iops",
        "v41.latency",
        "v41.status",
        "v41.throughput",
        "v41.timestamp",
    ]
    """v3.links,v3.duration,v3.iops,v3.latency,v3.status,v3.throughput,v3.timestamp,v4.links,v4.duration,v4.iops,v4.latency,v4.status,v4.throughput,v4.timestamp,v41.links,v41.duration,v41.iops,v41.latency,v41.status,v41.throughput,v41.timestamp,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
    ]
    """"""


class PerformanceSvmNfsMetric(Resource):

    _schema = PerformanceSvmNfsMetricSchema
