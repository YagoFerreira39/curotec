from abc import ABC, abstractmethod
from typing import AsyncIterator

from aiohttp import ClientSession

from src.externals.services.data_types.http_session.http_client_session_init_parameters import (
    HttpClientSessionInitParameters,
)


class IHttpSessionInfrastructure(ABC):
    @staticmethod
    @abstractmethod
    async def get_http_client_session(
        http_client_session_init_parameters: HttpClientSessionInitParameters,
    ) -> AsyncIterator[ClientSession]:
        pass
