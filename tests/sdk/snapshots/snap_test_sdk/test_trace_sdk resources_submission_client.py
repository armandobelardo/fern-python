# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.remove_none_from_headers import remove_none_from_headers
from ...environment import FernIrEnvironment
from ..commons.types.language import Language
from .types.execution_session_response import ExecutionSessionResponse
from .types.get_execution_session_state_response import GetExecutionSessionStateResponse


class SubmissionClient:
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

    def create_execution_session(self, language: Language) -> ExecutionSessionResponse:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", f"sessions/create-session/{language}"),
            headers=remove_none_from_headers(
                {
                    "X-Random-Header": self.x_random_header,
                    "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                }
            ),
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ExecutionSessionResponse, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_execution_session(self, session_id: str) -> typing.Optional[ExecutionSessionResponse]:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"sessions/{session_id}"),
            headers=remove_none_from_headers(
                {
                    "X-Random-Header": self.x_random_header,
                    "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                }
            ),
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Optional[ExecutionSessionResponse], _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def stop_execution_session(self, session_id: str) -> None:
        _response = httpx.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._environment.value}/", f"sessions/stop/{session_id}"),
            headers=remove_none_from_headers(
                {
                    "X-Random-Header": self.x_random_header,
                    "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                }
            ),
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_execution_sessions_state(self) -> GetExecutionSessionStateResponse:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "sessions/execution-sessions-state"),
            headers=remove_none_from_headers(
                {
                    "X-Random-Header": self.x_random_header,
                    "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                }
            ),
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetExecutionSessionStateResponse, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncSubmissionClient:
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

    async def create_execution_session(self, language: Language) -> ExecutionSessionResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", f"sessions/create-session/{language}"),
                headers=remove_none_from_headers(
                    {
                        "X-Random-Header": self.x_random_header,
                        "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                    }
                ),
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ExecutionSessionResponse, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_execution_session(self, session_id: str) -> typing.Optional[ExecutionSessionResponse]:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", f"sessions/{session_id}"),
                headers=remove_none_from_headers(
                    {
                        "X-Random-Header": self.x_random_header,
                        "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                    }
                ),
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Optional[ExecutionSessionResponse], _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def stop_execution_session(self, session_id: str) -> None:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "DELETE",
                urllib.parse.urljoin(f"{self._environment.value}/", f"sessions/stop/{session_id}"),
                headers=remove_none_from_headers(
                    {
                        "X-Random-Header": self.x_random_header,
                        "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                    }
                ),
            )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_execution_sessions_state(self) -> GetExecutionSessionStateResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", "sessions/execution-sessions-state"),
                headers=remove_none_from_headers(
                    {
                        "X-Random-Header": self.x_random_header,
                        "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                    }
                ),
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetExecutionSessionStateResponse, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)