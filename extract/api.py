import requests
import os
from dotenv import load_dotenv
import pandas as pd
load_dotenv()



TOKEN_URL = "https://auth.opensky-network.org/auth/realms/opensky-network/protocol/openid-connect/token"
LOCALIZACAO_URL =  "https://opensky-network.org/api/states/all?lamin=-33.7&lamax=5.2&lomin=-73.9&lomax=-34.7" 
CHEGADAS_URL  = "https://opensky-network.org/api/flights/arrival?airport=SBGR&begin=1517227200&end=1517230800"
PARTIDAS_URL = "https://opensky-network.org/api/flights/departure?airport=SBGR&begin=1517227200&end=1517230800"
INTERVALO_URL = "https://opensky-network.org/api/flights/all?begin=1517227200&end=1517230800"


def autenticacao_url(TOKEN_URL):
    response = requests.post(
        TOKEN_URL,
        data={
            "grant_type":"client_credentials",
            "client_id": os.getenv("CLIENT_ID"),
            "client_secret":os.getenv("CLIENT_SECRET")
        }
    )

    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        print(f"A api de autenticação deu erro : {requests.response}")


def buscar_voos_brasil(token,LOCALIZACAO_URL):
    response = requests.get(
        LOCALIZACAO_URL,
        headers={"Authorization": f"Bearer {token}"

        }
    )
    if response.status_code == 200:
        return response.json()
    else:
        print(f"O endpoint de buscar_voos_brasil está com erro  : {requests.response}")

    # dados = response.json()
    # df = pd.DataFrame(dados["states"])
    # print(df)

def buscar_chegadas_voos(token,CHEGADAS_URL):
    response = requests.get(
        CHEGADAS_URL,
        headers={"Authorization": f"Bearer {token}"
        }
    )
    if response.status_code == 200:
            return response.json()
    else:
        print(f"O endpoint de buscar_chegadas_voos está com erro : {requests.response}")


def buscar_partidas_voos(token,PARTIDAS_URL):
    response = requests.get(
    PARTIDAS_URL,
    headers={"Authorization": f"Bearer {token}"
        }
    )
    if response.status_code == 200:
            return response.json()
    else:
            print(f"O endpoint de buscar_partidas_brasil : {requests.response}")

def intervalo_de_tempos_voos(token,INTERVALO_URL):
    response = requests.get(
    INTERVALO_URL,
    headers={"Authorization": f"Bearer {token}"
        }
    )
    if response.status_code == 200:
            return response.json()
    else:
            print(f"O endpoint de buscar_partidas_brasil : {requests.response}")

resultado = autenticacao_url(TOKEN_URL)
local = buscar_voos_brasil(resultado,LOCALIZACAO_URL)
chegada = buscar_chegadas_voos(resultado,CHEGADAS_URL)
partidas = buscar_partidas_voos(resultado,PARTIDAS_URL)
intervalo = intervalo_de_tempos_voos(resultado,INTERVALO_URL)

print(intervalo)

