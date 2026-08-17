import sys
sys.path.append(".")  # ← ponto em vez de dois pontos

import pandas as pd
from load.carregar import criar_engine

engine = criar_engine()

# # df_voos_silver = pd.read_sql("SELECT * FROM raw_voos", engine)
# df_partidas_silver = pd.read_sql("SELECT * FROM raw_partidas",engine)
# df_chegadas_silver = pd.read_sql("SELECT * FROM raw_chegadas",engine)
df_intervalos_silver = pd.read_sql("SELECT * FROM raw_intervalo",engine)
print(df_intervalos_silver)