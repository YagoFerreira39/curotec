from dataclasses import dataclass

from src.domain.entities.value_objects.id_entity import IdEntity
from src.domain.exceptions.entity_exceptions import UnableToExecuteOrderException


@dataclass
class OrderEntity:
    __user_id: int
    __commodity_name: str
    __order_amount: float
    __quantity: int
    __unit_price: float
    __available_amount: float
    __order_id: IdEntity = None

    def __init__(
        self,
        user_id: int,
        commodity_name: str,
        quantity: int,
        unit_price: float,
        available_amount: float,
        order_id: IdEntity = None,
    ):
        self.__user_id = user_id
        self.__commodity_name = commodity_name
        self.__quantity = quantity
        self.__unit_price = unit_price
        self.__available_amount = available_amount
        self.__order_id = order_id if order_id else IdEntity.new_one()

        self.__create()

    @property
    def order_id(self) -> str:
        return self.__order_id.value

    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def commodity_name(self) -> str:
        return self.__commodity_name

    @property
    def order_amount(self) -> float:
        return self.__order_amount

    @property
    def quantity(self) -> int:
        return self.__quantity

    @property
    def unit_price(self) -> float:
        return self.__unit_price

    def __create(self) -> None:
        self.__calculate_order_amount()
        self.__validate_purchase_availability()

    def __calculate_order_amount(self) -> None:
        order_amount = float(self.__quantity * self.__unit_price)
        self.__order_amount = order_amount

    def __validate_purchase_availability(self) -> None:
        if float(self.__quantity * self.__unit_price) > self.__available_amount:
            raise UnableToExecuteOrderException(message="unable to execute order")
