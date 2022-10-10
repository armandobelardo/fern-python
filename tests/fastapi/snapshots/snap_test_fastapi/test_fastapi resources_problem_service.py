import abc
import inspect
import typing

import fastapi

from ...core.abstract_fern_service import AbstractFernService
from ...core.route_args import get_route_args
from ..commons.types.problem_id import ProblemId
from .types.create_problem_request import CreateProblemRequest
from .types.create_problem_response import CreateProblemResponse
from .types.get_default_starter_files_request import GetDefaultStarterFilesRequest
from .types.get_default_starter_files_response import GetDefaultStarterFilesResponse
from .types.update_problem_response import UpdateProblemResponse


class AbstractProblemCrudService(AbstractFernService):
    """
    AbstractProblemCrudService is an abstract class containing the methods that your
    ProblemCrudService implementation should implement.

    Each method is associated with an API route, which will be registered
    with FastAPI when you register your implementation using Fern's register()
    function.
    """

    @abc.abstractmethod
    def create_problem(self, *, request: CreateProblemRequest) -> CreateProblemResponse:
        ...

    @abc.abstractmethod
    def update_problem(self, *, request: CreateProblemRequest, problem_id: ProblemId) -> UpdateProblemResponse:
        ...

    @abc.abstractmethod
    def delete_problem(self, *, problem_id: ProblemId) -> None:
        ...

    @abc.abstractmethod
    def get_default_starter_files(self, *, request: GetDefaultStarterFilesRequest) -> GetDefaultStarterFilesResponse:
        ...

    """
    Below are internal methods used by Fern to register your implementation.
    You can ignore them.
    """

    @classmethod
    def _init_fern(cls, router: fastapi.APIRouter) -> None:
        cls.__init_create_problem(router=router)
        cls.__init_update_problem(router=router)
        cls.__init_delete_problem(router=router)
        cls.__init_get_default_starter_files(router=router)

    @classmethod
    def __init_create_problem(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.create_problem)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "request":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls, "__signature__", endpoint_function.replace(parameters=new_parameters))

        cls.create_problem = router.post(  # type: ignore
            path="/problem-crud/create", response_model=CreateProblemResponse, **get_route_args(cls.create_problem)
        )(cls.create_problem)

    @classmethod
    def __init_update_problem(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.update_problem)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "request":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "problem_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls, "__signature__", endpoint_function.replace(parameters=new_parameters))

        cls.update_problem = router.post(  # type: ignore
            path="/problem-crud/update/{problem_id}",
            response_model=UpdateProblemResponse,
            **get_route_args(cls.update_problem),
        )(cls.update_problem)

    @classmethod
    def __init_delete_problem(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.delete_problem)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "problem_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls, "__signature__", endpoint_function.replace(parameters=new_parameters))

        cls.delete_problem = router.delete(  # type: ignore
            path="/problem-crud/delete/{problem_id}", **get_route_args(cls.delete_problem)
        )(cls.delete_problem)

    @classmethod
    def __init_get_default_starter_files(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.get_default_starter_files)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "request":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls, "__signature__", endpoint_function.replace(parameters=new_parameters))

        cls.get_default_starter_files = router.post(  # type: ignore
            path="/problem-crud/default-starter-files",
            response_model=GetDefaultStarterFilesResponse,
            **get_route_args(cls.get_default_starter_files),
        )(cls.get_default_starter_files)