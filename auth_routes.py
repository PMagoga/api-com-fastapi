from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models import Usuario
from dependencies import pegar_sessao
from main import bcrypt_context
from schemas import LoginSchema, UsuarioSchema

auth_router = APIRouter(prefix="/auth", tags=["auth"])

def criar_token(id_usuario):
    token = f"sdafljkfknaskfja{id_usuario}"
    return token


@auth_router.get("/")
async def home():
    return {"mensagem": "Você precisa de autenticação", "autenticado": False}


@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema: UsuarioSchema, session: Session = Depends(pegar_sessao)):

    usuario = session.query(Usuario).filter(Usuario.email==usuario_schema.email).first()
    if usuario:
        # já existe um usuário
        return HTTPException(status_code=400, detail="Mensagem: Usuário já cadastrado")
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada,
                               usuario_schema.ativo, usuario_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return {"Mensagem": "Usuário cadastrado com sucesso"}

# login -> email + senha -> toke JWT
@auth_router.post("/login")
async def login(login_schema: LoginSchema, session: Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==login_schema.email).first()
    if usuario:
        raise HTTPException(status_code=400, detail="Usuário não cadastrado")
    else:
        access_token = criar_token(usuario.id)
        return {"access_token": access_token, "token_type": "bearer"}