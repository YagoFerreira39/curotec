from abc import ABC, abstractmethod

from src.use_cases.data_types.dtos.orders.order_dto import OrderDto
from src.use_cases.data_types.requests.orders.execute_order_request import (
    ExecuteOrderRequest,
)


class IExecuteOrderUseCase(ABC):
    @classmethod
    @abstractmethod
    async def execute_order(cls, request: ExecuteOrderRequest) -> OrderDto:
        pass
