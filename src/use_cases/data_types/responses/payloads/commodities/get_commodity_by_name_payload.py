from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class GetCommodityByNamePayload(BaseModel):
    exchange: Optional[str] = None
    name: Optional[str] = None
    price: Optional[float] = None
    updated: Optional[float] = None
