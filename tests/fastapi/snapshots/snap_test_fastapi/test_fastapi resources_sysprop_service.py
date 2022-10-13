# This file was auto-generated by Fern from our API Definition.

# flake8: noqa
# fmt: off
# isort: skip_file

import abc
import functools
import inspect
import logging
import typing

import fastapi

from ...core.abstract_fern_service import AbstractFernService
from ...core.exceptions.fern_http_exception import FernHTTPException
from ...core.route_args import get_route_args
from ..commons.types.language import Language


class AbstractSysPropCrudService(AbstractFernService):
    """
    AbstractSysPropCrudService is an abstract class containing the methods that your
    SysPropCrudService implementation should implement.

    Each method is associated with an API route, which will be registered
    with FastAPI when you register your implementation using Fern's register()
    function.
    """

    @abc.abstractmethod
    def set_num_warm_instances(self, *, language: Language, num_warm_instances: int) -> None:
        ...

    @abc.abstractmethod
    def get_num_warm_instances(self) -> typing.Dict[Language, int]:
        ...

    """
    Below are internal methods used by Fern to register your implementation.
    You can ignore them.
    """

    @classmethod
    def _init_fern(cls, router: fastapi.APIRouter) -> None:
        cls.__init_set_num_warm_instances(router=router)
        cls.__init_get_num_warm_instances(router=router)

    @classmethod
    def __init_set_num_warm_instances(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.set_num_warm_instances)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "language":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "num_warm_instances":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls.set_num_warm_instances, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.set_num_warm_instances)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> None:
            try:
                return cls.set_num_warm_instances(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(__name__).warn(
                    f"Endpoint 'set_num_warm_instances' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.set_num_warm_instances.__globals__)

        router.put(
            path="/sysprop/num-warm-instances/{language}/{num_warm_instances}",
            **get_route_args(cls.set_num_warm_instances),
        )(wrapper)

    @classmethod
    def __init_get_num_warm_instances(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.get_num_warm_instances)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            else:
                new_parameters.append(parameter)
        setattr(cls.get_num_warm_instances, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.get_num_warm_instances)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> typing.Dict[Language, int]:
            try:
                return cls.get_num_warm_instances(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(__name__).warn(
                    f"Endpoint 'get_num_warm_instances' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.get_num_warm_instances.__globals__)

        router.get(
            path="/sysprop/num-warm-instances",
            response_model=typing.Dict[Language, int],
            **get_route_args(cls.get_num_warm_instances),
        )(wrapper)
