from contextlib import asynccontextmanager
from typing import AsyncIterator

from aiohttp import (
    ClientSession,
    InvalidURL,
    ServerTimeoutError,
    ClientOSError,
    TooManyRedirects,
)

from src.externals.infrastructure.http_config.exceptions.http_session_infrastructure_exceptions import (
    HttpSessionInfrastructureRuntimeErrorException,
    HttpSessionInfrastructureInvalidUrlErrorException,
    HttpSessionInfrastructureServerTimeoutErrorException,
    HttpSessionInfrastructureClientOSErrorException,
    HttpSessionInfrastructureTooManyRedirectsErrorException,
)
from src.externals.services.data_types.http_session.http_client_session_init_parameters import (
    HttpClientSessionInitParameters,
)
from src.externals.services.ports.i_http_session_infrastructure import (
    IHttpSessionInfrastructure,
)


class HttpSessionInfrastructure(IHttpSessionInfrastructure):
    @staticmethod
    @asynccontextmanager
    async def get_http_client_session(
        http_client_session_init_parameters: HttpClientSessionInitParameters,
    ) -> AsyncIterator[ClientSession]:
        session_parameters = http_client_session_init_parameters.as_dict()

        async with ClientSession(**session_parameters) as session:
            try:
                yield session

            except RuntimeError as original_exception:
                raise HttpSessionInfrastructureRuntimeErrorException(
                    message="Http session runtime error. See original exception.",
                    original_error=original_exception,
                ) from original_exception

            except InvalidURL as original_exception:
                raise HttpSessionInfrastructureInvalidUrlErrorException(
                    message="Http session invalid url error. See original exception.",
                    original_error=original_exception,
                ) from original_exception

            except ServerTimeoutError as original_exception:
                raise HttpSessionInfrastructureServerTimeoutErrorException(
                    message="Http session server timeout error. See original exception.",
                    original_error=original_exception,
                ) from original_exception

            except ClientOSError as original_exception:
                raise HttpSessionInfrastructureClientOSErrorException(
                    message="Http session client OS error. See original exception.",
                    original_error=original_exception,
                ) from original_exception

            except TooManyRedirects as original_exception:
                raise HttpSessionInfrastructureTooManyRedirectsErrorException(
                    message="Http session too many redirects error. See original exception.",
                    original_error=original_exception,
                ) from original_exception
