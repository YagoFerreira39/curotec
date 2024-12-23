from abc import ABC, abstractmethod

from src.use_cases.data_types.dtos.commodities.get_commodity_by_name_dto import (
    GetCommodityByNameDto,
)
from src.use_cases.data_types.requests.commodities.get_commodity_by_name_request import (
    GetCommodityByNameRequest,
)


class IGetCommodityByNameUseCase(ABC):
    @classmethod
    @abstractmethod
    async def get_commodity_by_name(
        cls, request: GetCommodityByNameRequest
    ) -> GetCommodityByNameDto:
        pass
