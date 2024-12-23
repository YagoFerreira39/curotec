from abc import ABC, abstractmethod

from src.use_cases.data_types.dtos.commodities.get_commodity_by_name_dto import (
    GetCommodityByNameDto,
)
from src.use_cases.data_types.requests.commodities.get_commodity_by_name_request import (
    GetCommodityByNameRequest,
)
from src.use_cases.data_types.responses.commodities.get_commodity_by_name_response import (
    GetCommodityByNameResponse,
)
from src.use_cases.data_types.router_requests.commodities.get_commodity_by_name_router_request import (
    GetCommodityByNameRouterRequest,
)
from src.use_cases.data_types.services.responses.commodities.get_commodity_price_service_response import (
    GetCommodityPriceServiceResponse,
)


class IGetCommodityByNameExtension(ABC):
    @staticmethod
    @abstractmethod
    def from_router_request_to_request(
        router_request: GetCommodityByNameRouterRequest,
    ) -> GetCommodityByNameRequest:
        pass

    @staticmethod
    @abstractmethod
    def from_service_response_to_dto(
        service_response: GetCommodityPriceServiceResponse,
    ) -> GetCommodityByNameDto:
        pass

    @staticmethod
    @abstractmethod
    def from_dto_to_response(dto: GetCommodityByNameDto) -> GetCommodityByNameResponse:
        pass
