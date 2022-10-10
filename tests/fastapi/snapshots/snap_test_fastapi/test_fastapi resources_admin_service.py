import abc
import inspect
import typing

import fastapi

from ...core.abstract_fern_service import AbstractFernService
from ...core.route_args import get_route_args
from ..submission.types.submission_id import SubmissionId
from ..submission.types.test_submission_status import TestSubmissionStatus
from ..submission.types.test_submission_update import TestSubmissionUpdate
from ..submission.types.trace_response_v_2 import TraceResponseV2
from ..submission.types.workspace_submission_status import WorkspaceSubmissionStatus
from ..submission.types.workspace_submission_update import WorkspaceSubmissionUpdate
from ..v_2.problem.types.test_case_id import TestCaseId
from .types.store_traced_test_case_request import StoreTracedTestCaseRequest
from .types.store_traced_workspace_request import StoreTracedWorkspaceRequest


class AbstractAdminService(AbstractFernService):
    """
    AbstractAdminService is an abstract class containing the methods that your
    AdminService implementation should implement.

    Each method is associated with an API route, which will be registered
    with FastAPI when you register your implementation using Fern's register()
    function.
    """

    @abc.abstractmethod
    def update_test_submission_status(self, *, request: TestSubmissionStatus, submission_id: SubmissionId) -> None:
        ...

    @abc.abstractmethod
    def send_test_submission_update(self, *, request: TestSubmissionUpdate, submission_id: SubmissionId) -> None:
        ...

    @abc.abstractmethod
    def update_workspace_submission_status(
        self, *, request: WorkspaceSubmissionStatus, submission_id: SubmissionId
    ) -> None:
        ...

    @abc.abstractmethod
    def send_workspace_submission_update(
        self, *, request: WorkspaceSubmissionUpdate, submission_id: SubmissionId
    ) -> None:
        ...

    @abc.abstractmethod
    def store_traced_test_case(
        self, *, request: StoreTracedTestCaseRequest, submission_id: SubmissionId, test_case_id: str
    ) -> None:
        ...

    @abc.abstractmethod
    def store_traced_test_case_v_2(
        self, *, request: typing.List[TraceResponseV2], submission_id: SubmissionId, test_case_id: TestCaseId
    ) -> None:
        ...

    @abc.abstractmethod
    def store_traced_workspace(self, *, request: StoreTracedWorkspaceRequest, submission_id: SubmissionId) -> None:
        ...

    @abc.abstractmethod
    def store_traced_workspace_v_2(self, *, request: typing.List[TraceResponseV2], submission_id: SubmissionId) -> None:
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
            elif parameter_name == "request":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "submission_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls, "__signature__", endpoint_function.replace(parameters=new_parameters))

        cls.update_test_submission_status = router.post(  # type: ignore
            path="/admin/store-test-submission-status/{submission_id}",
            **get_route_args(cls.update_test_submission_status),
        )(cls.update_test_submission_status)

    @classmethod
    def __init_send_test_submission_update(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.send_test_submission_update)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "request":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "submission_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls, "__signature__", endpoint_function.replace(parameters=new_parameters))

        cls.send_test_submission_update = router.post(  # type: ignore
            path="/admin/store-test-submission-status-v2/{submission_id}",
            **get_route_args(cls.send_test_submission_update),
        )(cls.send_test_submission_update)

    @classmethod
    def __init_update_workspace_submission_status(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.update_workspace_submission_status)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "request":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "submission_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls, "__signature__", endpoint_function.replace(parameters=new_parameters))

        cls.update_workspace_submission_status = router.post(  # type: ignore
            path="/admin/store-workspace-submission-status/{submission_id}",
            **get_route_args(cls.update_workspace_submission_status),
        )(cls.update_workspace_submission_status)

    @classmethod
    def __init_send_workspace_submission_update(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.send_workspace_submission_update)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "request":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "submission_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls, "__signature__", endpoint_function.replace(parameters=new_parameters))

        cls.send_workspace_submission_update = router.post(  # type: ignore
            path="/admin/store-workspace-submission-status-v2/{submission_id}",
            **get_route_args(cls.send_workspace_submission_update),
        )(cls.send_workspace_submission_update)

    @classmethod
    def __init_store_traced_test_case(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.store_traced_test_case)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "request":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "submission_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "test_case_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls, "__signature__", endpoint_function.replace(parameters=new_parameters))

        cls.store_traced_test_case = router.post(  # type: ignore
            path="/admin/store-test-trace/submission/{submission_id}/testCase/{test_case_id}",
            **get_route_args(cls.store_traced_test_case),
        )(cls.store_traced_test_case)

    @classmethod
    def __init_store_traced_test_case_v_2(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.store_traced_test_case_v_2)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "request":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "submission_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "test_case_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls, "__signature__", endpoint_function.replace(parameters=new_parameters))

        cls.store_traced_test_case_v_2 = router.post(  # type: ignore
            path="/admin/store-test-trace-v2/submission/{submission_id}/testCase/{test_case_id}",
            **get_route_args(cls.store_traced_test_case_v_2),
        )(cls.store_traced_test_case_v_2)

    @classmethod
    def __init_store_traced_workspace(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.store_traced_workspace)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "request":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "submission_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls, "__signature__", endpoint_function.replace(parameters=new_parameters))

        cls.store_traced_workspace = router.post(  # type: ignore
            path="/admin/store-workspace-trace/submission/{submission_id}", **get_route_args(cls.store_traced_workspace)
        )(cls.store_traced_workspace)

    @classmethod
    def __init_store_traced_workspace_v_2(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.store_traced_workspace_v_2)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "request":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "submission_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            else:
                new_parameters.append(parameter)
        setattr(cls, "__signature__", endpoint_function.replace(parameters=new_parameters))

        cls.store_traced_workspace_v_2 = router.post(  # type: ignore
            path="/admin/store-workspace-trace-v2/submission/{submission_id}",
            **get_route_args(cls.store_traced_workspace_v_2),
        )(cls.store_traced_workspace_v_2)