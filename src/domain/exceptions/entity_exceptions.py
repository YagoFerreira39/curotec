from src.domain.exceptions.entity_base_exception import EntityBaseException
from src.domain.exceptions.entity_exceptions_reasons_enum import (
    EntityExceptionsReasonsEnum,
)


class UnableToExecuteOrderException(EntityBaseException):
    _reason = EntityExceptionsReasonsEnum.UNABLE_TO_EXECUTE_ORDER_ERROR
