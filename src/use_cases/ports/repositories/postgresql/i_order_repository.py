from abc import ABC, abstractmethod

from src.domain.models.order_model import OrderModel


class IOrderRepository(ABC):
    @classmethod
    @abstractmethod
    async def insert_order(cls, model: OrderModel) -> None:
        pass

    @classmethod
    @abstractmethod
    async def get_orders_by_user_id(cls, user_id: int) -> list[OrderModel]:
        pass
