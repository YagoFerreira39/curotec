from src.adapters.extensions.exceptions.extension_exceptions import (
    ExtensionUnexpectedException,
)
from src.domain.models.order_model import OrderModel
from src.use_cases.data_types.dtos.orders.order_dto import OrderDto
from src.use_cases.ports.extensions.orders.i_order_extension import IOrderExtension


class OrderExtension(IOrderExtension):

    @staticmethod
    def from_database_result_to_model(result: dict) -> OrderModel:
        try:
            model = OrderModel(
                user_id=result.get("user_id"),
                commodity_name=result.get("commodity_name"),
                unit_price=result.get("unit_price"),
                order_amount=result.get("order_amount"),
                quantity=result.get("quantity"),
                order_id=result.get("order_id"),
            )

            return model

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_database_result_to_model_list(result_list: list[dict]) -> list[OrderModel]:
        try:
            model_list = [
                OrderExtension.from_database_result_to_model(result=result)
                for result in result_list
            ]

            return model_list

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_model_to_dto(model: OrderModel) -> OrderDto:
        try:
            dto = OrderDto(
                commodity_name=model.commodity_name,
                unit_price=model.unit_price,
                order_amount=model.order_amount,
                quantity=model.quantity,
                order_id=model.order_id,
            )

            return dto

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception
