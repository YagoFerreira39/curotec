from src.adapters.extensions.exceptions.extension_exceptions import (
    ExtensionUnexpectedException,
)

from src.use_cases.data_types.services.responses.commodities.get_commodity_price_service_response import (
    GetCommodityPriceServiceResponse,
)
from src.use_cases.ports.extensions.services.i_commodities_service_extension import (
    ICommoditiesServiceExtension,
)


class CommoditiesServiceExtension(ICommoditiesServiceExtension):

    @staticmethod
    def from_service_result_to_response(
        service_result: dict,
    ) -> GetCommodityPriceServiceResponse:
        try:
            response = GetCommodityPriceServiceResponse(
                exchange=service_result.get("exchange"),
                name=service_result.get("name"),
                price=service_result.get("price"),
                updated=service_result.get("updated"),
            )

            return response

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception
