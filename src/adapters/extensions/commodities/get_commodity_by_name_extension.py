from src.adapters.extensions.exceptions.extension_exceptions import (
    ExtensionUnexpectedException,
)

from src.use_cases.data_types.dtos.commodities.get_commodity_by_name_dto import (
    GetCommodityByNameDto,
)
from src.use_cases.data_types.requests.commodities.get_commodity_by_name_request import (
    GetCommodityByNameRequest,
)
from src.use_cases.data_types.responses.commodities.get_commodity_by_name_response import (
    GetCommodityByNameResponse,
)
from src.use_cases.data_types.responses.payloads.commodities.get_commodity_by_name_payload import (
    GetCommodityByNamePayload,
)
from src.use_cases.data_types.router_requests.commodities.get_commodity_by_name_router_request import (
    GetCommodityByNameRouterRequest,
)
from src.use_cases.data_types.services.responses.commodities.get_commodity_price_service_response import (
    GetCommodityPriceServiceResponse,
)
from src.use_cases.ports.extensions.commodities.i_get_commodity_by_name_extension import (
    IGetCommodityByNameExtension,
)


class GetCommodityByNameExtension(IGetCommodityByNameExtension):
    @staticmethod
    def from_router_request_to_request(
        router_request: GetCommodityByNameRouterRequest,
    ) -> GetCommodityByNameRequest:
        try:
            request = GetCommodityByNameRequest(
                commodity_name=router_request.commodity_name
            )

            return request

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_service_response_to_dto(
        service_response: GetCommodityPriceServiceResponse,
    ) -> GetCommodityByNameDto:
        try:
            dto = GetCommodityByNameDto(
                exchange=service_response.exchange,
                name=service_response.name,
                price=service_response.price,
                updated=service_response.updated,
            )

            return dto

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_dto_to_response(dto: GetCommodityByNameDto) -> GetCommodityByNameResponse:
        try:
            payload = GetCommodityByNamePayload(
                exchange=dto.exchange,
                name=dto.name,
                price=dto.price,
                updated=dto.updated,
            )

            response = GetCommodityByNameResponse(
                status=True,
                payload=payload,
            )

            return response

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception
