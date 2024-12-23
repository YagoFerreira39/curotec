from abc import ABC, abstractmethod

from witch_doctor import WitchDoctor

from src.adapters.controllers import controller_error_handler

from src.adapters.ports.controllers.i_order_controller import IOrderController
from src.use_cases.data_types.responses.orders.execute_order_response import (
    ExecuteOrderResponse,
)
from src.use_cases.data_types.router_requests.orders.execute_order_router_request import (
    ExecuteOrderRouterRequest,
)
from src.use_cases.ports.extensions.orders.i_execute_order_extension import (
    IExecuteOrderExtension,
)
from src.use_cases.ports.use_cases.orders.i_execute_order_use_case import (
    IExecuteOrderUseCase,
)


class OrderController(IOrderController):
    @classmethod
    @controller_error_handler
    @WitchDoctor.injection
    async def execute_order(
        cls,
        router_request: ExecuteOrderRouterRequest,
        execute_order_extension: IExecuteOrderExtension,
        execute_order_use_case: IExecuteOrderUseCase,
    ) -> ExecuteOrderResponse:
        request = execute_order_extension.from_router_request_to_request(
            router_request=router_request
        )

        use_case_response = await execute_order_use_case.execute_order(request=request)

        response = execute_order_extension.from_dto_to_response(dto=use_case_response)

        return response
