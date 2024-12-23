from abc import ABC, abstractmethod

from src.domain.entities.order_entity import OrderEntity
from src.domain.models.order_model import OrderModel
from src.use_cases.data_types.dtos.orders.order_dto import OrderDto
from src.use_cases.data_types.requests.orders.execute_order_request import (
    ExecuteOrderRequest,
)
from src.use_cases.data_types.responses.orders.execute_order_response import (
    ExecuteOrderResponse,
)
from src.use_cases.data_types.router_requests.orders.execute_order_router_request import (
    ExecuteOrderRouterRequest,
)


class IExecuteOrderExtension(ABC):
    @staticmethod
    @abstractmethod
    def from_router_request_to_request(
        router_request: ExecuteOrderRouterRequest,
    ) -> ExecuteOrderRequest:
        pass

    @staticmethod
    @abstractmethod
    def from_request_to_entity(
        request: ExecuteOrderRequest, unit_price: float, available_amount: float
    ) -> OrderEntity:
        pass

    @staticmethod
    @abstractmethod
    def from_entity_to_model(entity: OrderEntity) -> OrderModel:
        pass

    @staticmethod
    @abstractmethod
    def from_dto_to_response(dto: OrderDto) -> ExecuteOrderResponse:
        pass
