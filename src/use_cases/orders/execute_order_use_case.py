import random

from src.adapters.repositories.exceptions.repository_base_exception import (
    RepositoryBaseException,
)

from src.adapters.extensions.exceptions.extension_base_exception import (
    ExtensionBaseException,
)
from src.domain.entities.order_entity import OrderEntity

from src.domain.exceptions.entity_base_exception import EntityBaseException
from src.domain.models.order_model import OrderModel
from src.externals.services.exceptions.service_base_exception import (
    ServiceBaseException,
)
from src.use_cases.data_types.services.responses.commodities.get_commodity_price_service_response import (
    GetCommodityPriceServiceResponse,
)

from src.use_cases.exceptions.use_case_exceptions import (
    UnexpectedUseCaseException,
    MalformedRequestInputException,
    UnableToExecuteOrderException,
)

from src.use_cases.exceptions.use_case_base_exception import UseCaseBaseException
from witch_doctor import WitchDoctor

from src.use_cases.data_types.dtos.orders.order_dto import OrderDto
from src.use_cases.data_types.requests.orders.execute_order_request import (
    ExecuteOrderRequest,
)
from src.use_cases.ports.extensions.orders.i_execute_order_extension import (
    IExecuteOrderExtension,
)
from src.use_cases.ports.extensions.orders.i_order_extension import IOrderExtension
from src.use_cases.ports.repositories.postgresql.i_order_repository import (
    IOrderRepository,
)
from src.use_cases.ports.services.i_commodities_service import ICommoditiesService
from src.use_cases.ports.use_cases.orders.i_execute_order_use_case import (
    IExecuteOrderUseCase,
)


class ExecuteOrderUseCase(IExecuteOrderUseCase):
    __order_extension: IOrderExtension
    __execute_order_extension: IExecuteOrderExtension
    __order_repository: IOrderRepository
    __commodities_service: ICommoditiesService

    @WitchDoctor.injection
    def __init__(
        self,
        order_extension: IOrderExtension,
        execute_order_extension: IExecuteOrderExtension,
        order_repository: IOrderRepository,
        commodities_service: ICommoditiesService,
    ):
        ExecuteOrderUseCase.__order_extension = order_extension
        ExecuteOrderUseCase.__execute_order_extension = execute_order_extension
        ExecuteOrderUseCase.__order_repository = order_repository
        ExecuteOrderUseCase.__commodities_service = commodities_service

    @classmethod
    async def execute_order(cls, request: ExecuteOrderRequest) -> OrderDto:
        try:
            commodity = await cls.__get_commodity(commodity_name=request.commodity_name)
            available_amount = random.uniform(1000, 100000)

            order_entity = cls.__create_order_entity(
                request=request,
                unit_price=commodity.price,
                available_amount=available_amount,
            )

            order_model = cls.__create_order_model(entity=order_entity)

            await cls.__insert_order(model=order_model)

            order_dto = cls.__create_order_dto(model=order_model)

            return order_dto

        except UseCaseBaseException as original_exception:
            raise original_exception

        except Exception as original_exception:
            raise UnexpectedUseCaseException(
                message="An unexpected error occurred.",
                original_error=original_exception,
            ) from original_exception

    @classmethod
    async def __get_commodity(
        cls, commodity_name: str
    ) -> GetCommodityPriceServiceResponse:
        try:
            commodity = await cls.__commodities_service.get_commodity_price_by_name(
                commodity_name=commodity_name
            )

            return commodity

        except ServiceBaseException as original_exception:
            raise UnableToExecuteOrderException(
                message="unable to execute order",
                original_error=original_exception,
            ) from original_exception

    @classmethod
    def __create_order_entity(
        cls, request: ExecuteOrderRequest, unit_price: float, available_amount: float
    ) -> OrderEntity:
        try:
            entity = cls.__execute_order_extension.from_request_to_entity(
                request=request,
                unit_price=unit_price,
                available_amount=available_amount,
            )

            return entity

        except EntityBaseException as original_exception:
            raise MalformedRequestInputException(
                message=original_exception.message,
                original_error=original_exception.original_error,
            ) from original_exception
        except ExtensionBaseException as original_exception:
            raise UnableToExecuteOrderException(
                message="unable to execute order",
                original_error=original_exception.original_error,
            ) from original_exception

    @classmethod
    def __create_order_model(cls, entity: OrderEntity) -> OrderModel:
        try:
            model = cls.__execute_order_extension.from_entity_to_model(entity=entity)

            return model

        except ExtensionBaseException as original_exception:
            raise UnableToExecuteOrderException(
                message="unable to execute order",
                original_error=original_exception.original_error,
            ) from original_exception

    @classmethod
    async def __insert_order(cls, model: OrderModel) -> None:
        try:
            await cls.__order_repository.insert_order(model=model)

        except RepositoryBaseException as original_exception:
            raise UnableToExecuteOrderException(
                message="unable to execute order",
                original_error=original_exception.original_error,
            ) from original_exception

    @classmethod
    def __create_order_dto(cls, model: OrderModel) -> OrderDto:
        try:
            dto = cls.__order_extension.from_model_to_dto(model=model)

            return dto

        except ExtensionBaseException as original_exception:
            raise UnableToExecuteOrderException(
                message="order executed, but with errors",
                original_error=original_exception.original_error,
            ) from original_exception
