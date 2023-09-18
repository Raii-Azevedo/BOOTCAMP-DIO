import pandas as pd
import requests
import json
import openai

# URL BASE
bscd2023_api_url = 'https://sdw-2023-prd.up.railway.app'

# Indicando ao pandas qual arquivo ele deve ler.
df = pd.read_csv('SBCD2023.csv')

# Vai indicar a leitura de todos os dados que tiverem após esse cabeçalho
user_ids = df['UserID'].tolist()

print(user_ids)  # Print de teste de reconhecimento de leitura da planilha.

def get_user(id):
    response = requests.get(f'{bscd2023_api_url}/users/{id}')
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao obter usuário {id}: {response.status_code}")
        return None

users = [user for id in user_ids if (user := get_user(id)) is not None]  # Compreensão de listas

# INTEGRAÇÃO COM O CHAT GPT
chave_api = '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'

openai.api_key = chave_api

# FUNÇÃO DE INTEGRAÇÃO
def generate_ai_news(user):
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo-0613',
        messages=[
            {
                "role": "system",
                "content": "Você é um especialista em marketing bancário."
            },
            {
                "role": "user",
                "content": f"Crie uma mensagem personalizada para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)"
            }
        ]
    )
    # Remover aspas duplas
    return completion.choices[0].message.content.strip('\"')

for user in users:
    news = generate_ai_news(user)
    print(news)
    user['news'].append({
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": news
    })


# FUNÇÃO DE ATUALIZAÇÃO
def update_user(user):
    response = requests.put(f"{bscd2023_api_url}/users/{user['id']}", json=user)
    return True if response.status_code == 200 else False


for user in users: # Chamada da função de atualização
    success = update_user(user) 
    print(f"{user['name']} updated? {success}")
    