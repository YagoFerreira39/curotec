from src.use_cases.data_types.responses.base.base_api_response import BaseApiResponse

from src.use_cases.data_types import base_model_omit_none
from src.use_cases.data_types.responses.payloads.commodities.get_commodity_by_name_payload import (
    GetCommodityByNamePayload,
)


@base_model_omit_none
class GetCommodityByNameResponse(BaseApiResponse):
    payload: GetCommodityByNamePayload = None
