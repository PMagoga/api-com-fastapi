from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import PedidoSchema
from dependencies import pegar_sessao
from models import Pedido

orders_router = APIRouter(prefix="/orders", tags=["orders"])

@orders_router.get("/", tags=["orders"])
async def pedidos():
    return {"message": "Você acessou a rota de pedidos"}

@orders_router.post("/pedido")
async def criar_pedido(pedido_schema: PedidoSchema, session: Session = Depends(pegar_sessao)):
    novo_pedido = Pedido(usuario=pedido_schema.usuario)
    session.add(novo_pedido)
    session.commit()
    return {"message": f"Pedido criado com sucesso {novo_pedido.id}"}