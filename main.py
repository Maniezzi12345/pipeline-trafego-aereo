import sys
import pandas as pd
sys.path.append("..")

from extract.api import (
    autenticacao_url,
    buscar_voos_brasil,
    buscar_chegadas_voos,
    buscar_partidas_voos,
    intervalo_de_tempos_voos,
    TOKEN_URL,
    LOCALIZACAO_URL,
    COLUNAS_VOOS
)
from load.carregar import criar_engine, salvar_dataframe



print(" Iniciando pipeline...")

# 1. autenticação
token = autenticacao_url(TOKEN_URL)

# 2. extração
print(" Extraindo dados da API...")
local    = buscar_voos_brasil(token, LOCALIZACAO_URL)
chegadas = buscar_chegadas_voos(token, 1753484400, 1753570800)
partidas = buscar_partidas_voos(token, 1753484400, 1753570800)
intervalo = intervalo_de_tempos_voos(token, 1753484400, 1753570800)


# 3. converte para DataFrame
print(" Convertendo para DataFrame...")
df_voos      = pd.DataFrame(local["states"], columns=COLUNAS_VOOS)
df_chegadas  = pd.DataFrame(chegadas)
df_partidas  = pd.DataFrame(partidas)
df_intervalo = pd.DataFrame(intervalo)

# 4. engine
engine = criar_engine()

# 5. salva no banco
print("💾 Salvando no banco...")
salvar_dataframe(df_voos,      "raw_voos",      engine)
salvar_dataframe(df_chegadas,  "raw_chegadas",  engine)
salvar_dataframe(df_partidas,  "raw_partidas",  engine)
salvar_dataframe(df_intervalo, "raw_intervalo", engine)

print("✅ Pipeline concluído!")