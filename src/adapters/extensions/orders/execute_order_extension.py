from src.adapters.extensions.exceptions.extension_exceptions import (
    ExtensionUnexpectedException,
)

from src.domain.entities.order_entity import OrderEntity
from src.domain.models.order_model import OrderModel
from src.use_cases.data_types.dtos.orders.order_dto import OrderDto
from src.use_cases.data_types.requests.orders.execute_order_request import (
    ExecuteOrderRequest,
)
from src.use_cases.data_types.responses.orders.execute_order_response import (
    ExecuteOrderResponse,
)
from src.use_cases.data_types.responses.payloads.orders.execute_order_payload import (
    ExecuteOrderPayload,
)
from src.use_cases.data_types.router_requests.orders.execute_order_router_request import (
    ExecuteOrderRouterRequest,
)
from src.use_cases.ports.extensions.orders.i_execute_order_extension import (
    IExecuteOrderExtension,
)


class ExecuteOrderExtension(IExecuteOrderExtension):
    @staticmethod
    def from_router_request_to_request(
        router_request: ExecuteOrderRouterRequest,
    ) -> ExecuteOrderRequest:
        try:
            request = ExecuteOrderRequest(
                user_id=router_request.user_id,
                commodity_name=router_request.commodity_name,
                quantity=router_request.quantity,
            )

            return request

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_request_to_entity(
        request: ExecuteOrderRequest, unit_price: float, available_amount: float
    ) -> OrderEntity:
        try:
            entity = OrderEntity(
                user_id=request.user_id,
                commodity_name=request.commodity_name,
                quantity=request.quantity,
                unit_price=unit_price,
                available_amount=available_amount,
            )

            return entity

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_entity_to_model(entity: OrderEntity) -> OrderModel:
        try:
            model = OrderModel(
                order_id=entity.order_id,
                user_id=entity.user_id,
                commodity_name=entity.commodity_name,
                order_amount=entity.order_amount,
                quantity=entity.quantity,
                unit_price=entity.unit_price,
            )

            return model

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_dto_to_response(dto: OrderDto) -> ExecuteOrderResponse:
        try:
            payload = ExecuteOrderPayload(
                commodity_name=dto.commodity_name,
                unit_price=dto.unit_price,
                order_amount=dto.order_amount,
                quantity=dto.quantity,
                order_id=dto.order_id,
            )

            response = ExecuteOrderResponse(
                status=True, payload=payload, message="order executed"
            )

            return response

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception
