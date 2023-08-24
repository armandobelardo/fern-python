# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from ..environment import FernIrEnvironment


class BaseClientWrapper:
    def __init__(self, *, environment: FernIrEnvironment):
        self._environment = environment

    def get_headers(self) -> typing.Dict[str, str]:
        headers: typing.Dict[str, str] = {"X-Fern-Language": "Python"}
        return headers

    def get_environment(self) -> FernIrEnvironment:
        return self._environment


class SyncClientWrapper(BaseClientWrapper):
    def __init__(self, *, environment: FernIrEnvironment, httpx_client: httpx.Client):
        super().__init__(environment=environment)
        self.httpx_client = httpx_client


class AsyncClientWrapper(BaseClientWrapper):
    def __init__(self, *, environment: FernIrEnvironment, httpx_client: httpx.AsyncClient):
        super().__init__(environment=environment)
        self.httpx_client = httpx_client