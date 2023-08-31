# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot
from snapshottest.file import FileSnapshot


snapshots = Snapshot()

snapshots['test_fastapi_file_upload __init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_file_upload __init__.py')

snapshots['test_fastapi_file_upload core___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_file_upload core___init__.py')

snapshots['test_fastapi_file_upload core_abstract_fern_service'] = FileSnapshot('snap_test_fastapi/test_fastapi_file_upload core_abstract_fern_service.py')

snapshots['test_fastapi_file_upload core_datetime_utils'] = FileSnapshot('snap_test_fastapi/test_fastapi_file_upload core_datetime_utils.py')

snapshots['test_fastapi_file_upload core_exceptions___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_file_upload core_exceptions___init__.py')

snapshots['test_fastapi_file_upload core_exceptions_fern_http_exception'] = FileSnapshot('snap_test_fastapi/test_fastapi_file_upload core_exceptions_fern_http_exception.py')

snapshots['test_fastapi_file_upload core_exceptions_handlers'] = FileSnapshot('snap_test_fastapi/test_fastapi_file_upload core_exceptions_handlers.py')

snapshots['test_fastapi_file_upload core_exceptions_unauthorized'] = FileSnapshot('snap_test_fastapi/test_fastapi_file_upload core_exceptions_unauthorized.py')

snapshots['test_fastapi_file_upload core_route_args'] = FileSnapshot('snap_test_fastapi/test_fastapi_file_upload core_route_args.py')

snapshots['test_fastapi_file_upload core_security___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_file_upload core_security___init__.py')

snapshots['test_fastapi_file_upload core_security_bearer'] = FileSnapshot('snap_test_fastapi/test_fastapi_file_upload core_security_bearer.py')

snapshots['test_fastapi_file_upload filepaths'] = [
    '__init__.py',
    'core/__init__.py',
    'core/abstract_fern_service.py',
    'core/datetime_utils.py',
    'core/exceptions/__init__.py',
    'core/exceptions/fern_http_exception.py',
    'core/exceptions/handlers.py',
    'core/exceptions/unauthorized.py',
    'core/route_args.py',
    'core/security/__init__.py',
    'core/security/bearer.py',
    'register.py',
    'resources/__init__.py',
    'resources/movie/__init__.py',
    'resources/movie/service/__init__.py',
    'resources/movie/service/service.py',
    'resources/movie/types/__init__.py',
    'resources/movie/types/movie_id.py'
]

snapshots['test_fastapi_file_upload register'] = FileSnapshot('snap_test_fastapi/test_fastapi_file_upload register.py')

snapshots['test_fastapi_file_upload resources___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_file_upload resources___init__.py')

snapshots['test_fastapi_file_upload resources_movie___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_file_upload resources_movie___init__.py')

snapshots['test_fastapi_file_upload resources_movie_service___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_file_upload resources_movie_service___init__.py')

snapshots['test_fastapi_file_upload resources_movie_service_service'] = FileSnapshot('snap_test_fastapi/test_fastapi_file_upload resources_movie_service_service.py')

snapshots['test_fastapi_file_upload resources_movie_types___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_file_upload resources_movie_types___init__.py')

snapshots['test_fastapi_file_upload resources_movie_types_movie_id'] = FileSnapshot('snap_test_fastapi/test_fastapi_file_upload resources_movie_types_movie_id.py')
