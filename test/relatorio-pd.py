

import pandas as pd

# Substitua 'bolinha/bolinha2/meu_csv' pelo caminho real do seu arquivo CSV
caminho_do_csv = '/home/marinho/Documents/fisica-exp/Exp04_Aceleracao_da_gravidade_local.csv'

# Use o pandas para ler o CSV e pular as primeiras 6 linhas
# Defina o delimitador como ';' e remova espaços em branco dos nomes das colunas
df = pd.read_csv(caminho_do_csv, delimiter=';', skiprows=6, skipinitialspace=True)

# Selecione as colunas corretas
valores_t1_t2_t3 = df[['P1-T', 'P2-T', 'P3-T']].values

print(df.columns)
