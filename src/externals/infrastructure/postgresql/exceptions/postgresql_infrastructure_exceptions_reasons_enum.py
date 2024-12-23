from enum import IntEnum


class PostgresqlInfrastructureExceptionsReasonsEnum(IntEnum):
    # PostgresqlInfrastructureExceptionsCodes 600-699

    INTERFACE_ERROR = 600
    DATABASE_ERROR = 601
    CONNECTION_TIMEOUT = 602
    UNEXPECTED_ERROR = 603
