from dataclasses import dataclass


from src.domain.enums.commodity_name_enum import CommodityNameEnum


@dataclass(slots=True)
class ExecuteOrderRouterRequest:
    user_id: int
    commodity_name: CommodityNameEnum
    quantity: int
