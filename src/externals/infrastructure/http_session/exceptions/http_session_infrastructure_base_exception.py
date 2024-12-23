from src.domain.exceptions.track_base_exception import TrackBaseException
from src.externals.infrastructures.http_session.exceptions.http_session_infrastructure_exceptions_reasons_enum import (
    HttpSessionInfrastructureExceptionsReasonsEnum,
)


class HttpSessionInfrastructureBaseException(TrackBaseException):
    _reason = HttpSessionInfrastructureExceptionsReasonsEnum
