from src.use_cases.data_types.responses.base.base_api_response import BaseApiResponse

from src.use_cases.data_types import base_model_omit_none
from src.use_cases.data_types.responses.payloads.orders.execute_order_payload import (
    ExecuteOrderPayload,
)


@base_model_omit_none
class ExecuteOrderResponse(BaseApiResponse):
    payload: ExecuteOrderPayload = None
