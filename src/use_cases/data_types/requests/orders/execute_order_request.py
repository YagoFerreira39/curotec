from dataclasses import dataclass

from fastapi import Query

from src.domain.enums.commodity_name_enum import CommodityNameEnum


@dataclass(slots=True)
class GetCommodityByNameRouterRequest:
    commodity_name: CommodityNameEnum = Query()
