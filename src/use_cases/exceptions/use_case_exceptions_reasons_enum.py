from enum import IntEnum


class UseCaseExceptionsReasonsEnum(IntEnum):
    # UseCaseExceptionsCodes  100-199
    UNEXPECTED_EXCEPTION_ERROR = 100
    MALFORMED_REQUEST_INPUT_ERROR = 101
    UNABLE_TO_EXECUTE_ORDER_ERROR = 102
    UNABLE_TO_RETRIEVE_COMMODITY_ERROR = 103
