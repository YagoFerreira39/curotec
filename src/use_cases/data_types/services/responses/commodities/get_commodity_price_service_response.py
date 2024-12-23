from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class GetCommodityPriceServiceResponse:
    exchange: str
    name: str
    price: float
    updated: float
