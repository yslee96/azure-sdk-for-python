# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient

from .. import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import MySQLManagementClientConfiguration
from .operations import (
    AzureADAdministratorsOperations,
    BackupAndExportOperations,
    BackupsOperations,
    CheckNameAvailabilityOperations,
    CheckNameAvailabilityWithoutLocationOperations,
    CheckVirtualNetworkSubnetUsageOperations,
    ConfigurationsOperations,
    DatabasesOperations,
    FirewallRulesOperations,
    GetPrivateDnsZoneSuffixOperations,
    LocationBasedCapabilitiesOperations,
    LogFilesOperations,
    Operations,
    ReplicasOperations,
    ServersOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class MySQLManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """The Microsoft Azure management API provides create, read, update, and delete functionality for
    Azure MySQL resources including servers, databases, firewall rules, VNET rules, log files and
    configurations with new business model.

    :ivar azure_ad_administrators: AzureADAdministratorsOperations operations
    :vartype azure_ad_administrators:
     azure.mgmt.rdbms.mysql_flexibleservers.aio.operations.AzureADAdministratorsOperations
    :ivar backups: BackupsOperations operations
    :vartype backups: azure.mgmt.rdbms.mysql_flexibleservers.aio.operations.BackupsOperations
    :ivar backup_and_export: BackupAndExportOperations operations
    :vartype backup_and_export:
     azure.mgmt.rdbms.mysql_flexibleservers.aio.operations.BackupAndExportOperations
    :ivar configurations: ConfigurationsOperations operations
    :vartype configurations:
     azure.mgmt.rdbms.mysql_flexibleservers.aio.operations.ConfigurationsOperations
    :ivar databases: DatabasesOperations operations
    :vartype databases: azure.mgmt.rdbms.mysql_flexibleservers.aio.operations.DatabasesOperations
    :ivar firewall_rules: FirewallRulesOperations operations
    :vartype firewall_rules:
     azure.mgmt.rdbms.mysql_flexibleservers.aio.operations.FirewallRulesOperations
    :ivar servers: ServersOperations operations
    :vartype servers: azure.mgmt.rdbms.mysql_flexibleservers.aio.operations.ServersOperations
    :ivar replicas: ReplicasOperations operations
    :vartype replicas: azure.mgmt.rdbms.mysql_flexibleservers.aio.operations.ReplicasOperations
    :ivar log_files: LogFilesOperations operations
    :vartype log_files: azure.mgmt.rdbms.mysql_flexibleservers.aio.operations.LogFilesOperations
    :ivar location_based_capabilities: LocationBasedCapabilitiesOperations operations
    :vartype location_based_capabilities:
     azure.mgmt.rdbms.mysql_flexibleservers.aio.operations.LocationBasedCapabilitiesOperations
    :ivar check_virtual_network_subnet_usage: CheckVirtualNetworkSubnetUsageOperations operations
    :vartype check_virtual_network_subnet_usage:
     azure.mgmt.rdbms.mysql_flexibleservers.aio.operations.CheckVirtualNetworkSubnetUsageOperations
    :ivar check_name_availability: CheckNameAvailabilityOperations operations
    :vartype check_name_availability:
     azure.mgmt.rdbms.mysql_flexibleservers.aio.operations.CheckNameAvailabilityOperations
    :ivar check_name_availability_without_location: CheckNameAvailabilityWithoutLocationOperations
     operations
    :vartype check_name_availability_without_location:
     azure.mgmt.rdbms.mysql_flexibleservers.aio.operations.CheckNameAvailabilityWithoutLocationOperations
    :ivar get_private_dns_zone_suffix: GetPrivateDnsZoneSuffixOperations operations
    :vartype get_private_dns_zone_suffix:
     azure.mgmt.rdbms.mysql_flexibleservers.aio.operations.GetPrivateDnsZoneSuffixOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.rdbms.mysql_flexibleservers.aio.operations.Operations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = MySQLManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client: AsyncARMPipelineClient = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.azure_ad_administrators = AzureADAdministratorsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.backups = BackupsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.backup_and_export = BackupAndExportOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.configurations = ConfigurationsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.databases = DatabasesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.firewall_rules = FirewallRulesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.servers = ServersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.replicas = ReplicasOperations(self._client, self._config, self._serialize, self._deserialize)
        self.log_files = LogFilesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.location_based_capabilities = LocationBasedCapabilitiesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.check_virtual_network_subnet_usage = CheckVirtualNetworkSubnetUsageOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.check_name_availability = CheckNameAvailabilityOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.check_name_availability_without_location = CheckNameAvailabilityWithoutLocationOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.get_private_dns_zone_suffix = GetPrivateDnsZoneSuffixOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "MySQLManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
