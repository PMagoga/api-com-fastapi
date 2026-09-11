from fastapi import APIRouter
from sqlalchemy.orm import sessionmaker

from models import Usuario, db

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    return {"mensagem": "Você precisa de autenticação", "autenticado": False}


@auth_router.post("/criar_conta")
async def criar_conta(email: str, senha: str, nome: str):
    Session = sessionmaker(bind=db)
    session = Session()
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if usuario:
        # já existe um usuário
        return {"Mensagem": "Usuário já cadastrado"}
    else:
        novo_usuario = Usuario(nome, email, senha)
        session.add(novo_usuario)
        session.commit()
        return {"Mensagem": "Usuário cadastrado com sucesso"}