import sys
sys.path.append(".")  # ← ponto em vez de dois pontos

import pandas as pd
from load.carregar import criar_engine

engine = criar_engine()

df_voos_silver = pd.read_sql("SELECT * FROM raw_voos", engine)
df_partidas_silver = pd.read_sql("SELECT * FROM raw_partidas",engine)
df_chegadas_silver = pd.read_sql("SELECT * FROM raw_chegadas",engine)
df_intervalos_silver = pd.read_sql("SELECT * FROM raw_intervalo",engine)

frames = [df_voos_silver, df_chegadas_silver, df_partidas_silver, df_intervalos_silver]

def icao_maiusculo(df):
     df = df.copy()
     df['icao24'] = df['icao24'].str.upper()
     return df

frames = [icao_maiusculo(df) for df in frames]
df_voos_silver, df_chegadas_silver, df_partidas_silver, df_intervalo_silver = frames


print(df_voos_silver)


# Proximos ataques , vamos de timestamp e distancia. Construir esses frames 