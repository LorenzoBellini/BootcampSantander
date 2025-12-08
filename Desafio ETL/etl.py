import requests
import json

# URL da API Local
API_URL = "http://127.0.0.1:8000"


def extract_user(user_id):
    response = requests.get(f"{API_URL}/users/{user_id}")
    if response.status_code == 200:
        return response.json()
    return None


def transform_user(user):
    "Simulaçao de mensagem gerada por IA para não gastar créditos"
    nome = user["name"]
    fake_ai_message = f"Olá {nome}, invista em renda fixa hoje!"

    # Adicionar mensagem na estrutura de news
    new_news = {
        "icon": "💡",
        "description": fake_ai_message
    }
    user['news'].append(new_news)
    return user


def load_user(user):
    # Prepara o payload apenas com o campo que a API espera para atualização
    payload = {"news": user["news"]}

    response = requests.put(f"{ API_URL}/users/{user['id']}", json=payload)
    if response.status_code == 200:
        print(f"Usuário {user["id"]} atualizado com sucesso!")
    else:
        print(f"Erro na atualização do usuário {user["id"]}: {response.text}")


# Execução do Pipeline
user_ids = [1, 2]  # IDs que sabemos que existem no meu db.json

for id in user_ids:
    user_data = extract_user(id)
    if user_data:
        transformed_user = transform_user(user_data)
        load_user(transformed_user)
