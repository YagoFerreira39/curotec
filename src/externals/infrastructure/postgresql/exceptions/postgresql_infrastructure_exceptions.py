


from src.externals.infrastructure.postgresql.exceptions.postgresql_base_infrastructure_exception import PostgresqlBaseInfrastructureException
from src.externals.infrastructure.postgresql.exceptions.postgresql_infrastructure_exceptions_reasons_enum import PostgresqlInfrastructureExceptionsReasonsEnum


class PostgresqlInfrastructureInterfaceErrorException(
    PostgresqlBaseInfrastructureException
):
    _reason = PostgresqlInfrastructureExceptionsReasonsEnum.INTERFACE_ERROR


class PostgresqlInfrastructureDatabaseErrorException(
    PostgresqlBaseInfrastructureException
):
    _reason = PostgresqlInfrastructureExceptionsReasonsEnum.DATABASE_ERROR


class PostgresqlInfrastructureConnectionTimeoutException(
    PostgresqlBaseInfrastructureException
):
    _reason = PostgresqlInfrastructureExceptionsReasonsEnum.CONNECTION_TIMEOUT


class PostgresqlInfrastructureUnexpectedErrorException(
    PostgresqlBaseInfrastructureException
):
    _reason = PostgresqlInfrastructureExceptionsReasonsEnum.UNEXPECTED_ERROR
