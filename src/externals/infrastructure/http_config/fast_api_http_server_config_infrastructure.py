from decouple import config
from fastapi import FastAPI
from src.externals.ports.infrastructures.http_config.i_http_server_config_infrastructure import (
    IHttpServerConfigInfrastructure,
)
from starlette.middleware.cors import CORSMiddleware

from src.externals.routers.commodity_router import CommodityRouter
from src.externals.routers.order_router import OrderRouter


class FastApiHttpServerConfigInfrastructure(IHttpServerConfigInfrastructure):
    def __init__(self):
        self.__root = config("ROOT_PATH")
        self.__app = FastAPI(
            title="Curotec Test",
            description="",
            docs_url=self.__root + "/docs",
            openapi_url=self.__root + "/openapi.json",
        )

    def __register_cors_rules(self):
        cors_allowed_origins_str = config("CORS_ALLOWED_ORIGINS")
        cors_allowed_origins = cors_allowed_origins_str.split(",")
        self.__app.add_middleware(
            CORSMiddleware,
            allow_origins=cors_allowed_origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def __curotec_router(self):
        order_router = OrderRouter.get_router()
        commodity_router = CommodityRouter.get_router()

        self.__app.include_router(order_router, prefix=self.__root)
        self.__app.include_router(commodity_router, prefix=self.__root)

    def config_http_server(self) -> FastAPI:
        self.__register_cors_rules()
        self.__curotec_router()
        return self.__app
