# O pandas vai fazer a leitura do CSV e criar uma estrutura
import pandas as pd

df = pd.read_csv('SBCD2023.csv') # Indicando ao pandas qual arquivo ele deve ler.
user_ids = df['UserID'].tolist() # Vai indicar a leitura de todos os dados que tiver após esse cabeçalho
print(user_ids)
