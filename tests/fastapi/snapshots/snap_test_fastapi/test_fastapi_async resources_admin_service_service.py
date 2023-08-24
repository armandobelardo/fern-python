# This file was auto-generated by Fern from our API Definition.

import abc
import functools
import inspect
import logging
import typing
import uuid

import fastapi
import starlette

from ....core.abstract_fern_service import AbstractFernService
from ....core.exceptions.fern_http_exception import FernHTTPException
from ....core.route_args import get_route_args
from ...submission.types.test_submission_status import TestSubmissionStatus
from ...submission.types.test_submission_update import TestSubmissionUpdate
from ...submission.types.trace_response_v_2 import TraceResponseV2
from ...submission.types.workspace_submission_status import WorkspaceSubmissionStatus
from ...submission.types.workspace_submission_update import WorkspaceSubmissionUpdate
from .store_traced_test_case_request import StoreTracedTestCaseRequest
from .store_traced_workspace_request import StoreTracedWorkspaceRequest


class AbstractAdminService(AbstractFernService):
    """
    AbstractAdminService is an abstract class containing the methods that you should implement.

    Each method is associated with an API route, which will be registered
    with FastAPI when you register your implementation using Fern's register()
    function.
    """

    @abc.abstractmethod
    async def update_test_submission_status(
        self, *, body: TestSubmissionStatus, submission_id: uuid.UUID, x_random_header: typing.Optional[str] = None
    ) -> None:
        ...

    @abc.abstractmethod
    async def send_test_submission_update(
        self, *, body: TestSubmissionUpdate, submission_id: uuid.UUID, x_random_header: typing.Optional[str] = None
    ) -> None:
        ...

    @abc.abstractmethod
    async def update_workspace_submission_status(
        self, *, body: WorkspaceSubmissionStatus, submission_id: uuid.UUID, x_random_header: typing.Optional[str] = None
    ) -> None:
        ...

    @abc.abstractmethod
    async def send_workspace_submission_update(
        self, *, body: WorkspaceSubmissionUpdate, submission_id: uuid.UUID, x_random_header: typing.Optional[str] = None
    ) -> None:
        ...

    @abc.abstractmethod
    async def store_traced_test_case(
        self,
        *,
        body: StoreTracedTestCaseRequest,
        submission_id: uuid.UUID,
        test_case_id: str,
        x_random_header: typing.Optional[str] = None,
    ) -> None:
        ...

    @abc.abstractmethod
    async def store_traced_test_case_v_2(
        self,
        *,
        body: typing.List[TraceResponseV2],
        submission_id: uuid.UUID,
        test_case_id: str,
        x_random_header: typing.Optional[str] = None,
    ) -> None:
        ...

    @abc.abstractmethod
    async def store_traced_workspace(
        self,
        *,
        body: StoreTracedWorkspaceRequest,
        submission_id: uuid.UUID,
        x_random_header: typing.Optional[str] = None,
    ) -> None:
        ...

    @abc.abstractmethod
    async def store_traced_workspace_v_2(
        self,
        *,
        body: typing.List[TraceResponseV2],
        submission_id: uuid.UUID,
        x_random_header: typing.Optional[str] = None,
    ) -> None:
        ...

    """
    Below are internal methods used by Fern to register your implementation.
    You can ignore them.
    """

    @classmethod
    def _init_fern(cls, router: fastapi.APIRouter) -> None:
        cls.__init_update_test_submission_status(router=router)
        cls.__init_send_test_submission_update(router=router)
        cls.__init_update_workspace_submission_status(router=router)
        cls.__init_send_workspace_submission_update(router=router)
        cls.__init_store_traced_test_case(router=router)
        cls.__init_store_traced_test_case_v_2(router=router)
        cls.__init_store_traced_workspace(router=router)
        cls.__init_store_traced_workspace_v_2(router=router)

    @classmethod
    def __init_update_test_submission_status(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.update_test_submission_status)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "submission_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "x_random_header":
                new_parameters.append(parameter.replace(default=fastapi.Header(default=None, alias="X-Random-Header")))
            else:
                new_parameters.append(parameter)
        setattr(
            cls.update_test_submission_status, "__signature__", endpoint_function.replace(parameters=new_parameters)
        )

        @functools.wraps(cls.update_test_submission_status)
        async def wrapper(*args: typing.Any, **kwargs: typing.Any) -> None:
            try:
                return await cls.update_test_submission_status(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'update_test_submission_status' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.update_test_submission_status.__globals__)

        router.post(
            path="/api/trace/admin/store-test-submission-status/{submission_id}",
            response_model=None,
            status_code=starlette.status.HTTP_204_NO_CONTENT,
            description=AbstractAdminService.update_test_submission_status.__doc__,
            **get_route_args(cls.update_test_submission_status, default_tag="admin"),
        )(wrapper)

    @classmethod
    def __init_send_test_submission_update(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.send_test_submission_update)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "submission_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "x_random_header":
                new_parameters.append(parameter.replace(default=fastapi.Header(default=None, alias="X-Random-Header")))
            else:
                new_parameters.append(parameter)
        setattr(cls.send_test_submission_update, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.send_test_submission_update)
        async def wrapper(*args: typing.Any, **kwargs: typing.Any) -> None:
            try:
                return await cls.send_test_submission_update(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'send_test_submission_update' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.send_test_submission_update.__globals__)

        router.post(
            path="/api/trace/admin/store-test-submission-status-v2/{submission_id}",
            response_model=None,
            status_code=starlette.status.HTTP_204_NO_CONTENT,
            description=AbstractAdminService.send_test_submission_update.__doc__,
            **get_route_args(cls.send_test_submission_update, default_tag="admin"),
        )(wrapper)

    @classmethod
    def __init_update_workspace_submission_status(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.update_workspace_submission_status)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "submission_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "x_random_header":
                new_parameters.append(parameter.replace(default=fastapi.Header(default=None, alias="X-Random-Header")))
            else:
                new_parameters.append(parameter)
        setattr(
            cls.update_workspace_submission_status,
            "__signature__",
            endpoint_function.replace(parameters=new_parameters),
        )

        @functools.wraps(cls.update_workspace_submission_status)
        async def wrapper(*args: typing.Any, **kwargs: typing.Any) -> None:
            try:
                return await cls.update_workspace_submission_status(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'update_workspace_submission_status' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.update_workspace_submission_status.__globals__)

        router.post(
            path="/api/trace/admin/store-workspace-submission-status/{submission_id}",
            response_model=None,
            status_code=starlette.status.HTTP_204_NO_CONTENT,
            description=AbstractAdminService.update_workspace_submission_status.__doc__,
            **get_route_args(cls.update_workspace_submission_status, default_tag="admin"),
        )(wrapper)

    @classmethod
    def __init_send_workspace_submission_update(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.send_workspace_submission_update)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "submission_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "x_random_header":
                new_parameters.append(parameter.replace(default=fastapi.Header(default=None, alias="X-Random-Header")))
            else:
                new_parameters.append(parameter)
        setattr(
            cls.send_workspace_submission_update, "__signature__", endpoint_function.replace(parameters=new_parameters)
        )

        @functools.wraps(cls.send_workspace_submission_update)
        async def wrapper(*args: typing.Any, **kwargs: typing.Any) -> None:
            try:
                return await cls.send_workspace_submission_update(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'send_workspace_submission_update' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.send_workspace_submission_update.__globals__)

        router.post(
            path="/api/trace/admin/store-workspace-submission-status-v2/{submission_id}",
            response_model=None,
            status_code=starlette.status.HTTP_204_NO_CONTENT,
            description=AbstractAdminService.send_workspace_submission_update.__doc__,
            **get_route_args(cls.send_workspace_submission_update, default_tag="admin"),
        )(wrapper)

    @classmethod
    def __init_store_traced_test_case(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.store_traced_test_case)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "submission_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "test_case_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "x_random_header":
                new_parameters.append(parameter.replace(default=fastapi.Header(default=None, alias="X-Random-Header")))
            else:
                new_parameters.append(parameter)
        setattr(cls.store_traced_test_case, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.store_traced_test_case)
        async def wrapper(*args: typing.Any, **kwargs: typing.Any) -> None:
            try:
                return await cls.store_traced_test_case(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'store_traced_test_case' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.store_traced_test_case.__globals__)

        router.post(
            path="/api/trace/admin/store-test-trace/submission/{submission_id}/testCase/{test_case_id}",
            response_model=None,
            status_code=starlette.status.HTTP_204_NO_CONTENT,
            description=AbstractAdminService.store_traced_test_case.__doc__,
            **get_route_args(cls.store_traced_test_case, default_tag="admin"),
        )(wrapper)

    @classmethod
    def __init_store_traced_test_case_v_2(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.store_traced_test_case_v_2)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "submission_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "test_case_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "x_random_header":
                new_parameters.append(parameter.replace(default=fastapi.Header(default=None, alias="X-Random-Header")))
            else:
                new_parameters.append(parameter)
        setattr(cls.store_traced_test_case_v_2, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.store_traced_test_case_v_2)
        async def wrapper(*args: typing.Any, **kwargs: typing.Any) -> None:
            try:
                return await cls.store_traced_test_case_v_2(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'store_traced_test_case_v_2' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.store_traced_test_case_v_2.__globals__)

        router.post(
            path="/api/trace/admin/store-test-trace-v2/submission/{submission_id}/testCase/{test_case_id}",
            response_model=None,
            status_code=starlette.status.HTTP_204_NO_CONTENT,
            description=AbstractAdminService.store_traced_test_case_v_2.__doc__,
            **get_route_args(cls.store_traced_test_case_v_2, default_tag="admin"),
        )(wrapper)

    @classmethod
    def __init_store_traced_workspace(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.store_traced_workspace)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "submission_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "x_random_header":
                new_parameters.append(parameter.replace(default=fastapi.Header(default=None, alias="X-Random-Header")))
            else:
                new_parameters.append(parameter)
        setattr(cls.store_traced_workspace, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.store_traced_workspace)
        async def wrapper(*args: typing.Any, **kwargs: typing.Any) -> None:
            try:
                return await cls.store_traced_workspace(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'store_traced_workspace' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.store_traced_workspace.__globals__)

        router.post(
            path="/api/trace/admin/store-workspace-trace/submission/{submission_id}",
            response_model=None,
            status_code=starlette.status.HTTP_204_NO_CONTENT,
            description=AbstractAdminService.store_traced_workspace.__doc__,
            **get_route_args(cls.store_traced_workspace, default_tag="admin"),
        )(wrapper)

    @classmethod
    def __init_store_traced_workspace_v_2(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.store_traced_workspace_v_2)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "submission_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "x_random_header":
                new_parameters.append(parameter.replace(default=fastapi.Header(default=None, alias="X-Random-Header")))
            else:
                new_parameters.append(parameter)
        setattr(cls.store_traced_workspace_v_2, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.store_traced_workspace_v_2)
        async def wrapper(*args: typing.Any, **kwargs: typing.Any) -> None:
            try:
                return await cls.store_traced_workspace_v_2(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'store_traced_workspace_v_2' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.store_traced_workspace_v_2.__globals__)

        router.post(
            path="/api/trace/admin/store-workspace-trace-v2/submission/{submission_id}",
            response_model=None,
            status_code=starlette.status.HTTP_204_NO_CONTENT,
            description=AbstractAdminService.store_traced_workspace_v_2.__doc__,
            **get_route_args(cls.store_traced_workspace_v_2, default_tag="admin"),
        )(wrapper)