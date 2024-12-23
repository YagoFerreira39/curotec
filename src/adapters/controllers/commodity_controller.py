from witch_doctor import WitchDoctor

from src.adapters.controllers import controller_error_handler

from src.adapters.ports.controllers.i_commodity_controller import ICommodityController
from src.use_cases.data_types.responses.commodities.get_commodity_by_name_response import (
    GetCommodityByNameResponse,
)
from src.use_cases.data_types.router_requests.commodities.get_commodity_by_name_router_request import (
    GetCommodityByNameRouterRequest,
)
from src.use_cases.ports.extensions.commodities.i_get_commodity_by_name_extension import (
    IGetCommodityByNameExtension,
)
from src.use_cases.ports.use_cases.commodities.i_get_commodity_by_name_use_case import (
    IGetCommodityByNameUseCase,
)


class CommodityController(ICommodityController):
    @classmethod
    @controller_error_handler
    @WitchDoctor.injection
    async def get_commodity_by_name(
        cls,
        router_request: GetCommodityByNameRouterRequest,
        get_commodity_by_name_extension: IGetCommodityByNameExtension,
        get_commodity_by_name_use_case: IGetCommodityByNameUseCase,
    ) -> GetCommodityByNameResponse:
        request = get_commodity_by_name_extension.from_router_request_to_request(
            router_request=router_request
        )

        use_case_response = await get_commodity_by_name_use_case.get_commodity_by_name(
            request=request
        )

        response = get_commodity_by_name_extension.from_dto_to_response(
            dto=use_case_response
        )

        return response
