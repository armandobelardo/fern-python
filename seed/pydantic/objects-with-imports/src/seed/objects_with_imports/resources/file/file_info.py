# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class FileInfo(str, enum.Enum):
    """
    from seed.objects_with_imports import FileInfo

    FileInfo.REGULAR
    """

    REGULAR = "REGULAR"
    """
    A regular file (e.g. foo.txt).
    """

    DIRECTORY = "DIRECTORY"
    """
    A directory (e.g. foo/).
    """

    def visit(self, regular: typing.Callable[[], T_Result], directory: typing.Callable[[], T_Result]) -> T_Result:
        if self is FileInfo.REGULAR:
            return regular()
        if self is FileInfo.DIRECTORY:
            return directory()
