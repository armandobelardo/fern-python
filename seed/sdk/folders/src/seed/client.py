# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

import httpx

from .a.client import AClient, AsyncAClient
from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .folder.client import AsyncFolderClient, FolderClient


class SeedApi:
    def __init__(
        self, *, base_url: str, timeout: typing.Optional[float] = 60, httpx_client: typing.Optional[httpx.Client] = None
    ):
        self._client_wrapper = SyncClientWrapper(
            base_url=base_url, httpx_client=httpx.Client(timeout=timeout) if httpx_client is None else httpx_client
        )
        self.a = AClient(client_wrapper=self._client_wrapper)
        self.folder = FolderClient(client_wrapper=self._client_wrapper)

    def foo(self) -> None:
        _response = self._client_wrapper.httpx_client.request(
            "POST", self._client_wrapper.get_base_url(), headers=self._client_wrapper.get_headers(), timeout=60
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncSeedApi:
    def __init__(
        self,
        *,
        base_url: str,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None
    ):
        self._client_wrapper = AsyncClientWrapper(
            base_url=base_url, httpx_client=httpx.AsyncClient(timeout=timeout) if httpx_client is None else httpx_client
        )
        self.a = AsyncAClient(client_wrapper=self._client_wrapper)
        self.folder = AsyncFolderClient(client_wrapper=self._client_wrapper)

    async def foo(self) -> None:
        _response = await self._client_wrapper.httpx_client.request(
            "POST", self._client_wrapper.get_base_url(), headers=self._client_wrapper.get_headers(), timeout=60
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
