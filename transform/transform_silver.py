import sys
sys.path.append(".")  # ← ponto em vez de dois pontos

import pandas as pd
from load.carregar import criar_engine

engine = criar_engine()

df_voos_silver = pd.read_sql("SELECT * FROM raw_voos", engine)
df_partidas_silver = pd.read_sql("SELECT * FROM raw_partidas",engine)
df_chegadas_silver = pd.read_sql("SELECT * FROM raw_chegadas",engine)
df_intervalos_silver = pd.read_sql("SELECT * FROM raw_intervalo",engine)

print(df_voos_silver)

frames = [df_voos_silver, df_chegadas_silver, df_partidas_silver, df_intervalos_silver]


def icao_maiusculo(df):
     df = df.copy()
     df['icao24'] = df['icao24'].str.upper()
     return df

frames = [icao_maiusculo(df) for df in frames]


# Proximos ataques , vamos de timestamp e distancia. Construir esses frames 

def normalizacao_timestamp(df):
     df = df.copy()
     if "firstSeen" in df.columns:
        df['firstSeen'] = pd.to_datetime(df["firstSeen"], unit='s')

     if "time_position" in df.columns and "last_contact" in df.columns:
        df['time_position'] = pd.to_datetime(df["time_position"],unit='s')
        df['last_contact'] = pd.to_datetime(df["last_contact"],unit='s')

     if "lastSeen" in df.columns:
         df['lastSeen'] = pd.to_datetime(df["lastSeen"] , unit='s')
     

     return df

frames = [normalizacao_timestamp(df) for df in frames]
df_voos_silver, df_chegadas_silver, df_partidas_silver, df_intervalo_silver = frames

print(df_chegadas_silver['lastSeen'])