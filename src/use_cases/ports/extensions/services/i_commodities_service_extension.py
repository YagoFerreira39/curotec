from abc import ABC, abstractmethod

from src.use_cases.data_types.services.responses.commodities.get_commodity_price_service_response import (
    GetCommodityPriceServiceResponse,
)


class ICommoditiesServiceExtension(ABC):

    @staticmethod
    @abstractmethod
    def from_service_result_to_response(
        service_result: dict,
    ) -> GetCommodityPriceServiceResponse:
        pass
