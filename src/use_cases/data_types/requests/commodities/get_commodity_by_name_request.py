from dataclasses import dataclass


@dataclass(slots=True)
class GetCommodityByNameRequest:
    commodity_name: str
