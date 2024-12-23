from src.adapters.extensions.exceptions.extension_base_exception import (
    ExtensionBaseException,
)

from src.use_cases.exceptions.use_case_base_exception import UseCaseBaseException
from witch_doctor import WitchDoctor

from src.externals.services.exceptions.service_base_exception import (
    ServiceBaseException,
)
from src.use_cases.data_types.dtos.commodities.get_commodity_by_name_dto import (
    GetCommodityByNameDto,
)
from src.use_cases.data_types.requests.commodities.get_commodity_by_name_request import (
    GetCommodityByNameRequest,
)
from src.use_cases.data_types.services.responses.commodities.get_commodity_price_service_response import (
    GetCommodityPriceServiceResponse,
)
from src.use_cases.exceptions.use_case_exceptions import (
    UnableToRetrieveCommodityException,
    UnexpectedUseCaseException,
)
from src.use_cases.ports.extensions.commodities.i_get_commodity_by_name_extension import (
    IGetCommodityByNameExtension,
)
from src.use_cases.ports.services.i_commodities_service import ICommoditiesService
from src.use_cases.ports.use_cases.commodities.i_get_commodity_by_name_use_case import (
    IGetCommodityByNameUseCase,
)


class GetCommodityByNameUseCase(IGetCommodityByNameUseCase):
    __commodities_service: ICommoditiesService
    __get_commodity_by_name_extension: IGetCommodityByNameExtension

    @WitchDoctor.injection
    def __init__(
        self,
        commodities_service: ICommoditiesService,
        get_commodity_by_name_extension: IGetCommodityByNameExtension,
    ):
        GetCommodityByNameUseCase.__commodities_service = commodities_service
        GetCommodityByNameUseCase.__get_commodity_by_name_extension = (
            get_commodity_by_name_extension
        )

    @classmethod
    async def get_commodity_by_name(
        cls, request: GetCommodityByNameRequest
    ) -> GetCommodityByNameDto:
        try:
            commodity_service_response = await cls.__get_commodity(
                commodity_name=request.commodity_name
            )

            dto = cls.__create_dto(service_response=commodity_service_response)

            return dto

        except UseCaseBaseException as original_exception:
            raise original_exception

        except Exception as original_exception:
            raise UnexpectedUseCaseException(
                message="An unexpected error occurred.",
                original_error=original_exception,
            ) from original_exception

    @classmethod
    async def __get_commodity(
        cls, commodity_name: str
    ) -> GetCommodityPriceServiceResponse:
        try:
            commodity = await cls.__commodities_service.get_commodity_price_by_name(
                commodity_name=commodity_name
            )

            return commodity

        except ServiceBaseException as original_exception:
            raise UnableToRetrieveCommodityException(
                message="unable to retrieve commodity",
                original_error=original_exception,
            ) from original_exception

    @classmethod
    def __create_dto(
        cls, service_response: GetCommodityPriceServiceResponse
    ) -> GetCommodityByNameDto:
        try:
            dto = cls.__get_commodity_by_name_extension.from_service_response_to_dto(
                service_response=service_response
            )

            return dto

        except ExtensionBaseException as original_exception:
            raise UnableToRetrieveCommodityException(
                message="unable to retrieve commodity",
                original_error=original_exception,
            ) from original_exception
