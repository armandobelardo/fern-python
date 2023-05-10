# This file was auto-generated by Fern from our API Definition.

import typing

from backports.cached_property import cached_property

from .....environment import FernIrEnvironment
from .resources.problem.client import AsyncProblemClient, ProblemClient

# this is used as the default value for optional parameters
_ = typing.cast(typing.Any, ...)


class V3Client:
    def __init__(
        self,
        *,
        environment: FernIrEnvironment = FernIrEnvironment.PROD,
        x_random_header: typing.Optional[str] = None,
        token: typing.Optional[str] = None
    ):
        self._environment = environment
        self.x_random_header = x_random_header
        self._token = token

    @cached_property
    def problem(self) -> ProblemClient:
        return ProblemClient(environment=self._environment, x_random_header=self.x_random_header, token=self._token)


class AsyncV3Client:
    def __init__(
        self,
        *,
        environment: FernIrEnvironment = FernIrEnvironment.PROD,
        x_random_header: typing.Optional[str] = None,
        token: typing.Optional[str] = None
    ):
        self._environment = environment
        self.x_random_header = x_random_header
        self._token = token

    @cached_property
    def problem(self) -> AsyncProblemClient:
        return AsyncProblemClient(
            environment=self._environment, x_random_header=self.x_random_header, token=self._token
        )
