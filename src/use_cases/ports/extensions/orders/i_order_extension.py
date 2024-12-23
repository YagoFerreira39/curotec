from abc import ABC, abstractmethod

from src.domain.models.order_model import OrderModel
from src.use_cases.data_types.dtos.orders.order_dto import OrderDto


class IOrderExtension(ABC):
    @staticmethod
    @abstractmethod
    def from_database_result_to_model(result: dict) -> OrderModel:
        pass

    @staticmethod
    @abstractmethod
    def from_database_result_to_model_list(result_list: list[dict]) -> list[OrderModel]:
        pass

    @staticmethod
    @abstractmethod
    def from_model_to_dto(model: OrderModel) -> OrderDto:
        pass
