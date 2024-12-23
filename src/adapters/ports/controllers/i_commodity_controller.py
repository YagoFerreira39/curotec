from abc import ABC, abstractmethod

from src.use_cases.data_types.responses.orders.execute_order_response import (
    ExecuteOrderResponse,
)
from src.use_cases.data_types.router_requests.commodities.get_commodity_by_name_router_request import (
    GetCommodityByNameRouterRequest,
)
from src.use_cases.ports.extensions.commodities.i_get_commodity_by_name_extension import (
    IGetCommodityByNameExtension,
)
from src.use_cases.ports.use_cases.commodities.i_get_commodity_by_name_use_case import (
    IGetCommodityByNameUseCase,
)


class ICommodityController(ABC):
    @classmethod
    @abstractmethod
    async def get_commodity_by_name(
        cls,
        router_request: GetCommodityByNameRouterRequest,
        get_commodity_by_name_extension: IGetCommodityByNameExtension,
        get_commodity_by_name_use_case: IGetCommodityByNameUseCase,
    ) -> ExecuteOrderResponse:
        pass
