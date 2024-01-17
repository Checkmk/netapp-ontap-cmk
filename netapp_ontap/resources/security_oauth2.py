r"""
Copyright &copy; 2023 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

## Overview
This API is used to retrieve and delete the OAuth 2.0 configuration in the cluster. The GET request retrieves the OAuth 2.0 configuration. The DELETE request removes the OAuth 2.0 configuration.  Various responses are shown in the examples below.
<br />
---
## Examples
### Retrieving the OAuth 2.0 configuration in the cluster
The following output shows the OAuth 2.0 configuration in the cluster.
<br />
---
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import SecurityOauth2

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = SecurityOauth2(name="auth0")
    resource.get()
    print(resource)

```
<div class="try_it_out">
<input id="example0_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example0_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example0_result" class="try_it_out_content">
```
SecurityOauth2(
    {
        "client_id": "client_id",
        "jwks": {
            "provider_uri": "https://examplelab.customer.com/pf/JWKS",
            "refresh_interval": "PT1H",
        },
        "outgoing_proxy": "https://johndoe:secretpass@proxy.example.com:8080",
        "issuer": "https://examplelab.customer.com",
        "audience": "aud",
        "remote_user_claim": "user_claim",
        "introspection": {
            "interval": "PT1H",
            "endpoint_uri": "https://examplelab.customer.com/server/endpoint",
        },
        "hashed_client_secret": "a019c4d5f3815b50f5e9267d3ee80e8d8008308b83705c57206a1f5984dd0b26",
        "_links": {
            "self": {"href": "/api/security/authentication/cluster/oauth2/clients"}
        },
        "use_local_roles_if_present": False,
        "name": "auth0",
        "application": "http",
        "use_mutual_tls": "required",
    }
)

```
</div>
</div>

---
### Deleting the OAuth 2.0 configuration
---
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import SecurityOauth2

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = SecurityOauth2(name="auth0")
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


__all__ = ["SecurityOauth2", "SecurityOauth2Schema"]
__pdoc__ = {
    "SecurityOauth2Schema.resource": False,
    "SecurityOauth2Schema.opts": False,
    "SecurityOauth2.security_oauth2_show": False,
    "SecurityOauth2.security_oauth2_create": False,
    "SecurityOauth2.security_oauth2_modify": False,
    "SecurityOauth2.security_oauth2_delete": False,
}


class SecurityOauth2Schema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the SecurityOauth2 object"""

    links = marshmallow_fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE, allow_none=True)
    r""" The links field of the security_oauth2."""

    application = marshmallow_fields.Str(
        data_key="application",
        validate=enum_validation(['http']),
        allow_none=True,
    )
    r""" The name of the application using OAuth 2.0. Required for POST operations.

Valid choices:

* http"""

    audience = marshmallow_fields.Str(
        data_key="audience",
        allow_none=True,
    )
    r""" The OAuth 2.0 Audience."""

    client_id = marshmallow_fields.Str(
        data_key="client_id",
        allow_none=True,
    )
    r""" The OAuth 2.0 client ID. Required in POST operations for remote introspection."""

    client_secret = marshmallow_fields.Str(
        data_key="client_secret",
        allow_none=True,
    )
    r""" The OAuth 2.0 client secret. Required in POST operations for remote introspection."""

    hashed_client_secret = marshmallow_fields.Str(
        data_key="hashed_client_secret",
        allow_none=True,
    )
    r""" The OAuth 2.0 client secret as a SHA256 HMAC hashed value created with the cluster UUID as its HMAC secret key."""

    introspection = marshmallow_fields.Nested("netapp_ontap.models.security_oauth2_introspection.SecurityOauth2IntrospectionSchema", data_key="introspection", unknown=EXCLUDE, allow_none=True)
    r""" The introspection field of the security_oauth2."""

    issuer = marshmallow_fields.Str(
        data_key="issuer",
        allow_none=True,
    )
    r""" The OAuth 2.0 Issuer.

Example: https://examplelab.customer.com"""

    jwks = marshmallow_fields.Nested("netapp_ontap.models.security_oauth2_jwks.SecurityOauth2JwksSchema", data_key="jwks", unknown=EXCLUDE, allow_none=True)
    r""" The jwks field of the security_oauth2."""

    name = marshmallow_fields.Str(
        data_key="name",
        allow_none=True,
    )
    r""" The configuration name. Required for POST operations.

Example: auth0"""

    outgoing_proxy = marshmallow_fields.Str(
        data_key="outgoing_proxy",
        allow_none=True,
    )
    r""" Outgoing proxy to access external identity providers (IdPs). If not specified, no proxy is configured.

Example: https://johndoe:secretpass@proxy.example.com:8080"""

    remote_user_claim = marshmallow_fields.Str(
        data_key="remote_user_claim",
        allow_none=True,
    )
    r""" The remote user claim."""

    skip_uri_validation = marshmallow_fields.Boolean(
        data_key="skip_uri_validation",
        allow_none=True,
    )
    r""" Indicates whether or not to validate the input URIs. Default value is false."""

    use_local_roles_if_present = marshmallow_fields.Boolean(
        data_key="use_local_roles_if_present",
        allow_none=True,
    )
    r""" Indicates whether or not to use locally confgiured roles, if present. Default value is false."""

    use_mutual_tls = marshmallow_fields.Str(
        data_key="use_mutual_tls",
        validate=enum_validation(['none', 'request', 'required']),
        allow_none=True,
    )
    r""" OAuth 2.0 mutual TLS authentication setting. Set this value to \"none\" to disable mutual TLS authentication. Set this value to \"required\" to enforce mutual TLS authentication for all access tokens and reject any token that does not have x5t#S256 property in the cnf section. The default value is \"request\" which means mutual TLS authentication is enforced only if the x5t#S256 property is present in the cnf section of the access token.

Valid choices:

* none
* request
* required"""

    @property
    def resource(self):
        return SecurityOauth2

    gettable_fields = [
        "links",
        "application",
        "audience",
        "client_id",
        "hashed_client_secret",
        "introspection",
        "issuer",
        "jwks",
        "name",
        "outgoing_proxy",
        "remote_user_claim",
        "use_local_roles_if_present",
        "use_mutual_tls",
    ]
    """links,application,audience,client_id,hashed_client_secret,introspection,issuer,jwks,name,outgoing_proxy,remote_user_claim,use_local_roles_if_present,use_mutual_tls,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
        "application",
        "audience",
        "client_id",
        "client_secret",
        "introspection",
        "issuer",
        "jwks",
        "name",
        "outgoing_proxy",
        "remote_user_claim",
        "skip_uri_validation",
        "use_local_roles_if_present",
        "use_mutual_tls",
    ]
    """application,audience,client_id,client_secret,introspection,issuer,jwks,name,outgoing_proxy,remote_user_claim,skip_uri_validation,use_local_roles_if_present,use_mutual_tls,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in SecurityOauth2.get_collection(fields=field)]
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
            raise NetAppRestError("SecurityOauth2 modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class SecurityOauth2(Resource):
    """Allows interaction with SecurityOauth2 objects on the host"""

    _schema = SecurityOauth2Schema
    _path = "/api/security/authentication/cluster/oauth2/clients"
    _keys = ["name"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves all OAuth 2.0 configurations.
### Related ONTAP commands
* `security oauth2 client show`

### Learn more
* [`DOC /security/authentication/cluster/oauth2/clients`](#docs-security-security_authentication_cluster_oauth2_clients)"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="security oauth2 show")
        def security_oauth2_show(
            fields: List[Choices.define(["application", "audience", "client_id", "client_secret", "hashed_client_secret", "issuer", "name", "outgoing_proxy", "remote_user_claim", "skip_uri_validation", "use_local_roles_if_present", "use_mutual_tls", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of SecurityOauth2 resources

            Args:
                application: The name of the application using OAuth 2.0. Required for POST operations.
                audience: The OAuth 2.0 Audience.
                client_id: The OAuth 2.0 client ID. Required in POST operations for remote introspection.
                client_secret: The OAuth 2.0 client secret. Required in POST operations for remote introspection.
                hashed_client_secret: The OAuth 2.0 client secret as a SHA256 HMAC hashed value created with the cluster UUID as its HMAC secret key.
                issuer: The OAuth 2.0 Issuer.
                name: The configuration name. Required for POST operations.
                outgoing_proxy: Outgoing proxy to access external identity providers (IdPs). If not specified, no proxy is configured.
                remote_user_claim: The remote user claim.
                skip_uri_validation: Indicates whether or not to validate the input URIs. Default value is false.
                use_local_roles_if_present: Indicates whether or not to use locally confgiured roles, if present. Default value is false.
                use_mutual_tls: OAuth 2.0 mutual TLS authentication setting. Set this value to \\\"none\\\" to disable mutual TLS authentication. Set this value to \\\"required\\\" to enforce mutual TLS authentication for all access tokens and reject any token that does not have x5t#S256 property in the cnf section. The default value is \\\"request\\\" which means mutual TLS authentication is enforced only if the x5t#S256 property is present in the cnf section of the access token.
            """

            kwargs = {}
            if application is not None:
                kwargs["application"] = application
            if audience is not None:
                kwargs["audience"] = audience
            if client_id is not None:
                kwargs["client_id"] = client_id
            if client_secret is not None:
                kwargs["client_secret"] = client_secret
            if hashed_client_secret is not None:
                kwargs["hashed_client_secret"] = hashed_client_secret
            if issuer is not None:
                kwargs["issuer"] = issuer
            if name is not None:
                kwargs["name"] = name
            if outgoing_proxy is not None:
                kwargs["outgoing_proxy"] = outgoing_proxy
            if remote_user_claim is not None:
                kwargs["remote_user_claim"] = remote_user_claim
            if skip_uri_validation is not None:
                kwargs["skip_uri_validation"] = skip_uri_validation
            if use_local_roles_if_present is not None:
                kwargs["use_local_roles_if_present"] = use_local_roles_if_present
            if use_mutual_tls is not None:
                kwargs["use_mutual_tls"] = use_mutual_tls
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return SecurityOauth2.get_collection(
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all SecurityOauth2 resources that match the provided query"""
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
        """Returns a list of RawResources that represent SecurityOauth2 resources that match the provided query"""
        return super()._get_collection(
            *args, connection=connection, max_records=max_records, raw=True, **kwargs
        )

    fast_get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)


    @classmethod
    def post_collection(
        cls,
        records: Iterable["SecurityOauth2"],
        *args,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> Union[List["SecurityOauth2"], NetAppResponse]:
        r"""Creates the OAuth 2.0 configuration.
### Required properties
* `name`
* `application`
* `issuer`
### Optional properties
* `audience`
* `client_id`
* `client_secret`
* `introspection.endpoint_uri`
* `introspection.interval`
* `remote_user_claim`
* `jwks.provider_uri`
* `jwks.refresh_interval`
* `outgoing_proxy`
* `use_local_roles_if_present`
* `skip_uri_validation`
* `use_mutual_tls`
### Related ONTAP commands
* `security oauth2 client create`

### Learn more
* [`DOC /security/authentication/cluster/oauth2/clients`](#docs-security-security_authentication_cluster_oauth2_clients)"""
        return super()._post_collection(
            records, *args, hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    post_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post_collection.__doc__)

    @classmethod
    def delete_collection(
        cls,
        *args,
        records: Iterable["SecurityOauth2"] = None,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes the OAuth 2.0 configuration with the specified name.
### Required properties
    * `config_name`
### Related ONTAP commands
* `security oauth2 client delete`

### Learn more
* [`DOC /security/authentication/cluster/oauth2/clients/{name}`](#docs-security-security_authentication_cluster_oauth2_clients_{name})"""
        return super()._delete_collection(
            *args, body=body, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)

    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves all OAuth 2.0 configurations.
### Related ONTAP commands
* `security oauth2 client show`

### Learn more
* [`DOC /security/authentication/cluster/oauth2/clients`](#docs-security-security_authentication_cluster_oauth2_clients)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)

    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the OAuth 2.0 configuration with the specified name.
### Related ONTAP commands
* `security oauth2 client show`

### Learn more
* [`DOC /security/authentication/cluster/oauth2/clients/{name}`](#docs-security-security_authentication_cluster_oauth2_clients_{name})"""
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
        r"""Creates the OAuth 2.0 configuration.
### Required properties
* `name`
* `application`
* `issuer`
### Optional properties
* `audience`
* `client_id`
* `client_secret`
* `introspection.endpoint_uri`
* `introspection.interval`
* `remote_user_claim`
* `jwks.provider_uri`
* `jwks.refresh_interval`
* `outgoing_proxy`
* `use_local_roles_if_present`
* `skip_uri_validation`
* `use_mutual_tls`
### Related ONTAP commands
* `security oauth2 client create`

### Learn more
* [`DOC /security/authentication/cluster/oauth2/clients`](#docs-security-security_authentication_cluster_oauth2_clients)"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="security oauth2 create")
        async def security_oauth2_create(
        ) -> ResourceTable:
            """Create an instance of a SecurityOauth2 resource

            Args:
                links: 
                application: The name of the application using OAuth 2.0. Required for POST operations.
                audience: The OAuth 2.0 Audience.
                client_id: The OAuth 2.0 client ID. Required in POST operations for remote introspection.
                client_secret: The OAuth 2.0 client secret. Required in POST operations for remote introspection.
                hashed_client_secret: The OAuth 2.0 client secret as a SHA256 HMAC hashed value created with the cluster UUID as its HMAC secret key.
                introspection: 
                issuer: The OAuth 2.0 Issuer.
                jwks: 
                name: The configuration name. Required for POST operations.
                outgoing_proxy: Outgoing proxy to access external identity providers (IdPs). If not specified, no proxy is configured.
                remote_user_claim: The remote user claim.
                skip_uri_validation: Indicates whether or not to validate the input URIs. Default value is false.
                use_local_roles_if_present: Indicates whether or not to use locally confgiured roles, if present. Default value is false.
                use_mutual_tls: OAuth 2.0 mutual TLS authentication setting. Set this value to \\\"none\\\" to disable mutual TLS authentication. Set this value to \\\"required\\\" to enforce mutual TLS authentication for all access tokens and reject any token that does not have x5t#S256 property in the cnf section. The default value is \\\"request\\\" which means mutual TLS authentication is enforced only if the x5t#S256 property is present in the cnf section of the access token.
            """

            kwargs = {}
            if links is not None:
                kwargs["links"] = links
            if application is not None:
                kwargs["application"] = application
            if audience is not None:
                kwargs["audience"] = audience
            if client_id is not None:
                kwargs["client_id"] = client_id
            if client_secret is not None:
                kwargs["client_secret"] = client_secret
            if hashed_client_secret is not None:
                kwargs["hashed_client_secret"] = hashed_client_secret
            if introspection is not None:
                kwargs["introspection"] = introspection
            if issuer is not None:
                kwargs["issuer"] = issuer
            if jwks is not None:
                kwargs["jwks"] = jwks
            if name is not None:
                kwargs["name"] = name
            if outgoing_proxy is not None:
                kwargs["outgoing_proxy"] = outgoing_proxy
            if remote_user_claim is not None:
                kwargs["remote_user_claim"] = remote_user_claim
            if skip_uri_validation is not None:
                kwargs["skip_uri_validation"] = skip_uri_validation
            if use_local_roles_if_present is not None:
                kwargs["use_local_roles_if_present"] = use_local_roles_if_present
            if use_mutual_tls is not None:
                kwargs["use_mutual_tls"] = use_mutual_tls

            resource = SecurityOauth2(
                **kwargs
            )
            try:
                response = resource.post(hydrate=True, poll=False)
                await _wait_for_job(response)
                resource.get()
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to create SecurityOauth2: %s" % err)
            return [resource]


    def delete(
        self,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes the OAuth 2.0 configuration with the specified name.
### Required properties
    * `config_name`
### Related ONTAP commands
* `security oauth2 client delete`

### Learn more
* [`DOC /security/authentication/cluster/oauth2/clients/{name}`](#docs-security-security_authentication_cluster_oauth2_clients_{name})"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="security oauth2 delete")
        async def security_oauth2_delete(
        ) -> None:
            """Delete an instance of a SecurityOauth2 resource

            Args:
                application: The name of the application using OAuth 2.0. Required for POST operations.
                audience: The OAuth 2.0 Audience.
                client_id: The OAuth 2.0 client ID. Required in POST operations for remote introspection.
                client_secret: The OAuth 2.0 client secret. Required in POST operations for remote introspection.
                hashed_client_secret: The OAuth 2.0 client secret as a SHA256 HMAC hashed value created with the cluster UUID as its HMAC secret key.
                issuer: The OAuth 2.0 Issuer.
                name: The configuration name. Required for POST operations.
                outgoing_proxy: Outgoing proxy to access external identity providers (IdPs). If not specified, no proxy is configured.
                remote_user_claim: The remote user claim.
                skip_uri_validation: Indicates whether or not to validate the input URIs. Default value is false.
                use_local_roles_if_present: Indicates whether or not to use locally confgiured roles, if present. Default value is false.
                use_mutual_tls: OAuth 2.0 mutual TLS authentication setting. Set this value to \\\"none\\\" to disable mutual TLS authentication. Set this value to \\\"required\\\" to enforce mutual TLS authentication for all access tokens and reject any token that does not have x5t#S256 property in the cnf section. The default value is \\\"request\\\" which means mutual TLS authentication is enforced only if the x5t#S256 property is present in the cnf section of the access token.
            """

            kwargs = {}
            if application is not None:
                kwargs["application"] = application
            if audience is not None:
                kwargs["audience"] = audience
            if client_id is not None:
                kwargs["client_id"] = client_id
            if client_secret is not None:
                kwargs["client_secret"] = client_secret
            if hashed_client_secret is not None:
                kwargs["hashed_client_secret"] = hashed_client_secret
            if issuer is not None:
                kwargs["issuer"] = issuer
            if name is not None:
                kwargs["name"] = name
            if outgoing_proxy is not None:
                kwargs["outgoing_proxy"] = outgoing_proxy
            if remote_user_claim is not None:
                kwargs["remote_user_claim"] = remote_user_claim
            if skip_uri_validation is not None:
                kwargs["skip_uri_validation"] = skip_uri_validation
            if use_local_roles_if_present is not None:
                kwargs["use_local_roles_if_present"] = use_local_roles_if_present
            if use_mutual_tls is not None:
                kwargs["use_mutual_tls"] = use_mutual_tls

            if hasattr(SecurityOauth2, "find"):
                resource = SecurityOauth2.find(
                    **kwargs
                )
            else:
                resource = SecurityOauth2()
            try:
                response = resource.delete(poll=False)
                await _wait_for_job(response)
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to delete SecurityOauth2: %s" % err)


