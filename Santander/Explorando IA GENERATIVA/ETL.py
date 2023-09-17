# O pandas vai fazer a leitura do CSV e criar uma estrutura
import pandas as pd
import requests
import json

# URL BASE
bscd2023_api_url = 'https://sdw-2023-prd.up.railway.app'

df = pd.read_csv('SBCD2023.csv') # Indicando ao pandas qual arquivo ele deve ler.
user_ids = df['UserID'].tolist() # Vai indicar a leitura de todos os dados que tiver após esse cabeçalho
print(user_ids) # Print de teste de reconhecimento de leitura da planilha.

def get_user(id):
    response = requests.get(f'{bscd2023_api_url}/users/{id}')
    return response.json() if response.status_code == 200 else None


users = [user for id in user_ids if (user := get_user(id)) is not None] # Compreensão de listas

print (json.dumps(users, indent= 2))
