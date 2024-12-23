from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class OrderDto:
    commodity_name: str = None
    unit_price: float = None
    order_amount: float = None
    quantity: int = None
    order_id: str = None
