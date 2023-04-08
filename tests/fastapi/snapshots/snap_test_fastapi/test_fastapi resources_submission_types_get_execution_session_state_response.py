# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .execution_session_state import ExecutionSessionState


class GetExecutionSessionStateResponse(pydantic.BaseModel):
    states: typing.Dict[str, ExecutionSessionState]
    num_warming_instances: typing.Optional[int] = pydantic.Field(alias="numWarmingInstances")
    warming_session_ids: typing.List[str] = pydantic.Field(alias="warmingSessionIds")

    class Partial(typing_extensions.TypedDict):
        states: typing_extensions.NotRequired[typing.Dict[str, ExecutionSessionState]]
        num_warming_instances: typing_extensions.NotRequired[typing.Optional[int]]
        warming_session_ids: typing_extensions.NotRequired[typing.List[str]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @GetExecutionSessionStateResponse.Validators.root()
            def validate(values: GetExecutionSessionStateResponse.Partial) -> GetExecutionSessionStateResponse.Partial:
                ...

            @GetExecutionSessionStateResponse.Validators.field("states")
            def validate_states(states: typing.Dict[str, ExecutionSessionState], values: GetExecutionSessionStateResponse.Partial) -> typing.Dict[str, ExecutionSessionState]:
                ...

            @GetExecutionSessionStateResponse.Validators.field("num_warming_instances")
            def validate_num_warming_instances(num_warming_instances: typing.Optional[int], values: GetExecutionSessionStateResponse.Partial) -> typing.Optional[int]:
                ...

            @GetExecutionSessionStateResponse.Validators.field("warming_session_ids")
            def validate_warming_session_ids(warming_session_ids: typing.List[str], values: GetExecutionSessionStateResponse.Partial) -> typing.List[str]:
                ...
        """

        _pre_validators: typing.ClassVar[
            typing.List[GetExecutionSessionStateResponse.Validators._PreRootValidator]
        ] = []
        _post_validators: typing.ClassVar[typing.List[GetExecutionSessionStateResponse.Validators._RootValidator]] = []
        _states_pre_validators: typing.ClassVar[
            typing.List[GetExecutionSessionStateResponse.Validators.PreStatesValidator]
        ] = []
        _states_post_validators: typing.ClassVar[
            typing.List[GetExecutionSessionStateResponse.Validators.StatesValidator]
        ] = []
        _num_warming_instances_pre_validators: typing.ClassVar[
            typing.List[GetExecutionSessionStateResponse.Validators.PreNumWarmingInstancesValidator]
        ] = []
        _num_warming_instances_post_validators: typing.ClassVar[
            typing.List[GetExecutionSessionStateResponse.Validators.NumWarmingInstancesValidator]
        ] = []
        _warming_session_ids_pre_validators: typing.ClassVar[
            typing.List[GetExecutionSessionStateResponse.Validators.PreWarmingSessionIdsValidator]
        ] = []
        _warming_session_ids_post_validators: typing.ClassVar[
            typing.List[GetExecutionSessionStateResponse.Validators.WarmingSessionIdsValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [GetExecutionSessionStateResponse.Validators._RootValidator],
            GetExecutionSessionStateResponse.Validators._RootValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [GetExecutionSessionStateResponse.Validators._PreRootValidator],
            GetExecutionSessionStateResponse.Validators._PreRootValidator,
        ]:
            ...

        @classmethod
        def root(cls, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["states"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [GetExecutionSessionStateResponse.Validators.PreStatesValidator],
            GetExecutionSessionStateResponse.Validators.PreStatesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["states"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [GetExecutionSessionStateResponse.Validators.StatesValidator],
            GetExecutionSessionStateResponse.Validators.StatesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["num_warming_instances"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [GetExecutionSessionStateResponse.Validators.PreNumWarmingInstancesValidator],
            GetExecutionSessionStateResponse.Validators.PreNumWarmingInstancesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["num_warming_instances"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [GetExecutionSessionStateResponse.Validators.NumWarmingInstancesValidator],
            GetExecutionSessionStateResponse.Validators.NumWarmingInstancesValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["warming_session_ids"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [GetExecutionSessionStateResponse.Validators.PreWarmingSessionIdsValidator],
            GetExecutionSessionStateResponse.Validators.PreWarmingSessionIdsValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["warming_session_ids"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [GetExecutionSessionStateResponse.Validators.WarmingSessionIdsValidator],
            GetExecutionSessionStateResponse.Validators.WarmingSessionIdsValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "states":
                    if pre:
                        cls._states_pre_validators.append(validator)
                    else:
                        cls._states_post_validators.append(validator)
                if field_name == "num_warming_instances":
                    if pre:
                        cls._num_warming_instances_pre_validators.append(validator)
                    else:
                        cls._num_warming_instances_post_validators.append(validator)
                if field_name == "warming_session_ids":
                    if pre:
                        cls._warming_session_ids_pre_validators.append(validator)
                    else:
                        cls._warming_session_ids_post_validators.append(validator)
                return validator

            return decorator

        class PreStatesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: GetExecutionSessionStateResponse.Partial) -> typing.Any:
                ...

        class StatesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Dict[str, ExecutionSessionState], __values: GetExecutionSessionStateResponse.Partial
            ) -> typing.Dict[str, ExecutionSessionState]:
                ...

        class PreNumWarmingInstancesValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: GetExecutionSessionStateResponse.Partial) -> typing.Any:
                ...

        class NumWarmingInstancesValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[int], __values: GetExecutionSessionStateResponse.Partial
            ) -> typing.Optional[int]:
                ...

        class PreWarmingSessionIdsValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: GetExecutionSessionStateResponse.Partial) -> typing.Any:
                ...

        class WarmingSessionIdsValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[str], __values: GetExecutionSessionStateResponse.Partial
            ) -> typing.List[str]:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(
                self, __values: GetExecutionSessionStateResponse.Partial
            ) -> GetExecutionSessionStateResponse.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(
        cls, values: GetExecutionSessionStateResponse.Partial
    ) -> GetExecutionSessionStateResponse.Partial:
        for validator in GetExecutionSessionStateResponse.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(
        cls, values: GetExecutionSessionStateResponse.Partial
    ) -> GetExecutionSessionStateResponse.Partial:
        for validator in GetExecutionSessionStateResponse.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("states", pre=True)
    def _pre_validate_states(
        cls, v: typing.Dict[str, ExecutionSessionState], values: GetExecutionSessionStateResponse.Partial
    ) -> typing.Dict[str, ExecutionSessionState]:
        for validator in GetExecutionSessionStateResponse.Validators._states_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("states", pre=False)
    def _post_validate_states(
        cls, v: typing.Dict[str, ExecutionSessionState], values: GetExecutionSessionStateResponse.Partial
    ) -> typing.Dict[str, ExecutionSessionState]:
        for validator in GetExecutionSessionStateResponse.Validators._states_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("num_warming_instances", pre=True)
    def _pre_validate_num_warming_instances(
        cls, v: typing.Optional[int], values: GetExecutionSessionStateResponse.Partial
    ) -> typing.Optional[int]:
        for validator in GetExecutionSessionStateResponse.Validators._num_warming_instances_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("num_warming_instances", pre=False)
    def _post_validate_num_warming_instances(
        cls, v: typing.Optional[int], values: GetExecutionSessionStateResponse.Partial
    ) -> typing.Optional[int]:
        for validator in GetExecutionSessionStateResponse.Validators._num_warming_instances_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("warming_session_ids", pre=True)
    def _pre_validate_warming_session_ids(
        cls, v: typing.List[str], values: GetExecutionSessionStateResponse.Partial
    ) -> typing.List[str]:
        for validator in GetExecutionSessionStateResponse.Validators._warming_session_ids_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("warming_session_ids", pre=False)
    def _post_validate_warming_session_ids(
        cls, v: typing.List[str], values: GetExecutionSessionStateResponse.Partial
    ) -> typing.List[str]:
        for validator in GetExecutionSessionStateResponse.Validators._warming_session_ids_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        orm_mode = True
        allow_population_by_field_name = True
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
