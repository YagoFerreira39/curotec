from abc import ABC, abstractmethod

from src.use_cases.data_types.services.responses.commodities.get_commodity_price_service_response import (
    GetCommodityPriceServiceResponse,
)


class ICommoditiesService(ABC):
    @classmethod
    @abstractmethod
    async def get_commodity_price_by_name(
        cls, commodity_name: str
    ) -> GetCommodityPriceServiceResponse:
        pass
