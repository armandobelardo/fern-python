# This file was auto-generated by Fern from our API Definition.

import abc
import functools
import inspect
import logging
import typing

import fastapi

from ........core.abstract_fern_service import AbstractFernService
from ........core.exceptions.fern_http_exception import FernHTTPException
from ........core.route_args import get_route_args
from ..types.lightweight_problem_info_v_2 import LightweightProblemInfoV2
from ..types.problem_info_v_2 import ProblemInfoV2


class AbstractProblemService(AbstractFernService):
    """
    AbstractProblemService is an abstract class containing the methods that you should implement.

    Each method is associated with an API route, which will be registered
    with FastAPI when you register your implementation using Fern's register()
    function.
    """

    @abc.abstractmethod
    def get_lightweight_problems(self) -> typing.List[LightweightProblemInfoV2]:
        """
        Returns lightweight versions of all problems
        """
        ...

    @abc.abstractmethod
    def get_problems(self) -> typing.List[ProblemInfoV2]:
        """
        Returns latest versions of all problems
        """
        ...

    @abc.abstractmethod
    def get_latest_problem(self, *, problem_id: str) -> ProblemInfoV2:
        """
        Returns latest version of a problem
        """
        ...

    @abc.abstractmethod
    def get_problem_version(self, *, problem_id: str, problem_version: int) -> ProblemInfoV2:
        """
        Returns requested version of a problem
        """
        ...

    """
    Below are internal methods used by Fern to register your implementation.
    You can ignore them.
    """

    @classmethod
    def _init_fern(cls, router: fastapi.APIRouter) -> None:
        cls.__init_get_lightweight_problems(router=router)
        cls.__init_get_problems(router=router)
        cls.__init_get_latest_problem(router=router)
        cls.__init_get_problem_version(router=router)

    @classmethod
    def __init_get_lightweight_problems(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.get_lightweight_problems)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            else:
                new_parameters.append(parameter)
        setattr(cls.get_lightweight_problems, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.get_lightweight_problems)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> typing.List[LightweightProblemInfoV2]:
            try:
                return cls.get_lightweight_problems(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'get_lightweight_problems' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.get_lightweight_problems.__globals__)

        router.get(
            path="/problems-v2/lightweight-problem-info",
            response_model=typing.List[LightweightProblemInfoV2],
            description=AbstractProblemService.get_lightweight_problems.__doc__,
            **get_route_args(cls.get_lightweight_problems, default_tag="v_2.v_3.problem"),
        )(wrapper)

    @classmethod
    def __init_get_problems(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.get_problems)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            else:
                new_parameters.append(parameter)
        setattr(cls.get_problems, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.get_problems)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> typing.List[ProblemInfoV2]:
            try:
                return cls.get_problems(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'get_problems' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.get_problems.__globals__)

        router.get(
            path="/problems-v2/problem-info",
            response_model=typing.List[ProblemInfoV2],
            description=AbstractProblemService.get_problems.__doc__,
            **get_route_args(cls.get_problems, default_tag="v_2.v_3.problem"),
        )(wrapper)

    @classmethod
    def __init_get_latest_problem(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.get_latest_problem)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "problem_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls.get_latest_problem, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.get_latest_problem)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> ProblemInfoV2:
            try:
                return cls.get_latest_problem(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'get_latest_problem' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.get_latest_problem.__globals__)

        router.get(
            path="/problems-v2/problem-info/{problem_id}",
            response_model=ProblemInfoV2,
            description=AbstractProblemService.get_latest_problem.__doc__,
            **get_route_args(cls.get_latest_problem, default_tag="v_2.v_3.problem"),
        )(wrapper)

    @classmethod
    def __init_get_problem_version(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.get_problem_version)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "problem_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "problem_version":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls.get_problem_version, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.get_problem_version)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> ProblemInfoV2:
            try:
                return cls.get_problem_version(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'get_problem_version' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.get_problem_version.__globals__)

        router.get(
            path="/problems-v2/problem-info/{problem_id}/version/{problem_version}",
            response_model=ProblemInfoV2,
            description=AbstractProblemService.get_problem_version.__doc__,
            **get_route_args(cls.get_problem_version, default_tag="v_2.v_3.problem"),
        )(wrapper)
