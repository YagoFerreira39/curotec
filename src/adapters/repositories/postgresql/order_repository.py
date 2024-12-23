from decouple import config
from psycopg import AsyncCursor
from psycopg.rows import dict_row
from psycopg.sql import SQL
from src.adapters.repositories.exceptions.repository_exceptions import (
    FailToInsertInformationException,
    FailToRetrieveInformationException,
)
from witch_doctor import WitchDoctor

from src.adapters.ports.postgresql.i_postgresql_connection_pool import (
    IPostgresqlConnectionPool,
)
from src.adapters.ports.postgresql.i_postgresql_infrastructure import (
    IPostgresqlInfrastructure,
)
from src.domain.models.order_model import OrderModel
from src.externals.infrastructure.postgresql.exceptions.postgresql_base_infrastructure_exception import (
    PostgresqlBaseInfrastructureException,
)
from src.use_cases.ports.extensions.orders.i_order_extension import IOrderExtension
from src.use_cases.ports.repositories.postgresql.i_order_repository import (
    IOrderRepository,
)


class OrderRepository(IOrderRepository):

    __postgresql_infrastructure: IPostgresqlInfrastructure
    __postgresql_connection_pool: IPostgresqlConnectionPool
    __order_extension: IOrderExtension

    @WitchDoctor.injection
    def __init__(
        self,
        postgresql_infrastructure: IPostgresqlInfrastructure,
        order_extension: IOrderExtension,
    ):
        OrderRepository.__postgresql_infrastructure = postgresql_infrastructure
        OrderRepository.__postgresql_connection_pool = (
            OrderRepository.__postgresql_infrastructure.get_pool(
                uri=config("POSTGRESQL_STRING_CONNECTION"),
                database=config("POSTGRESQL_DATABASE"),
            )
        )
        OrderRepository.__order_extension = order_extension

    @classmethod
    async def insert_order(cls, model: OrderModel) -> None:
        try:
            async with cls.__postgresql_connection_pool.get_connection() as connection, connection.cursor() as cursor:
                cursor: AsyncCursor

                query = SQL(
                    obj="""
                    INSERT INTO commodity_orders
                    (user_id, commodity_name, order_amount, quantity, unit_price, created_at, updated_at)
                    VALUES(%(user_id)s, %(commodity_name)s, %(order_amount)s, %(quantity)s, %(unit_price)s, %(created_at)s, %(updated_at)s);
                    """
                )

                await cursor.execute(
                    query=query, params=model.to_insert(), prepare=True
                )

        except PostgresqlBaseInfrastructureException as original_exception:
            raise FailToInsertInformationException(
                message="Fail to insert order in database.",
                original_error=original_exception,
            ) from original_exception

        except Exception as original_exception:
            raise FailToInsertInformationException(
                message="Fail to insert order in database.",
                original_error=original_exception,
            ) from original_exception

    @classmethod
    async def get_orders_by_user_id(cls, user_id: int) -> list[OrderModel]:
        try:
            async with cls.__postgresql_connection_pool.get_connection() as connection, connection.cursor(
                row_factory=dict_row
            ) as cursor:
                cursor: AsyncCursor

                query = SQL(
                    obj="""
                        SELECT * FROM commodity_orders
                        WHERE user_id = %(user_id)s;
                    """
                )

                prepared_statement = await cursor.execute(
                    query=query,
                    params={"user_id": user_id},
                    prepare=True,
                )

                result_list = await prepared_statement.fetchall()
                if result_list:
                    model_list = (
                        cls.__order_extension.from_database_result_to_model_list(
                            result_list=result_list
                        )
                    )

                return model_list

        except PostgresqlBaseInfrastructureException as original_exception:
            raise FailToRetrieveInformationException(
                message="Fail to retrieve orders in database.",
                original_error=original_exception,
            ) from original_exception

        except Exception as original_exception:
            raise FailToRetrieveInformationException(
                message="Fail to retrieve orders in database.",
                original_error=original_exception,
            ) from original_exception
