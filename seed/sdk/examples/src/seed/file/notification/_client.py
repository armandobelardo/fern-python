# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .service._client import AsyncServiceClient, ServiceClient


class NotificationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.service = ServiceClient(client_wrapper=self._client_wrapper)


class AsyncNotificationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.service = AsyncServiceClient(client_wrapper=self._client_wrapper)
