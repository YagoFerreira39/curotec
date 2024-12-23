from abc import ABC, abstractmethod

from src.use_cases.data_types.responses.orders.execute_order_response import (
    ExecuteOrderResponse,
)
from src.use_cases.data_types.router_requests.orders.execute_order_router_request import (
    ExecuteOrderRouterRequest,
)
from src.use_cases.ports.extensions.orders.i_execute_order_extension import (
    IExecuteOrderExtension,
)
from src.use_cases.ports.use_cases.orders.i_execute_order_use_case import (
    IExecuteOrderUseCase,
)


class IOrderController(ABC):
    @classmethod
    @abstractmethod
    async def execute_order(
        cls,
        router_request: ExecuteOrderRouterRequest,
        execute_order_extension: IExecuteOrderExtension,
        execute_order_use_case: IExecuteOrderUseCase,
    ) -> ExecuteOrderResponse:
        pass
