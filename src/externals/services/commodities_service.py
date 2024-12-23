from http import HTTPStatus

from aiohttp import ClientSession
from decouple import config
from src.adapters.extensions.exceptions.extension_base_exception import (
    ExtensionBaseException,
)
from witch_doctor import WitchDoctor

from src.externals.infrastructure.http_config.exceptions.http_session_infrastructure_base_exception import (
    HttpSessionInfrastructureBaseException,
)
from src.externals.services.data_types.http_session.http_client_session_init_parameters import (
    HttpClientSessionInitParameters,
)
from src.externals.services.exceptions.service_exceptions import (
    HttpServiceException,
    ServiceUnexpectedException,
)
from src.externals.services.ports.i_http_session_infrastructure import (
    IHttpSessionInfrastructure,
)
from src.use_cases.data_types.services.responses.commodities.get_commodity_price_service_response import (
    GetCommodityPriceServiceResponse,
)
from src.use_cases.ports.extensions.services.i_commodities_service_extension import (
    ICommoditiesServiceExtension,
)
from src.use_cases.ports.services.i_commodities_service import ICommoditiesService


class CommoditiesService(ICommoditiesService):
    __http_session_infrastructure: IHttpSessionInfrastructure
    __commodities_service_extension: ICommoditiesServiceExtension

    @WitchDoctor.injection
    def __init__(
        self,
        http_session_infrastructure: IHttpSessionInfrastructure,
        commodities_service_extension: ICommoditiesServiceExtension,
    ):
        CommoditiesService.__http_session_infrastructure = http_session_infrastructure
        CommoditiesService.__commodities_service_extension = (
            commodities_service_extension
        )

    @classmethod
    async def get_commodity_price_by_name(
        cls, commodity_name: str
    ) -> GetCommodityPriceServiceResponse:
        try:
            http_session_parameters = HttpClientSessionInitParameters(
                base_url=config("COMMODITIES_SERVICE_URI"),
                headers={
                    "X-Api-Key": config("SERVICE_API_KEY"),
                    "Content-Type": "application/json",
                },
            )

            async with cls.__http_session_infrastructure.get_http_client_session(
                http_client_session_init_parameters=http_session_parameters
            ) as http_client_session:
                http_client_session: ClientSession
                url = config("GET_COMMODITY_PRICE_URL")

                async with http_client_session.get(
                    url=url, params={"name": commodity_name}
                ) as result:
                    if result.status == HTTPStatus.OK:
                        json_result = await result.json(content_type=None)
                        service_response = cls.__commodities_service_extension.from_service_result_to_response(
                            service_result=json_result
                        )

                    return service_response

        except HttpSessionInfrastructureBaseException as original_exception:
            raise HttpServiceException(
                message=original_exception.message,
                original_error=original_exception.original_error,
            ) from original_exception
        except ExtensionBaseException as original_exception:
            raise ServiceUnexpectedException(
                message=original_exception.message,
                original_error=original_exception,
            ) from original_exception
        except Exception as original_exception:
            raise ServiceUnexpectedException(
                message="Unexpected service exception",
                original_error=original_exception,
            ) from original_exception
