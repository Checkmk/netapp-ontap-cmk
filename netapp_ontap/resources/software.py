r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

## Overview
You can use the ONTAP cluster software API to retrieve and display relevant information about a software profile, software packages collection, software history collection, and firmware packages collection. This API retrieves the information about all software packages present in the cluster, or a specific software package, or firmware upgrade status.
<br/>You can use the POST request to download a software package/firmware from an HTTP or FTP server. The PATCH request provides the option to upgrade the cluster software version. Select the `validate_only` field to validate the package before triggering the update. Set the `version` field to trigger the installation of the package in the cluster. You can pause, resume, or cancel any ongoing software upgrade by selecting `action`. You can use the DELETE request to remove a specific software package present in the cluster.
---
## Examples
### Retrieving software profile information
The following example shows how to retrieve software and firmware profile information. You can check the validation results after selecting the `validate_only` field. Upgrade progress information is available after an upgrade has started.
<br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Software

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Software()
    resource.get(return_timeout=15)
    print(resource)

```
<div class="try_it_out">
<input id="example0_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example0_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example0_result" class="try_it_out_content">
```
Software(
    {
        "status_details": [
            {
                "state": "completed",
                "end_time": "2018-05-21T11:53:04+05:30",
                "issue": {"code": 0, "message": "Image update complete"},
                "node": {"name": "sti70-vsim-ucs165n"},
                "start_time": "2018-05-21T09:53:04+05:30",
                "name": "do-download-job",
            }
        ],
        "state": "in_progress",
        "validation_results": [
            {
                "action": {"message": "Use NFS hard mounts, if possible."},
                "issue": {"message": "Use NFS hard mounts, if possible."},
                "status": "warning",
                "update_check": "NFS mounts",
            }
        ],
        "pending_version": "9.6.0",
        "_links": {"self": {"href": "/api/cluster/software/"}},
        "metrocluster": {
            "progress_details": {
                "message": 'Installing software image on cluster "sti70-vsim-ucs165n_siteA".'
            },
            "progress_summary": {"message": "Update paused by user"},
            "clusters": [
                {
                    "name": "sti70-vsim-ucs165n_siteA",
                    "elapsed_duration": 0,
                    "state": "waiting",
                    "estimated_duration": 3480,
                }
            ],
        },
        "version": "9.5.0",
        "nodes": [
            {
                "firmware": {
                    "dqp": {
                        "revision": "20200117",
                        "version": "3.17",
                        "record_count": {
                            "device": 29,
                            "alias": 200,
                            "system": 3,
                            "drive": 680,
                        },
                        "file_name": "qual_devices_v2",
                    },
                    "shelf": {"update_status": "idle", "in_progress_count": 2},
                    "cluster_fw_progress": [
                        {
                            "update_type": "automatic_update",
                            "job": {
                                "_links": {
                                    "self": {
                                        "href": "/api/cluster/jobs/5a21663c-a9a0-11ea-af9a-005056bb44d7"
                                    }
                                },
                                "uuid": "5a21663c-a9a0-11ea-af9a-005056bb44d7",
                            },
                            "update_state": [
                                {
                                    "message": "Cannot open the local staging zip file.",
                                    "worker_node": {
                                        "uuid": "fcd40f70-f531-11eb-b235-005056bb3497",
                                        "name": "Node 1",
                                    },
                                    "code": 2228325,
                                    "status": "failed",
                                    "attempts": 3,
                                },
                                {
                                    "message": "Success",
                                    "worker_node": {
                                        "uuid": "fcd40f70-f531-11eb-b235-005056bb3498",
                                        "name": "Node 2",
                                    },
                                    "code": 0,
                                    "status": "complete",
                                    "attempts": 3,
                                },
                            ],
                            "zip_file_name": "abc.zip",
                        },
                        {
                            "update_type": "manual_update",
                            "job": {
                                "_links": {
                                    "self": {
                                        "href": "/api/cluster/jobs/5a21663c-a9a0-11ea-af9a-005056bb44d7"
                                    }
                                },
                                "uuid": "5a21663c-a9a0-11ea-af9a-005056bb44d7",
                            },
                            "update_state": [
                                {
                                    "message": "Cannot open the local staging zip file.",
                                    "worker_node": {
                                        "uuid": "fcd40f70-f531-11eb-b235-005056bb3497",
                                        "name": "Node 1",
                                    },
                                    "code": 2228325,
                                    "status": "failed",
                                    "attempts": 3,
                                },
                                {
                                    "message": "Success",
                                    "worker_node": {
                                        "uuid": "fcd40f70-f531-11eb-b235-005056bb3498",
                                        "name": "Node 2",
                                    },
                                    "code": 0,
                                    "status": "complete",
                                    "attempts": 3,
                                },
                            ],
                            "zip_file_name": "xyz.zip",
                        },
                    ],
                    "disk": {
                        "update_status": "idle",
                        "average_duration_per_disk": 120,
                        "total_completion_estimate": 0,
                        "num_waiting_download": 0,
                    },
                    "sp_bmc": {
                        "image": " primary",
                        "end_time": "2018-05-21T09:53:04+05:30",
                        "running_version": "1.2.3.4",
                        "is_current": True,
                        "in_progress": False,
                        "percent_done": 100,
                        "fw_type": "SP",
                        "start_time": "2018-05-21T09:53:04+05:30",
                    },
                },
                "version": "9.5.0",
            }
        ],
        "update_details": [
            {
                "elapsed_duration": 29,
                "state": "in_progress",
                "phase": "Data ONTAP updates",
                "estimated_duration": 4620,
                "node": {"name": "sti70-vsim-ucs165n"},
            }
        ],
    }
)

```
</div>
</div>

---
### Upgrading the software version
The following example shows how to upgrade cluster software. Set the `version` field to trigger the installation of the package. You can select the `validate_only` field to validate the package before the installation starts. Setting `skip_warning` as `true` ignores the validation warning before the installation starts. Setting the `action` field performs a `pause`, `resume`, or `cancel' operation on an ongoing upgrade. An upgrade can only be resumed if it is in the paused state. Setting `stabilize_minutes` allows each node a specified amount of time to stabilize after a reboot; the default is 8 minutes. If `show_validation_details` is set to "true", all validation details will be shown in the output.
<br/>You can start the upgrade process at the cluster level. There are no options available to start the upgrade for a specific node or HA pair.
#### 1. Validating the package and verifying the validation results
The following example shows how to validate a cluster software package. You must validate the package before the software upgrade. Set the `validate_only` field to `true` to start the validation. You can check for validation results in the GET /cluster/software endpoint.
<br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Software

with HostConnection("<mgmt_ip>", username="admin", password="password", verify=False):
    resource = Software()
    resource.version = "9.5.0"
    resource.patch(hydrate=True, validate_only=True)

```

---
The call to validate the software cluster version returns the job UUID, including a HAL link to retrieve details about the job. The job object includes a `state` field and a message to indicate the progress of the job. When the job is complete and the application is fully created, the message indicates success and the `state` field of the job is set to `success`.
<br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Job

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Job(uuid="f587d316-5feb-11e8-b0e0-005056956dfc")
    resource.get()
    print(resource)

```
<div class="try_it_out">
<input id="example2_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example2_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example2_result" class="try_it_out_content">
```
Job(
    {
        "message": "success",
        "state": "success",
        "code": 0,
        "uuid": "f587d316-5feb-11e8-b0e0-005056956dfc",
        "_links": {
            "self": {"href": "/api/cluster/jobs/f587d316-5feb-11e8-b0e0-005056956dfc"}
        },
        "description": "PATCH /api/cluster/software",
    }
)

```
</div>
</div>

---
You can check for validation results in the GET /cluster/software endpoint. The following example shows how to check the validation warnings and errors after setting the `validate_only` field to `true`.
<br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Software

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Software()
    resource.get()
    print(resource)

```
<div class="try_it_out">
<input id="example3_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example3_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example3_result" class="try_it_out_content">
```
Software(
    {
        "elapsed_duration": 56,
        "state": "failed",
        "validation_results": [
            {
                "action": {
                    "message": "Check cluster HA configuration. Check storage failover status."
                },
                "issue": {
                    "message": 'Cluster HA is not configured in the cluster. Storage failover is not enabled on node "node1", "node2".'
                },
                "status": "error",
                "update_check": "High Availability status",
            },
            {
                "action": {
                    "message": 'Refer to the Upgrade Advisor Plan or the "What should I verify before I upgrade with or without Upgrade Advisor" section in the "Upgrade ONTAP" documentation for the remaining validation checks that need to be performed before update.'
                },
                "issue": {
                    "message": 'Manual validation checks need to be performed. Refer to the Upgrade Advisor Plan or the "What should I verify before I upgrade with or without Upgrade Advisor" section in the "Upgrade ONTAP" documentation for the remaining validation checks that need to be performed before update. Failing to do so can result in an update failure or an I/O disruption.'
                },
                "status": "warning",
                "update_check": "Manual checks",
            },
        ],
        "estimated_duration": 600,
        "_links": {"self": {"href": "/api/cluster/software"}},
        "version": "9.7.0",
        "nodes": [
            {
                "firmware": {
                    "dqp": {
                        "revision": "20200117",
                        "version": "3.17",
                        "record_count": {
                            "device": 29,
                            "alias": 200,
                            "system": 3,
                            "drive": 680,
                        },
                        "file_name": "qual_devices_v2",
                    },
                    "shelf": {"update_status": "idle", "in_progress_count": 2},
                    "cluster_fw_progress": [
                        {
                            "update_type": "automatic_update",
                            "job": {
                                "_links": {
                                    "self": {
                                        "href": "/api/cluster/jobs/5a21663c-a9a0-11ea-af9a-005056bb44d7"
                                    }
                                },
                                "uuid": "5a21663c-a9a0-11ea-af9a-005056bb44d7",
                            },
                            "update_state": [
                                {
                                    "message": "Cannot open the local staging zip file.",
                                    "worker_node": {
                                        "uuid": "fcd40f70-f531-11eb-b235-005056bb3498",
                                        "name": "Node 1",
                                    },
                                    "code": 2228325,
                                    "status": "failed",
                                    "attempts": 3,
                                },
                                {
                                    "message": "Success",
                                    "worker_node": {
                                        "uuid": "fcd40f70-f531-11eb-b235-005056bb3498",
                                        "name": "Node 2",
                                    },
                                    "code": 0,
                                    "status": "complete",
                                    "attempts": 3,
                                },
                            ],
                            "zip_file_name": "abc.zip",
                        },
                        {
                            "update_type": "automatic_update",
                            "job": {
                                "_links": {
                                    "self": {
                                        "href": "/api/cluster/jobs/5a21663c-a9a0-11ea-af9a-005056bb44d7"
                                    }
                                },
                                "uuid": "5a21663c-a9a0-11ea-af9a-005056bb44d7",
                            },
                            "update_state": [
                                {
                                    "message": "Cannot open the local staging zip file.",
                                    "worker_node": {
                                        "uuid": "fcd40f70-f531-11eb-b235-005056bb3498",
                                        "name": "Node 1",
                                    },
                                    "code": 2228325,
                                    "status": "failed",
                                    "attempts": 3,
                                },
                                {
                                    "message": "Success",
                                    "worker_node": {
                                        "uuid": "fcd40f70-f531-11eb-b235-005056bb3498",
                                        "name": "Node 2",
                                    },
                                    "code": 0,
                                    "status": "complete",
                                    "attempts": 3,
                                },
                            ],
                            "zip_file_name": "xyz.zip",
                        },
                    ],
                    "disk": {
                        "update_status": "idle",
                        "average_duration_per_disk": 120,
                        "total_completion_estimate": 0,
                        "num_waiting_download": 0,
                    },
                    "sp_bmc": {
                        "image": " primary",
                        "end_time": "2018-05-21T09:53:04+05:30",
                        "running_version": "1.2.3.4",
                        "is_current": True,
                        "in_progress": False,
                        "percent_done": 100,
                        "fw_type": "SP",
                        "start_time": "2018-05-21T09:53:04+05:30",
                    },
                },
                "version": "9.5.0",
            }
        ],
    }
)

```
</div>
</div>

---
#### 2. Updating the cluster
The following example shows how to initiate a cluster software upgrade. You must validate the package before the software upgrade starts. Set the `skip_warnings` field to `true` to skip validation warnings and start the software package upgrade. You can specify the `stabilize_minutes` value between 1 to 60 minutes. Setting `stabilize_minutes` allows each node a specified amount of time to stabilize after a reboot; the default is 8 minutes. If the value of `show_validation_details` is set to "true", then all validation details will be shown in the output.
<br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Software

with HostConnection("<mgmt_ip>", username="admin", password="password", verify=False):
    resource = Software()
    resource.version = "9.5.0"
    resource.patch(hydrate=True, skip_warnings=True)

```

---
The call to update the software cluster version returns the job UUID, including a HAL link to retrieve details about the job. The job object includes a `state` field and a message to indicate the progress of the job. When the job is complete and the application is fully created, the message indicates success and the `state` field of the job is set to `success`.
<br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Job

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Job(uuid="f587d316-5feb-11e8-b0e0-005056956dfc")
    resource.get()
    print(resource)

```
<div class="try_it_out">
<input id="example2_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example2_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example2_result" class="try_it_out_content">
```
Job(
    {
        "message": "success",
        "state": "success",
        "code": 0,
        "uuid": "f587d316-5feb-11e8-b0e0-005056956dfc",
        "_links": {
            "self": {"href": "/api/cluster/jobs/f587d316-5feb-11e8-b0e0-005056956dfc"}
        },
        "description": "PATCH /api/cluster/software",
    }
)

```
</div>
</div>

---
You can check the update progress information in the GET /cluster/software endpoint. The following example shows how to check the progress of an update after setting the `skip_warnings` field to `true`. Each node's object also includes information about the firmware update status on the node.      <br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Software

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Software()
    resource.get()
    print(resource)

```
<div class="try_it_out">
<input id="example6_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example6_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example6_result" class="try_it_out_content">
```
Software(
    {
        "status_details": [
            {
                "end_time": "2019-01-14T23:12:14+05:30",
                "issue": {"code": 10551400, "message": "Installing software image."},
                "node": {"name": "node1"},
                "start_time": "2019-01-14T23:12:14+05:30",
                "name": "do-download-job",
            },
            {
                "end_time": "2019-01-14T23:12:14+05:30",
                "issue": {"code": 10551400, "message": "Installing software image."},
                "node": {"name": "node2"},
                "start_time": "2019-01-14T23:12:14+05:30",
                "name": "do-download-job",
            },
        ],
        "elapsed_duration": 63,
        "state": "in_progress",
        "validation_results": [
            {
                "action": {
                    "message": 'Refer to the Upgrade Advisor Plan or the "What should I verify before I upgrade with or without Upgrade Advisor" section in the "Upgrade ONTAP" documentation for the remaining validation checks that need to be performed before update.'
                },
                "issue": {
                    "message": 'Manual validation checks need to be performed. Refer to the Upgrade Advisor Plan or the "What should I verify before I upgrade with or without Upgrade Advisor" section in the "Upgrade ONTAP" documentation for the remaining validation checks that need to be performed before update. Failing to do so can result in an update failure or an I/O disruption.'
                },
                "status": "warning",
                "update_check": "Manual checks",
            }
        ],
        "pending_version": "9.7.0",
        "estimated_duration": 5220,
        "_links": {"self": {"href": "/api/cluster/software"}},
        "version": "9.7.0",
        "nodes": [
            {
                "firmware": {
                    "dqp": {
                        "revision": "20200117",
                        "version": "3.17",
                        "record_count": {
                            "device": 29,
                            "alias": 200,
                            "system": 3,
                            "drive": 680,
                        },
                        "file_name": "qual_devices_v2",
                    },
                    "shelf": {"update_status": "idle", "in_progress_count": 2},
                    "cluster_fw_progress": [
                        {
                            "update_type": "automated_update",
                            "job": {
                                "_links": {
                                    "self": {
                                        "href": "/api/cluster/jobs/5a21663c-a9a0-11ea-af9a-005056bb44d7"
                                    }
                                },
                                "uuid": "5a21663c-a9a0-11ea-af9a-005056bb44d7",
                            },
                            "update_state": [
                                {
                                    "message": "Cannot open the local staging zip file.",
                                    "worker_node": {
                                        "uuid": "fcd40f70-f531-11eb-b235-005056bb3497",
                                        "name": "Node 3",
                                    },
                                    "code": 2228325,
                                    "status": "failed",
                                    "attempts": 3,
                                },
                                {
                                    "message": "Success",
                                    "worker_node": {
                                        "uuid": "fcd40f70-f531-11eb-b235-005056bb3498",
                                        "name": "Node 4",
                                    },
                                    "code": 0,
                                    "status": "complete",
                                    "attempts": 3,
                                },
                            ],
                            "zip_file_name": "abc.zip",
                        },
                        {
                            "update_type": "automated_update",
                            "job": {
                                "_links": {
                                    "self": {
                                        "href": "/api/cluster/jobs/5a21663c-a9a0-11ea-af9a-005056bb44d7"
                                    }
                                },
                                "uuid": "5a21663c-a9a0-11ea-af9a-005056bb44d7",
                            },
                            "update_state": [
                                {
                                    "message": "Cannot open the local staging zip file.",
                                    "worker_node": {
                                        "uuid": "fcd40f70-f531-11eb-b235-005056bb3497",
                                        "name": "Node 1",
                                    },
                                    "code": 2228325,
                                    "status": "failed",
                                    "attempts": 3,
                                },
                                {
                                    "message": "Success",
                                    "worker_node": {
                                        "uuid": "fcd40f70-f531-11eb-b235-005056bb3497",
                                        "name": "Node 2",
                                    },
                                    "code": 0,
                                    "status": "complete",
                                    "attempts": 3,
                                },
                            ],
                            "zip_file_name": "xyz.zip",
                        },
                    ],
                    "disk": {
                        "update_status": "idle",
                        "average_duration_per_disk": 120,
                        "total_completion_estimate": 0,
                        "num_waiting_download": 0,
                    },
                    "sp_bmc": {
                        "image": " primary",
                        "end_time": "2018-05-21T09:53:04+05:30",
                        "running_version": "1.2.3.4",
                        "is_current": True,
                        "in_progress": False,
                        "percent_done": 100,
                        "fw_type": "SP",
                        "start_time": "2018-05-21T09:53:04+05:30",
                    },
                },
                "version": "9.5.0",
            }
        ],
        "update_details": [
            {
                "elapsed_duration": 10,
                "phase": "Data ONTAP updates",
                "estimated_duration": 4620,
                "node": {"name": "node1"},
            },
            {
                "elapsed_duration": 10,
                "phase": "Data ONTAP updates",
                "estimated_duration": 4620,
                "node": {"name": "node2"},
            },
        ],
    }
)

```
</div>
</div>

---
In the case of a post update check failure, the details are available under the heading "post_update_checks" in the GET /cluster/software endpoint.
The following example shows how to check the progress of an update after a post update check has failed. Each node's object also includes information about the firmware update status on the node.      <br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Software

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Software()
    resource.get()
    print(resource)

```
<div class="try_it_out">
<input id="example7_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example7_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example7_result" class="try_it_out_content">
```
Software(
    {
        "status_details": [
            {
                "end_time": "2019-01-14T23:12:14+05:30",
                "issue": {"code": 0, "message": "Image update complete."},
                "node": {"name": "node1"},
                "start_time": "2019-01-14T23:12:14+05:30",
                "name": "do-download-job",
            },
            {
                "end_time": "2019-01-14T23:12:14+05:30",
                "issue": {"code": 0, "message": "Image update complete."},
                "node": {"name": "node2"},
                "start_time": "2019-01-14T23:12:14+05:30",
                "name": "do-download-job",
            },
        ],
        "elapsed_duration": 63,
        "state": "in_progress",
        "validation_results": [
            {
                "action": {
                    "message": 'Refer to the Upgrade Advisor Plan or the "What should I verify before I upgrade with or without Upgrade Advisor" section in the "Upgrade ONTAP" documentation for the remaining validation checks that need to be performed before update.'
                },
                "issue": {
                    "message": 'Manual validation checks need to be performed. Refer to the Upgrade Advisor Plan or the "What should I verify before I upgrade with or without Upgrade Advisor" section in the "Upgrade ONTAP" documentation for the remaining validation checks that need to be performed before update. Failing to do so can result in an update failure or an I/O disruption.'
                },
                "status": "warning",
                "update_check": "Manual checks",
            }
        ],
        "pending_version": "9.7.0",
        "estimated_duration": 5220,
        "post_update_checks": [
            {
                "action": {"message": "Ensure all aggregates are online."},
                "issue": {"message": "Not all aggregates are online"},
                "status": "error",
                "update_check": "Aggregate Health Status",
            },
            {
                "action": {
                    "message": "Ensure storage failover is enabled on all nodes of the cluster."
                },
                "issue": {
                    "message": "Storage failover is not enabled on nodes of the cluster."
                },
                "status": "error",
                "update_check": "HA Health Status",
            },
        ],
        "_links": {"self": {"href": "/api/cluster/software"}},
        "version": "9.7.0",
        "nodes": [
            {
                "firmware": {
                    "dqp": {
                        "revision": "20200117",
                        "version": "3.17",
                        "record_count": {
                            "device": 29,
                            "alias": 200,
                            "system": 3,
                            "drive": 680,
                        },
                        "file_name": "qual_devices_v2",
                    },
                    "shelf": {"update_status": "idle", "in_progress_count": 2},
                    "cluster_fw_progress": [
                        {
                            "update_type": "automated_update",
                            "job": {
                                "_links": {
                                    "self": {
                                        "href": "/api/cluster/jobs/5a21663c-a9a0-11ea-af9a-005056bb44d7"
                                    }
                                },
                                "uuid": "5a21663c-a9a0-11ea-af9a-005056bb44d7",
                            },
                            "update_state": [
                                {
                                    "message": "<message catalog text>",
                                    "worker_node": {
                                        "uuid": "fcd40f70-f531-11eb-b235-005056bb3497",
                                        "name": "Node 1",
                                    },
                                    "code": 3,
                                    "status": "working",
                                    "attempts": 3,
                                },
                                {
                                    "message": "Error message",
                                    "worker_node": {
                                        "uuid": "fcd40f70-f531-11eb-b235-005056bb3497",
                                        "name": "Node 2",
                                    },
                                    "code": 0,
                                    "status": "completed",
                                    "attempts": 3,
                                },
                            ],
                            "zip_file_name": "abc.zip",
                        },
                        {
                            "update_type": "automated_update",
                            "job": {
                                "_links": {
                                    "self": {
                                        "href": "/api/cluster/jobs/5a21663c-a9a0-11ea-af9a-005056bb44d7"
                                    }
                                },
                                "uuid": "5a21663c-a9a0-11ea-af9a-005056bb44d7",
                            },
                            "update_state": [
                                {
                                    "message": "Error message",
                                    "worker_node": {
                                        "uuid": "fcd40f70-f531-11eb-b235-005056bb3497",
                                        "name": "Node 1",
                                    },
                                    "code": 0,
                                    "status": "completed",
                                    "attempts": 1,
                                },
                                {
                                    "message": "Error message",
                                    "worker_node": {
                                        "uuid": "fcd40f70-f531-11eb-b235-005056bb3497",
                                        "name": "Node 2",
                                    },
                                    "code": 0,
                                    "status": "completed",
                                    "attempts": 3,
                                },
                            ],
                            "zip_file_name": "xyz.zip",
                        },
                    ],
                    "disk": {
                        "update_status": "idle",
                        "average_duration_per_disk": 120,
                        "total_completion_estimate": 0,
                        "num_waiting_download": 0,
                    },
                    "sp_bmc": {
                        "image": " primary",
                        "end_time": "2018-05-21T09:53:04+05:30",
                        "running_version": "1.2.3.4",
                        "is_current": True,
                        "in_progress": True,
                        "percent_done": 100,
                        "fw_type": "SP",
                        "start_time": "2018-05-21T09:53:04+05:30",
                    },
                },
                "version": "9.5.0",
            }
        ],
        "update_details": [
            {
                "elapsed_duration": 3120,
                "phase": "Data ONTAP updates",
                "estimated_duration": 4620,
                "node": {"name": "node1"},
            },
            {
                "elapsed_duration": 3210,
                "phase": "Data ONTAP updates",
                "estimated_duration": 4620,
                "node": {"name": "node2"},
            },
            {
                "elapsed_duration": 10,
                "phase": "Post-update checks",
                "estimated_duration": 600,
                "node": {"name": "node2"},
            },
        ],
    }
)

```
</div>
</div>

---
#### 3. Pausing, resuming or canceling an upgrade
The following example shows how to `pause` an ongoing cluster software package upgrade. Set the `action` field to `pause`, `resume`, or `cancel` to pause, resume or cancel the upgrade respectively. Not all update operations support these actions. An update can only be resumed if it is in the paused state.
<br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Software

with HostConnection("<mgmt_ip>", username="admin", password="password", verify=False):
    resource = Software()
    resource.version = "9.5.0"
    resource.patch(hydrate=True, action="pause")

```

---
The call to update the software cluster version and/or firmware version returns the job UUID, including a HAL link to retrieve details about the job. The job object includes a `state` field and a message to indicate the progress of the job. When the job is complete and the application is fully created, the message indicates success and the `state` field of the job is set to `success`.
<br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Job

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Job(uuid="f587d316-5feb-11e8-b0e0-005056956dfc")
    resource.get()
    print(resource)

```
<div class="try_it_out">
<input id="example2_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example2_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example2_result" class="try_it_out_content">
```
Job(
    {
        "message": "success",
        "state": "success",
        "code": 0,
        "uuid": "f587d316-5feb-11e8-b0e0-005056956dfc",
        "_links": {
            "self": {"href": "/api/cluster/jobs/f587d316-5feb-11e8-b0e0-005056956dfc"}
        },
        "description": "PATCH /api/cluster/software",
    }
)

```
</div>
</div>

---
You can check the progress of the upgrade in the GET /cluster/software endpoint. The following example shows how to check the progress of the pause upgrade state after setting the `action` field to `pause`.
<br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Software

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Software()
    resource.get()
    print(resource)

```
<div class="try_it_out">
<input id="example10_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example10_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example10_result" class="try_it_out_content">
```
Software(
    {
        "status_details": [
            {
                "issue": {"code": 10551400, "message": "Installing software image."},
                "node": {"name": "node1"},
                "start_time": "2019-01-08T02:54:36+05:30",
            },
            {
                "issue": {"code": 10551400, "message": "Installing software image."},
                "node": {"name": "node2"},
                "start_time": "2019-01-08T02:54:36+05:30",
            },
        ],
        "elapsed_duration": 103,
        "state": "pause_pending",
        "validation_results": [
            {
                "action": {
                    "message": 'Refer to the Upgrade Advisor Plan or the "What should I verify before I upgrade with or without Upgrade Advisor" section in the "Upgrade ONTAP" documentation for the remaining validation checks that need to be performed before update.'
                },
                "issue": {
                    "message": 'Manual validation checks need to be performed. Refer to the Upgrade Advisor Plan or the "What should I verify before I upgrade with or without Upgrade Advisor" section in the "Upgrade ONTAP" documentation for the remaining validation checks that need to be performed before update. Failing to do so can result in an update failure or an I/O disruption.'
                },
                "status": "warning",
                "update_check": "Manual checks",
            }
        ],
        "pending_version": "9.7.0",
        "estimated_duration": 5220,
        "_links": {"self": {"href": "/api/cluster/software"}},
        "version": "9.7.0",
        "nodes": [
            {
                "firmware": {
                    "dqp": {
                        "revision": "20200117",
                        "version": "3.17",
                        "record_count": {
                            "device": 29,
                            "alias": 200,
                            "system": 3,
                            "drive": 680,
                        },
                        "file_name": "qual_devices_v2",
                    },
                    "shelf": {"update_status": "idle", "in_progress_count": 2},
                    "cluster_fw_progress": [
                        {
                            "update_type": "automated_update",
                            "job": {
                                "_links": {
                                    "self": {
                                        "href": "/api/cluster/jobs/5a21663c-a9a0-11ea-af9a-005056bb44d7"
                                    }
                                },
                                "uuid": "5a21663c-a9a0-11ea-af9a-005056bb44d7",
                            },
                            "update_state": [
                                {
                                    "message": "Cannot open the local staging zip file.",
                                    "worker_node": {
                                        "uuid": "fcd40f70-f531-11eb-b235-005056bb3497",
                                        "name": "Node 1",
                                    },
                                    "code": 2228325,
                                    "status": "failed",
                                    "attempts": 3,
                                },
                                {
                                    "message": "Success",
                                    "code": 0,
                                    "status": "complete",
                                    "attempts": 3,
                                },
                            ],
                            "zip_file_name": "abc.zip",
                        },
                        {
                            "update_type": "automated_update",
                            "job": {
                                "_links": {
                                    "self": {
                                        "href": "/api/cluster/jobs/5a21663c-a9a0-11ea-af9a-005056bb44d7"
                                    }
                                },
                                "uuid": "5a21663c-a9a0-11ea-af9a-005056bb44d7",
                            },
                            "update_state": [
                                {
                                    "message": "Cannot open the local staging zip file.",
                                    "worker_node": {
                                        "uuid": "fcd40f70-f531-11eb-b235-005056bb3497",
                                        "name": "Node 1",
                                    },
                                    "code": 2228325,
                                    "status": "failed",
                                    "attempts": 3,
                                },
                                {
                                    "message": "Success",
                                    "code": 0,
                                    "status": "complete",
                                    "attempts": 3,
                                },
                            ],
                            "zip_file_name": "xyz.zip",
                        },
                    ],
                    "disk": {
                        "update_status": "idle",
                        "average_duration_per_disk": 120,
                        "total_completion_estimate": 0,
                        "num_waiting_download": 0,
                    },
                    "sp_bmc": {
                        "image": " primary",
                        "end_time": "2018-05-21T09:53:04+05:30",
                        "running_version": "1.2.3.4",
                        "is_current": True,
                        "in_progress": False,
                        "percent_done": 100,
                        "fw_type": "SP",
                        "start_time": "2018-05-21T09:53:04+05:30",
                    },
                },
                "version": "9.5.0",
            }
        ],
        "update_details": [
            {
                "elapsed_duration": 54,
                "phase": "Pre-update checks",
                "estimated_duration": 600,
                "node": {"name": "node1"},
            },
            {
                "elapsed_duration": 49,
                "phase": "Data ONTAP updates",
                "estimated_duration": 4620,
                "node": {"name": "node2"},
            },
            {
                "elapsed_duration": 49,
                "phase": "Data ONTAP updates",
                "estimated_duration": 4620,
            },
        ],
    }
)

```
</div>
</div>

---
### Downloading the software package
The following example shows how to download the software/firmware package from an HTTP or FTP server. Provide the `url`, `username`, and `password`, if required, to start the download of the package to the cluster.
<br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import SoftwarePackageDownload

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = SoftwarePackageDownload()
    resource.url = "http://server/package"
    resource.username = "admin"
    resource.password = "*********"
    resource.post(hydrate=True, return_timeout=0)
    print(resource)

```
<div class="try_it_out">
<input id="example11_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example11_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example11_result" class="try_it_out_content">
```
SoftwarePackageDownload(
    {"url": "http://server/package", "password": "*********", "username": "admin"}
)

```
</div>
</div>

---
The call to download the software/firmware package returns the job UUID, including a HAL link to retrieve details about the job. The job object includes a `state` field and a message to indicate the progress of the job. When the job is complete and the application is fully created, the message indicates success and the job `state` field is set to `success`.
<br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Job

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Job(uuid="f587d316-5feb-11e8-b0e0-005056956dfc")
    resource.get()
    print(resource)

```
<div class="try_it_out">
<input id="example12_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example12_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example12_result" class="try_it_out_content">
```
Job(
    {
        "message": "success",
        "state": "success",
        "code": 0,
        "uuid": "f587d316-5feb-11e8-b0e0-005056956dfc",
        "_links": {
            "self": {"href": "/api/cluster/jobs/f587d316-5feb-11e8-b0e0-005056956dfc"}
        },
        "description": "POST /api/cluster/software/download",
    }
)

```
</div>
</div>

---
### Checking the progress of the software package being downloaded from an HTTP or FTP server
The following example shows how to retrieve the progress status of the software package being
downloaded from a HTTP or FTP server.
<br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import SoftwarePackageDownload

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = SoftwarePackageDownload()
    resource.get()
    print(resource)

```
<div class="try_it_out">
<input id="example13_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example13_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example13_result" class="try_it_out_content">
```
SoftwarePackageDownload({})

```
</div>
</div>

---
#### HTTPS error codes
The following is a list of possible error codes that can be returned during a package download operation.
<br/>
ONTAP Error Response Codes
| Error Code | Description |
| ---------- | ----------- |
| 2228324 | Failed to access the remote zip file on node. |
| 2228325 | Cannot open local staging ZIP file |
| 2228326 | File copy to local staging failed. |
| 2228327 | Firmware file already exists. |
| 2228328 | Firmware update of node failed. |
| 2228329 | Attempt to start worker on node failed |
| 2228330 | Uploaded firmware file is not present. |
| 2228331 | Copy of file from webserver failed. |
| 2228428 | Firmware update  completed with errors |
| 2228429 | Firmware update completed. |
| 10551327 | Package image with the same name already exists. |
| 10551357 | Cannot perform an update when a previous update is still in progress. |
| 10551381 | Package download failed. |
| 10551382 | Package download is still running. |
| 10551384 | Package download has not started. |
| 10551496 | Failed to download package. |
| 10551797 | Internal error. Failed to check if file upload is enabled. Contact technical support for assistance. |
Also see the table of common errors in the <a href="#Response_body">Response body</a> overview section of this documentation.
---
### Uploading a software/firmware package
The following example shows how to upload a software package.
<br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Software

with HostConnection(
    "<mgmt-ip>", username="username", password="password", verify=False
):
    resource = Software()
    resource.upload()

```
<div class="try_it_out">
<input id="example14_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example14_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example14_result" class="try_it_out_content">
```
Software({})

```
</div>
</div>

---
#### HTTPS error codes
The following is a list of possible error codes that can be returned during a package upload operation.
<br/>
ONTAP Error Response Codes
| Error Code | Description |
| ---------- | ----------- |
| 2228324 | Failed to access the remote zip file on node. |
| 2228325 | Cannot open local staging ZIP file |
| 2228326 | File copy to local staging failed. |
| 2228327 | Firmware file already exists. |
| 2228328 | Firmware update of node failed. |
| 2228329 | Attempt to start worker on node failed |
| 2228330 | Uploaded firmware file is not present. |
| 2228331 | Copy of file from webserver failed. |
| 2228428 | Firmware update  completed with errors |
| 2228429 | Firmware update completed. |
| 10551395 | Validation checks failed with warnings. |
| 10551797 | Internal error. Failed to check if file upload is enabled. |
| 10551798 | File upload is disabled. Enable file upload by setting "ApacheUploadEnabled 1" in the web services configuration file or contact technical support for assistance. |
| 10551800 | Internal error. Access permissions restrict file upload. This is likely due to a bad web jail setup. Contact technical support for assistance. |
| 10551801 | Internal error. A read/write error occurred when uploading this file. Contact technical support for assistance |
| 10551802 | An invalid argument was supplied to create a file handle. Try uploading the file again or contact technical support for assistance. |
| 10551803 | An unknown error occurred. Retry file upload operation again or contact technical support for assistance. |
| 10551804 | Internal error. There is not sufficient space in the file upload directory to upload this file. Contact technical support for assistance. |
| 10551805 | Internal error in JAIL setup. Contact technical support for assistance. |
| 10551806 | Internal error. Failed to write to file in the webjail directory. Contact technical support for assistance. |
| 10551807 | The request must only contain a single file. More than one file per request is not supported. |
| 10551808 | The request must be of type multipart/form-data. |
Also see the table of common errors in the <a href="#Response_body">Response body</a> overview section of this documentation.
---
### Retrieving cluster software packages information
The following example shows how to retrieve the ONTAP software packages in a cluster.
<br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import SoftwarePackage

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    print(list(SoftwarePackage.get_collection(return_timeout=15)))

```
<div class="try_it_out">
<input id="example15_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example15_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example15_result" class="try_it_out_content">
```
[
    SoftwarePackage(
        {
            "_links": {"self": {"href": "/api/cluster/software/packages/9.7.0"}},
            "version": "9.7.0",
        }
    ),
    SoftwarePackage(
        {
            "_links": {"self": {"href": "/api/cluster/software/packages/9.5.0"}},
            "version": "9.5.0",
        }
    ),
]

```
</div>
</div>

---
The following example shows how to retrieve the details of a given cluster software package.
<br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import SoftwarePackage

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = SoftwarePackage(version="9.7.0")
    resource.get()
    print(resource)

```
<div class="try_it_out">
<input id="example16_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example16_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example16_result" class="try_it_out_content">
```
SoftwarePackage(
    {
        "_links": {"self": {"href": "/api/cluster/software/packages/9.7.0"}},
        "create_time": "2018-05-21T10:06:59+05:30",
        "version": "9.7.0",
    }
)

```
</div>
</div>

---
### Deleting a cluster software package
The following example shows how to delete a package from the cluster. You need to provide the package version that you want to delete. The software package delete creates a job to perform the delete operation.
<br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import SoftwarePackage

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = SoftwarePackage(version="9.6.0")
    resource.delete()

```

---
The call to delete the package returns the job UUID, including a HAL link to retrieve details about the job. The job object includes a `state` field and a message to indicate the progress of the job. When the job is complete and the application is fully created, the message indicates success and the job `state` field is set to `success`.
<br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Job

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Job(uuid="f587d316-5feb-11e8-b0e0-005056956dfc")
    resource.get()
    print(resource)

```
<div class="try_it_out">
<input id="example18_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example18_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example18_result" class="try_it_out_content">
```
Job(
    {
        "message": "success",
        "state": "success",
        "code": 0,
        "uuid": "f587d316-5feb-11e8-b0e0-005056956dfc",
        "_links": {
            "self": {"href": "/api/cluster/jobs/f587d316-5feb-11e8-b0e0-005056956dfc"}
        },
        "description": "DELETE /api/cluster/software/packages/9.6.0",
    }
)

```
</div>
</div>

---
#### HTTPS error codes
The following is a list of possible error codes that can be returned during a package delete operation.
<br/>
```
# ONTAP Error Response codes
| ----------- | -------------------------------------------------------- |
| Error codes |                     Description                          |
| ----------- | -------------------------------------------------------- |
| 10551315    | Package store is empty                                   |
| 10551322    | Error in retrieving package cleanup status               |
| 10551323    | Error in cleaning up package information on a node       |
| 10551324    | Error in cleaning up package information on both nodes   |
| 10551325    | Package does not exist on the system                     |
| 10551326    | Error in deleting older package cleanup tasks            |
| 10551346    | Package delete failed since a validation is in progress  |
| 10551347    | Package delete failed since an update is in progress     |
| 10551367    | A package synchronization is in progress                 |
| 10551388    | Package delete operation timed out                       |
| 10551566    | Validation is not completed on the MetroCluster partner  |
|             | cluster                                                  |
| 10551567    | Package version is not available in the package          |
|             | repository on the MetroCluster partner cluster           |
| ----------- | -------------------------------------------------------- |
```
---
### Retrieving software installation history information
The following example shows how to:
   - retrieve the software package installation history information.
   - display specific node level software installation history information.
   - provide all the attributes by default in response when the self referential link is not present.
<br/>
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import SoftwareHistory

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    print(list(SoftwareHistory.get_collection()))

```
<div class="try_it_out">
<input id="example19_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example19_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example19_result" class="try_it_out_content">
```
SoftwareHistory(
    {
        "to_version": "9.5.0",
        "state": "successful",
        "from_version": "9.4.0",
        "end_time": "2018-05-21T10:14:51+05:30",
        "node": {
            "_links": {
                "self": {
                    "href": "/api/cluster/nodes/58cd3a2b-af63-11e8-8b0d-0050568e7279"
                }
            },
            "uuid": "58cd3a2b-af63-11e8-8b0d-0050568e7279",
            "name": "sti70-vsim-ucs165n",
        },
        "start_time": "2018-09-03T16:18:46+05:30",
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


__all__ = ["Software", "SoftwareSchema"]
__pdoc__ = {
    "SoftwareSchema.resource": False,
    "SoftwareSchema.opts": False,
    "Software.software_show": False,
    "Software.software_create": False,
    "Software.software_modify": False,
    "Software.software_delete": False,
}


class SoftwareSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the Software object"""

    links = marshmallow_fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE, allow_none=True)
    r""" The links field of the software."""

    action = marshmallow_fields.Str(
        data_key="action",
        validate=enum_validation(['pause', 'cancel', 'resume']),
        allow_none=True,
    )
    r""" User triggered action to apply to the install operation

Valid choices:

* pause
* cancel
* resume"""

    elapsed_duration = Size(
        data_key="elapsed_duration",
        allow_none=True,
    )
    r""" Elapsed time during the upgrade or validation operation

Example: 2140"""

    estimated_duration = Size(
        data_key="estimated_duration",
        allow_none=True,
    )
    r""" Overall estimated time for completion of the upgrade or validation operation.

Example: 5220"""

    metrocluster = marshmallow_fields.Nested("netapp_ontap.models.software_reference_metrocluster.SoftwareReferenceMetroclusterSchema", data_key="metrocluster", unknown=EXCLUDE, allow_none=True)
    r""" The metrocluster field of the software."""

    nodes = marshmallow_fields.List(marshmallow_fields.Nested("netapp_ontap.models.software_node.SoftwareNodeSchema", unknown=EXCLUDE, allow_none=True), data_key="nodes", allow_none=True)
    r""" List of nodes, active versions, and firmware update progressions."""

    pending_version = marshmallow_fields.Str(
        data_key="pending_version",
        allow_none=True,
    )
    r""" Version being installed on the system.

Example: ONTAP_X_1"""

    post_update_checks = marshmallow_fields.List(marshmallow_fields.Nested("netapp_ontap.models.software_validation.SoftwareValidationSchema", unknown=EXCLUDE, allow_none=True), data_key="post_update_checks", allow_none=True)
    r""" List of failed post-update checks' warnings, errors, and advice."""

    state = marshmallow_fields.Str(
        data_key="state",
        validate=enum_validation(['in_progress', 'waiting', 'paused_by_user', 'paused_on_error', 'completed', 'canceled', 'failed', 'pause_pending', 'cancel_pending']),
        allow_none=True,
    )
    r""" Operational state of the upgrade

Valid choices:

* in_progress
* waiting
* paused_by_user
* paused_on_error
* completed
* canceled
* failed
* pause_pending
* cancel_pending"""

    status_details = marshmallow_fields.List(marshmallow_fields.Nested("netapp_ontap.models.software_status_details.SoftwareStatusDetailsSchema", unknown=EXCLUDE, allow_none=True), data_key="status_details", allow_none=True)
    r""" Display status details."""

    update_details = marshmallow_fields.List(marshmallow_fields.Nested("netapp_ontap.models.software_update_details.SoftwareUpdateDetailsSchema", unknown=EXCLUDE, allow_none=True), data_key="update_details", allow_none=True)
    r""" Display update progress details."""

    validation_results = marshmallow_fields.List(marshmallow_fields.Nested("netapp_ontap.models.software_validation.SoftwareValidationSchema", unknown=EXCLUDE, allow_none=True), data_key="validation_results", allow_none=True)
    r""" List of validation warnings, errors, and advice."""

    version = marshmallow_fields.Str(
        data_key="version",
        allow_none=True,
    )
    r""" Version of ONTAP installed and currently active on the system. During PATCH, using the 'validate_only' parameter on the request executes pre-checks, but does not perform the full installation.

Example: ONTAP_X"""

    @property
    def resource(self):
        return Software

    gettable_fields = [
        "links",
        "action",
        "elapsed_duration",
        "estimated_duration",
        "metrocluster",
        "nodes",
        "pending_version",
        "post_update_checks",
        "state",
        "status_details",
        "update_details",
        "validation_results",
        "version",
    ]
    """links,action,elapsed_duration,estimated_duration,metrocluster,nodes,pending_version,post_update_checks,state,status_details,update_details,validation_results,version,"""

    patchable_fields = [
        "action",
        "metrocluster",
        "version",
    ]
    """action,metrocluster,version,"""

    postable_fields = [
        "action",
        "metrocluster",
        "version",
    ]
    """action,metrocluster,version,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in Software.get_collection(fields=field)]
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
            raise NetAppRestError("Software modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class Software(Resource):
    """Allows interaction with Software objects on the host"""

    _schema = SoftwareSchema
    _path = "/api/cluster/software"
    _action_form_data_parameters = { 'file':'file', }






    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the software profile of a cluster.
### Related ONTAP commands
* `cluster image show`
* `cluster image show-update-progress`
* `system node image package show`
### Learn more
* [`DOC /cluster/software`](#docs-cluster-cluster_software)
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="software show")
        def software_show(
            fields: List[str] = None,
        ) -> ResourceTable:
            """Fetch a single Software resource

            Args:
                action: User triggered action to apply to the install operation
                elapsed_duration: Elapsed time during the upgrade or validation operation
                estimated_duration: Overall estimated time for completion of the upgrade or validation operation.
                pending_version: Version being installed on the system.
                state: Operational state of the upgrade
                version: Version of ONTAP installed and currently active on the system. During PATCH, using the 'validate_only' parameter on the request executes pre-checks, but does not perform the full installation.
            """

            kwargs = {}
            if action is not None:
                kwargs["action"] = action
            if elapsed_duration is not None:
                kwargs["elapsed_duration"] = elapsed_duration
            if estimated_duration is not None:
                kwargs["estimated_duration"] = estimated_duration
            if pending_version is not None:
                kwargs["pending_version"] = pending_version
            if state is not None:
                kwargs["state"] = state
            if version is not None:
                kwargs["version"] = version
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            resource = Software(
                **kwargs
            )
            resource.get()
            return [resource]


    def patch(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates the cluster software version.
Important note:
  * Setting 'version' triggers the package installation.
  * To validate the package for installation but not perform the installation, use the `validate_only` field on the request.
### Required properties
* `version` - Software version to be installed on the cluster.
### Recommended optional parameters
* `validate_only` - Required to validate a software package before an upgrade.
* `skip_warnings` - Used to skip validation warnings when starting a software upgrade.
* `action` - Used to pause, resume, or cancel an ongoing software upgrade.
* `stabilize_minutes` - Specifies a custom value between 1 to 60 minutes that allows each node a specified amount of time to stabilize after a reboot; the default is 8 minutes.
* `estimate_only` - Estimates the time duration; does not perform any update.
* `nodes_to_update` - Specifies a subset of the cluster's nodes for update.
* `show_validation_details` - If the value is set to true, then all validation details will be shown in the output.
### Related ONTAP commands
* `cluster image validate`
* `cluster image update`
* `cluster image pause-update`
* `cluster image resume-update`
* `cluster image cancel-update`
### Learn more
* [`DOC /cluster/software`](#docs-cluster-cluster_software)
"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="software modify")
        async def software_modify(
        ) -> ResourceTable:
            """Modify an instance of a Software resource

            Args:
                action: User triggered action to apply to the install operation
                query_action: User triggered action to apply to the install operation
                elapsed_duration: Elapsed time during the upgrade or validation operation
                query_elapsed_duration: Elapsed time during the upgrade or validation operation
                estimated_duration: Overall estimated time for completion of the upgrade or validation operation.
                query_estimated_duration: Overall estimated time for completion of the upgrade or validation operation.
                pending_version: Version being installed on the system.
                query_pending_version: Version being installed on the system.
                state: Operational state of the upgrade
                query_state: Operational state of the upgrade
                version: Version of ONTAP installed and currently active on the system. During PATCH, using the 'validate_only' parameter on the request executes pre-checks, but does not perform the full installation.
                query_version: Version of ONTAP installed and currently active on the system. During PATCH, using the 'validate_only' parameter on the request executes pre-checks, but does not perform the full installation.
            """

            kwargs = {}
            changes = {}
            if query_action is not None:
                kwargs["action"] = query_action
            if query_elapsed_duration is not None:
                kwargs["elapsed_duration"] = query_elapsed_duration
            if query_estimated_duration is not None:
                kwargs["estimated_duration"] = query_estimated_duration
            if query_pending_version is not None:
                kwargs["pending_version"] = query_pending_version
            if query_state is not None:
                kwargs["state"] = query_state
            if query_version is not None:
                kwargs["version"] = query_version

            if action is not None:
                changes["action"] = action
            if elapsed_duration is not None:
                changes["elapsed_duration"] = elapsed_duration
            if estimated_duration is not None:
                changes["estimated_duration"] = estimated_duration
            if pending_version is not None:
                changes["pending_version"] = pending_version
            if state is not None:
                changes["state"] = state
            if version is not None:
                changes["version"] = version

            if hasattr(Software, "find"):
                resource = Software.find(
                    **kwargs
                )
            else:
                resource = Software()
            try:
                for key, value in changes.items():
                    setattr(resource, key, value)
                response = resource.patch(poll=False)
                await _wait_for_job(response)
                resource.get(fields=",".join(changes.keys()))
                return [resource]
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to modify Software: %s" % err)


    def upload(
        self,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Uploads a software or firmware package located on the local filesystem.
### Related ONTAP commands
* `cluster image package get`
### Learn more
* [`DOC /cluster/software`](#docs-cluster-cluster_software)
"""
        return super()._action(
            "upload", body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    upload.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._action.__doc__)

