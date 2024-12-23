from fastapi import APIRouter
from starlette.routing import Router

from src.adapters.controllers.order_controller import OrderController
from src.use_cases.data_types.responses.orders.execute_order_response import (
    ExecuteOrderResponse,
)
from src.use_cases.data_types.router_requests.orders.execute_order_router_request import (
    ExecuteOrderRouterRequest,
)


class OrderRouter(Router):
    __order_router = APIRouter(prefix="/order")

    @staticmethod
    def get_router() -> APIRouter:
        return OrderRouter.__order_router

    @staticmethod
    @__order_router.post(
        path="/",
        tags=["Orders"],
        response_model=ExecuteOrderResponse,
        response_model_exclude_none=True,
    )
    async def execute_order(
        router_request: ExecuteOrderRouterRequest,
    ) -> ExecuteOrderResponse:
        response = await OrderController.execute_order(router_request=router_request)

        return response
