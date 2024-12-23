from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class GetCommodityByNameDto:
    exchange: str = None
    name: str = None
    price: float = None
    updated: float = None
