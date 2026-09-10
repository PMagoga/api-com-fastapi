from fastapi import APIRouter

orders_router = APIRouter(prefix="/orders", tags=["orders"])

@orders_router.get("/", tags=["orders"])
async def pedidos():
    return {"message": "Você acessou a rota de pedidos"}