import asyncio

import loglifos
from fastapi import APIRouter
from starlette.routing import Router
from starlette.websockets import WebSocket, WebSocketDisconnect

from src.adapters.controllers.commodity_controller import CommodityController
from src.use_cases.data_types.router_requests.commodities.get_commodity_by_name_router_request import (
    GetCommodityByNameRouterRequest,
)


class CommodityRouter(Router):
    __commodity_router = APIRouter(prefix="/commodity")

    @staticmethod
    def get_router() -> APIRouter:
        return CommodityRouter.__commodity_router

    @staticmethod
    @__commodity_router.websocket(
        path="/ws",
    )
    async def get_commodity_by_name(websocket: WebSocket):
        await websocket.accept()
        try:
            current_request = None
            while True:
                try:
                    data = await asyncio.wait_for(websocket.receive_json(), timeout=5)
                    current_request = GetCommodityByNameRouterRequest(**data)
                except asyncio.TimeoutError:
                    loglifos.info("WebSocket disconnected")

                if current_request:
                    try:
                        response = await CommodityController.get_commodity_by_name(
                            router_request=current_request
                        )
                        await websocket.send_json(response.dict())
                    except Exception as exception:
                        loglifos.error("an error occurred", exception=exception)
                        await websocket.send_json(
                            {"status": "error", "message": "an error occurred"}
                        )

        except WebSocketDisconnect:
            loglifos.info("WebSocket disconnected")
        except Exception as exception:
            loglifos.error("an error occurred", exception=exception)
            await websocket.send_json(
                {"status": "error", "message": "an error occurred"}
            )
