# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.datetime_utils import serialize_datetime
from ...core.jsonable_encoder import jsonable_encoder
from .errors.invalid_movie_error import InvalidMovieError
from .errors.movie_already_exists_error import MovieAlreadyExistsError
from .errors.movie_not_found_error import MovieNotFoundError
from .types.movie import Movie
from .types.movie_id import MovieId


class MovieClient:
    def __init__(self, *, environment: str):
        self._environment = environment

    def get_movie(self, movie_id: MovieId) -> Movie:
        _response = httpx.request(
            "GET", urllib.parse.urljoin(f"{self._environment}/", f"movie/movie/{movie_id}"), timeout=60
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Movie, _response_json)  # type: ignore
        if _response.status_code == 404:
            raise MovieNotFoundError(pydantic.parse_obj_as(MovieId, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_all_movies(self) -> typing.List[Movie]:
        _response = httpx.request("GET", urllib.parse.urljoin(f"{self._environment}/", "movie/all-movies"), timeout=60)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[Movie], _response_json)  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_movie(
        self,
        *,
        date: dt.date,
        datetime: dt.datetime,
        optional_date: typing.Optional[dt.date] = None,
        optional_datetime: typing.Optional[dt.datetime] = None,
        boolean: bool,
        optional_boolean: typing.Optional[bool] = None,
        request: Movie,
    ) -> None:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment}/", "movie/movie"),
            params={
                "date": str(date),
                "datetime": serialize_datetime(datetime),
                "optional_date": str(optional_date) if optional_date is not None else None,
                "optional_datetime": serialize_datetime(optional_datetime) if optional_datetime is not None else None,
                "boolean": boolean,
                "optional_boolean": optional_boolean,
            },
            json=jsonable_encoder(request),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 429:
            raise MovieAlreadyExistsError()
        if _response.status_code == 400:
            raise InvalidMovieError(pydantic.parse_obj_as(MovieId, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_movie(self, movie_id: MovieId) -> None:
        _response = httpx.request(
            "DELETE", urllib.parse.urljoin(f"{self._environment}/", f"movie/{movie_id}"), timeout=60
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 404:
            raise MovieNotFoundError(pydantic.parse_obj_as(MovieId, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncMovieClient:
    def __init__(self, *, environment: str):
        self._environment = environment

    async def get_movie(self, movie_id: MovieId) -> Movie:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET", urllib.parse.urljoin(f"{self._environment}/", f"movie/movie/{movie_id}"), timeout=60
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Movie, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise MovieNotFoundError(pydantic.parse_obj_as(MovieId, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_all_movies(self) -> typing.List[Movie]:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET", urllib.parse.urljoin(f"{self._environment}/", "movie/all-movies"), timeout=60
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[Movie], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_movie(
        self,
        *,
        date: dt.date,
        datetime: dt.datetime,
        optional_date: typing.Optional[dt.date] = None,
        optional_datetime: typing.Optional[dt.datetime] = None,
        boolean: bool,
        optional_boolean: typing.Optional[bool] = None,
        request: Movie,
    ) -> None:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment}/", "movie/movie"),
                params={
                    "date": str(date),
                    "datetime": serialize_datetime(datetime),
                    "optional_date": str(optional_date) if optional_date is not None else None,
                    "optional_datetime": serialize_datetime(optional_datetime)
                    if optional_datetime is not None
                    else None,
                    "boolean": boolean,
                    "optional_boolean": optional_boolean,
                },
                json=jsonable_encoder(request),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 429:
            raise MovieAlreadyExistsError()
        if _response.status_code == 400:
            raise InvalidMovieError(pydantic.parse_obj_as(MovieId, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_movie(self, movie_id: MovieId) -> None:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "DELETE", urllib.parse.urljoin(f"{self._environment}/", f"movie/{movie_id}"), timeout=60
            )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 404:
            raise MovieNotFoundError(pydantic.parse_obj_as(MovieId, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
