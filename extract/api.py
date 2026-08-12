import requests
import os
from dotenv import load_dotenv
import pandas as pd
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))



TOKEN_URL = "https://auth.opensky-network.org/auth/realms/opensky-network/protocol/openid-connect/token"
LOCALIZACAO_URL =  "https://opensky-network.org/api/states/all?lamin=-33.7&lamax=5.2&lomin=-73.9&lomax=-34.7" 



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
        print(f"A api de autenticação deu erro : {response.status_code} - {response.text}")


def buscar_voos_brasil(token,LOCALIZACAO_URL):
    response = requests.get(
        LOCALIZACAO_URL,
        headers={"Authorization": f"Bearer {token}"

        }
    )
    if response.status_code == 200:
        dados = response.json()
        return dados
    else: 
        print(f"O endpoint de buscar_voos_brasil está com erro  : {response.status_code} - {response.text}")


def buscar_chegadas_voos(token,begin,end):
    aeroportos = ["SBGR", "SBGL", "SBBR"]
    todos=[]
    for aeroporto in aeroportos:
        CHEGADAS_URL  = f"https://opensky-network.org/api/flights/arrival?airport={aeroporto}&begin={begin}&end={end}"
        response = requests.get(CHEGADAS_URL, headers={"Authorization": f"Bearer {token}"})
        if response.status_code == 200:
             dados = response.json()
             todos.extend(dados)
             print(f"{aeroporto}: chegadas:{len(dados)} voos")
        else:
            print(f" {aeroporto}: {response.status_code} - {response.text}")
    return todos


def buscar_partidas_voos(token,begin,end):
    aeroportos = ["SBGR", "SBGL", "SBBR"]
    todos = []
    for aeroporto in aeroportos:
         PARTIDAS_URL = f"https://opensky-network.org/api/flights/departure?airport={aeroporto}&begin={begin}&end={end}"
         response = requests.get(PARTIDAS_URL,headers={"Authorization": f"Bearer {token}"})
         if response.status_code == 200:
                dados = response.json()
                todos.extend(dados)
                print(f"{aeroporto}: saidas:{len(dados)} voos")
         else:
                print(f"O endpoint de buscar_partidas_brasil : {response.status_code} - {response.text}")
    return todos


def intervalo_de_tempos_voos(token,begin,end):
    INTERVALO_URL = f"https://opensky-network.org/api/flights/all?begin={begin}&end={end}"
    response = requests.get(
    INTERVALO_URL,
    headers={"Authorization": f"Bearer {token}"
        }
    )
    if response.status_code == 200:
            return response.json()
    else:
            print(f"O endpoint de buscar_partidas_brasil : {response.status_code} - {response.text}")




# forma de resolver frame 

# print(type(local))
# print(local.keys())
# print(type(local["time"]))
# print(type(local["states"]))

# print(local["states"][0])

# Vimos que a classe é de dict 
# Agora veremos as suas keys
# Achando as chaves veremis o tipo das chaves 




