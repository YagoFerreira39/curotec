from dataclasses import dataclass
import datetime


@dataclass(slots=True)
class OrderModel:
    user_id: int
    commodity_name: str
    order_amount: float
    quantity: int
    unit_price: float
    created_at: datetime = None
    updated_at: datetime = None
    order_id: str = None

    def __as_dict(self) -> dict:
        model_dict = {
            "user_id": self.user_id,
            "commodity_name": self.commodity_name,
            "order_amount": self.order_amount,
            "quantity": self.quantity,
            "unit_price": self.unit_price,
        }

        return model_dict

    def to_insert(self) -> dict:
        model_to_insert = self.__as_dict()
        model_to_insert["order_id"] = self.order_id
        model_to_insert["created_at"] = datetime.datetime.strftime(
            datetime.datetime.now(), "%Y-%m-%d %H:%M:%S"
        )
        model_to_insert["updated_at"] = datetime.datetime.strftime(
            datetime.datetime.now(), "%Y-%m-%d %H:%M:%S"
        )

        return model_to_insert
