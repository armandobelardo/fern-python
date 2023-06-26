from fern_python.codegen.source_file import SourceFile
from ..context.sdk_generator_context import SdkGeneratorContext


class ClientWrapper:
    BASE_CLIENT_WRAPPER_CLASS_NAME = "BaseClientWrapper"
    SYNC_CLIENT_WRAPPER_CLASS_NAME = "SyncClientWrapper"
    ASYNC_CLIENT_WRAPPER_CLASS_NAME = "AsyncClientWrapper"

    GET_HEADERS_METHOD_NAME = "get_headers"
    
    HTTPX_CLIENT_MEMBER_NAME = "httpx_client"

    def __init__(
        self,
        *,
        context: SdkGeneratorContext,
    ):
        self._context = context

    def generate(self, source_file: SourceFile) -> None:
        # class_declaration = self._create_class_declaration(is_async=False)
        # source_file.add_class_declaration(
        #     declaration=class_declaration,
        #     should_export=False,
        # )
        # source_file.add_class_declaration(
        #     declaration=self._create_class_declaration(is_async=True),
        #     should_export=False,
        # )
        pass
    
    def _create_base_client_wrapper_class_declaration() -> None:
        pass

    def _create_sync_client_wrapper_class_declaration() -> None:
        pass

    def _create_async_client_wrapper_class_declaration() -> None:
        pass
