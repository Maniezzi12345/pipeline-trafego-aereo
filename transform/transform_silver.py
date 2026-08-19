import sys
sys.path.append(".")  # ← ponto em vez de dois pontos

import pandas as pd
from load.carregar import criar_engine

engine = criar_engine()

df_voos_silver = pd.read_sql("SELECT * FROM raw_voos", engine)
df_partidas_silver = pd.read_sql("SELECT * FROM raw_partidas",engine)
df_chegadas_silver = pd.read_sql("SELECT * FROM raw_chegadas",engine)
df_intervalos_silver = pd.read_sql("SELECT * FROM raw_intervalo",engine)



df_query = pd.read_sql("""SELECT COUNT(RI.icao24) AS Quantidade,
                                 RP.firstSeen 
                        FROM raw_voos AS RW 
                        JOIN raw_intevalo AS RP 
                        ON RW.icao24 = RP.icao24 
                        GROUP BY RP.firstSeen  
                        HAVING Quantidade > 30  ORDER BY Quantidade DESC """,engine)

print(df_query)



# print(df_voos_silver['velocity'])


# frames = [df_voos_silver, df_chegadas_silver, df_partidas_silver, df_intervalos_silver]


# def icao_maiusculo(df):
#      df = df.copy()
#      df['icao24'] = df['icao24'].str.upper()
#      return df


# def normalizacao_timestamp(df):
#      df = df.copy()
#      if "firstSeen" in df.columns:
#         df['firstSeen'] = pd.to_datetime(df["firstSeen"], unit='s')

#      if "time_position" in df.columns and "last_contact" in df.columns:
#         df['time_position'] = pd.to_datetime(df["time_position"],unit='s')
#         df['last_contact'] = pd.to_datetime(df["last_contact"],unit='s')

#      if "lastSeen" in df.columns:
#          df['lastSeen'] = pd.to_datetime(df["lastSeen"] , unit='s')
     

#      return df


# def normalizacao_distancia(df):
#     df = df.copy()
#     colunas = [
#         'estDepartureAirportHorizDistance',
#         'estDepartureAirportVertDistance',
#         'estArrivalAirportHorizDistance',
#         'estArrivalAirportVertDistance'
#     ]

#     for coluna in colunas:
#         if coluna in df.columns:
#             df[coluna] = df[coluna] / 100
#     return df

# def normalizacao_velocidade(df):
#     df = df.copy()
#     df['velocity'] = df["velocity"] * 3.6
#     return df

# frame = normalizacao_velocidade(df_voos_silver)
# frames = [normalizacao_distancia(df) for df in frames]
# frames = [normalizacao_timestamp(df) for df in frames]
# frames = [icao_maiusculo(df) for df in frames]
# df_voos_silver, df_chegadas_silver, df_partidas_silver, df_intervalo_silver = frames


# print(df_voos_silver['velocity'])
