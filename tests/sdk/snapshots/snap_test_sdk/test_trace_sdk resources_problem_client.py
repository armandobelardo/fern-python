# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_headers import remove_none_from_headers
from ...environment import FernIrEnvironment
from ..commons.types.problem_id import ProblemId
from ..commons.types.variable_type import VariableType
from .types.create_problem_request import CreateProblemRequest
from .types.create_problem_response import CreateProblemResponse
from .types.get_default_starter_files_response import GetDefaultStarterFilesResponse
from .types.update_problem_response import UpdateProblemResponse
from .types.variable_type_and_name import VariableTypeAndName

# this is used as the default value for optional parameters
_ = typing.cast(typing.Any, ...)


class ProblemClient:
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

    def create_problem(self, *, request: CreateProblemRequest) -> CreateProblemResponse:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "problem-crud/create"),
            json=jsonable_encoder(request),
            headers=remove_none_from_headers(
                {
                    "X-Random-Header": self.x_random_header,
                    "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                }
            ),
            timeout=None,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CreateProblemResponse, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_problem(self, problem_id: ProblemId, *, request: CreateProblemRequest) -> UpdateProblemResponse:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", f"problem-crud/update/{problem_id}"),
            json=jsonable_encoder(request),
            headers=remove_none_from_headers(
                {
                    "X-Random-Header": self.x_random_header,
                    "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                }
            ),
            timeout=None,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UpdateProblemResponse, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_problem(self, problem_id: ProblemId) -> None:
        _response = httpx.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._environment.value}/", f"problem-crud/delete/{problem_id}"),
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

    def get_default_starter_files(
        self, *, input_params: typing.List[VariableTypeAndName], output_type: VariableType, method_name: str
    ) -> GetDefaultStarterFilesResponse:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "problem-crud/default-starter-files"),
            json=jsonable_encoder({"inputParams": input_params, "outputType": output_type, "methodName": method_name}),
            headers=remove_none_from_headers(
                {
                    "X-Random-Header": self.x_random_header,
                    "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                }
            ),
            timeout=None,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetDefaultStarterFilesResponse, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncProblemClient:
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

    async def create_problem(self, *, request: CreateProblemRequest) -> CreateProblemResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", "problem-crud/create"),
                json=jsonable_encoder(request),
                headers=remove_none_from_headers(
                    {
                        "X-Random-Header": self.x_random_header,
                        "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                    }
                ),
                timeout=None,
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CreateProblemResponse, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update_problem(self, problem_id: ProblemId, *, request: CreateProblemRequest) -> UpdateProblemResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", f"problem-crud/update/{problem_id}"),
                json=jsonable_encoder(request),
                headers=remove_none_from_headers(
                    {
                        "X-Random-Header": self.x_random_header,
                        "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                    }
                ),
                timeout=None,
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UpdateProblemResponse, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_problem(self, problem_id: ProblemId) -> None:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "DELETE",
                urllib.parse.urljoin(f"{self._environment.value}/", f"problem-crud/delete/{problem_id}"),
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

    async def get_default_starter_files(
        self, *, input_params: typing.List[VariableTypeAndName], output_type: VariableType, method_name: str
    ) -> GetDefaultStarterFilesResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", "problem-crud/default-starter-files"),
                json=jsonable_encoder(
                    {"inputParams": input_params, "outputType": output_type, "methodName": method_name}
                ),
                headers=remove_none_from_headers(
                    {
                        "X-Random-Header": self.x_random_header,
                        "Authorization": f"Bearer {self._token}" if self._token is not None else None,
                    }
                ),
                timeout=None,
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetDefaultStarterFilesResponse, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
