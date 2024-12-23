from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ExecuteOrderPayload(BaseModel):
    name: Optional[str] = None
    unit_price: Optional[float] = None
    order_amount: Optional[float] = None
    quantity: Optional[int] = None
    order_id: Optional[str] = None
