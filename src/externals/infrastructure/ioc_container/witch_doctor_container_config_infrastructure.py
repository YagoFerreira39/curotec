from src.adapters.extensions.commodities.get_commodity_by_name_extension import (
    GetCommodityByNameExtension,
)
from src.adapters.extensions.services.commodities_service_extension import (
    CommoditiesServiceExtension,
)
from src.externals.infrastructure.http_session.http_session_infrastructure import (
    HttpSessionInfrastructure,
)
from src.adapters.extensions.orders.execute_order_extension import ExecuteOrderExtension
from src.adapters.extensions.orders.order_extension import OrderExtension
from src.adapters.repositories.postgresql.order_repository import OrderRepository
from src.externals.infrastructure.logs.loglifos_config_infrastructure import (
    LoglifosConfigInfrastructure,
)
from src.externals.ports.infrastructures.logs_config.i_logs_config_infrastructure import (
    ILogsConfigInfrastructure,
)

from src.adapters.ports.postgresql.i_postgresql_infrastructure import (
    IPostgresqlInfrastructure,
)
from src.externals.infrastructure.postgresql.postgresql_infrastructure import (
    PostgresqlInfrastructure,
)
from src.externals.ports.infrastructures.ioc_container.i_ioc_container import (
    IIocContainerConfigInfrastructure,
)
from witch_doctor import WitchDoctor, InjectionType

from src.externals.services.commodities_service import CommoditiesService
from src.externals.services.ports.i_http_session_infrastructure import (
    IHttpSessionInfrastructure,
)
from src.use_cases.commodities.get_commodity_by_name_use_case import (
    GetCommodityByNameUseCase,
)
from src.use_cases.orders.execute_order_use_case import ExecuteOrderUseCase
from src.use_cases.ports.extensions.commodities.i_get_commodity_by_name_extension import (
    IGetCommodityByNameExtension,
)
from src.use_cases.ports.extensions.orders.i_execute_order_extension import (
    IExecuteOrderExtension,
)
from src.use_cases.ports.extensions.orders.i_order_extension import IOrderExtension
from src.use_cases.ports.extensions.services.i_commodities_service_extension import (
    ICommoditiesServiceExtension,
)
from src.use_cases.ports.repositories.postgresql.i_order_repository import (
    IOrderRepository,
)
from src.use_cases.ports.services.i_commodities_service import ICommoditiesService
from src.use_cases.ports.use_cases.commodities.i_get_commodity_by_name_use_case import (
    IGetCommodityByNameUseCase,
)
from src.use_cases.ports.use_cases.orders.i_execute_order_use_case import (
    IExecuteOrderUseCase,
)


class WitchDoctorContainerConfigInfrastructure(IIocContainerConfigInfrastructure):
    @classmethod
    def __create_use_cases_container(cls):
        use_cases_container = WitchDoctor.container("use_cases")

        use_cases_container(
            IExecuteOrderUseCase, ExecuteOrderUseCase, InjectionType.SINGLETON
        )
        use_cases_container(
            IGetCommodityByNameUseCase,
            GetCommodityByNameUseCase,
            InjectionType.SINGLETON,
        )

        return use_cases_container

    @classmethod
    def __create_infrastructures_container(cls):
        infrastructures_container = WitchDoctor.container("infrastructures")

        infrastructures_container(
            IPostgresqlInfrastructure, PostgresqlInfrastructure, InjectionType.SINGLETON
        )
        infrastructures_container(
            ILogsConfigInfrastructure,
            LoglifosConfigInfrastructure,
            InjectionType.SINGLETON,
        )

        infrastructures_container(
            IHttpSessionInfrastructure,
            HttpSessionInfrastructure,
            InjectionType.SINGLETON,
        )

        return infrastructures_container

    @classmethod
    def __create_services_container(cls):
        services_container = WitchDoctor.container("services")

        services_container(
            ICommoditiesService, CommoditiesService, InjectionType.SINGLETON
        )

        return services_container

    @classmethod
    def __create_repositories_container(cls):
        repositories_container = WitchDoctor.container("repositories")

        repositories_container(
            IOrderRepository, OrderRepository, InjectionType.SINGLETON
        )

        return repositories_container

    @classmethod
    def __create_extensions_container(cls):
        extensions_container = WitchDoctor.container("extensions")

        extensions_container(IOrderExtension, OrderExtension, InjectionType.SINGLETON)
        extensions_container(
            IExecuteOrderExtension, ExecuteOrderExtension, InjectionType.SINGLETON
        )
        extensions_container(
            ICommoditiesServiceExtension,
            CommoditiesServiceExtension,
            InjectionType.SINGLETON,
        )
        extensions_container(
            IGetCommodityByNameExtension,
            GetCommodityByNameExtension,
            InjectionType.SINGLETON,
        )

        return extensions_container

    @classmethod
    def __create_containers(cls):
        cls.__create_use_cases_container()
        cls.__create_infrastructures_container()
        cls.__create_services_container()
        cls.__create_repositories_container()
        cls.__create_extensions_container()

    @classmethod
    def __load_containers(cls):
        WitchDoctor.load_container("use_cases")
        WitchDoctor.load_container("infrastructures")
        WitchDoctor.load_container("services")
        WitchDoctor.load_container("repositories")
        WitchDoctor.load_container("extensions")

    @classmethod
    def build_ioc_container(cls):
        cls.__create_containers()
        cls.__load_containers()
