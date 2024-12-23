from dataclasses import dataclass
from typing import Union

from aiohttp import BasicAuth
from aiohttp.typedefs import LooseCookies, LooseHeaders
from yarl import URL


@dataclass(slots=True)
class HttpClientSessionInitParameters:
    base_url: Union[URL, str] = None
    cookies: LooseCookies = None
    headers: LooseHeaders = None
    auth: BasicAuth = None

    def as_dict(self) -> dict:
        http_client_session_init_parameters = {
            "base_url": self.base_url,
            "cookies": self.cookies,
            "headers": self.headers,
            "auth": self.auth,
        }

        return http_client_session_init_parameters
