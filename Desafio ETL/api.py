from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import json

app = FastAPI()


# Criando modelo de Dados para validação
class News(BaseModel):
    icon: str
    description: str


class UserUpdate(BaseModel):
    news: List[News]


# Função para Ler/ Escrever no JSON
DB_FILE = "db.json"


def load_db():
    with open(DB_FILE, "r") as f:
        return json.load(f)


def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)


@app.get("/users/{user_id}")
def get_user(user_id: int):
    """Rota de EXTRAÇÃO: Busca usuário pelo ID"""
    db = load_db()
    user = next((item for item in db if item["id"] == user_id), None)
    if user:
        return user
    raise HTTPException(status_code=404, detail="Usuário não encontrado")


@app.put("/users/{user_id}")
def update_user(user_id: int, user_update: UserUpdate):
    """Rota de CARGA: Atualiza news do usuário"""
    db = load_db()
    for user in db:
        if user["id"] == user_id:
            # Transforma os dados do Pyantic em dicionários e atualiza
            user["news"].extend([n.dict() for n in user_update.news])
            save_db(db)
            return user
    raise HTTPException(status_code=404, detail="Usuário não encontrado")


@app.get("/users")
def list_users():
    """Rota extra para ver todos"""
    return load_db()
