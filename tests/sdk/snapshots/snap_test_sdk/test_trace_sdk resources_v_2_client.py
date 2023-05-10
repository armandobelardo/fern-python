# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

import httpx
from backports.cached_property import cached_property

from ...core.api_error import ApiError
from ...core.remove_none_from_headers import remove_none_from_headers
from ...environment import FernIrEnvironment
from .resources.problem.client import AsyncProblemClient, ProblemClient
from .resources.v_3.client import AsyncV3Client, V3Client

# this is used as the default value for optional parameters
_ = typing.cast(typing.Any, ...)


class V2Client:
    def __init__(
        self,
        *,
        environment: FernIrEnvironment = FernIrEnvironment.PROD,
        x_random_header: typing.Optional[str] = None,
        token: typing.Optional[str] = None,
    ):
        self._environment = environment
        self.x_random_header = x_random_header
        self._token = token

    def test(self) -> None:
        _response = httpx.request(
            "GET",
            self._environment.value,
            headers=remove_none_from_headers(
                {
                    "X-Random-Header": self.x_random_header,
                    "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                }
            ),
            timeout=None,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    @cached_property
    def problem(self) -> ProblemClient:
        return ProblemClient(environment=self._environment, x_random_header=self.x_random_header, token=self._token)

    @cached_property
    def v_3(self) -> V3Client:
        return V3Client(environment=self._environment, x_random_header=self.x_random_header, token=self._token)


class AsyncV2Client:
    def __init__(
        self,
        *,
        environment: FernIrEnvironment = FernIrEnvironment.PROD,
        x_random_header: typing.Optional[str] = None,
        token: typing.Optional[str] = None,
    ):
        self._environment = environment
        self.x_random_header = x_random_header
        self._token = token

    async def test(self) -> None:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                self._environment.value,
                headers=remove_none_from_headers(
                    {
                        "X-Random-Header": self.x_random_header,
                        "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                    }
                ),
                timeout=None,
            )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    @cached_property
    def problem(self) -> AsyncProblemClient:
        return AsyncProblemClient(
            environment=self._environment, x_random_header=self.x_random_header, token=self._token
        )

    @cached_property
    def v_3(self) -> AsyncV3Client:
        return AsyncV3Client(environment=self._environment, x_random_header=self.x_random_header, token=self._token)
