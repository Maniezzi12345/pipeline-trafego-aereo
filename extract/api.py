import requests
import os
from dotenv import load_dotenv
load_dotenv()



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
        print(f"A api de autenticação deu erro : {requests.response}")


def buscar_voos_brasil(token,LOCALIZACAO_URL):
    response = requests.get(
    LOCALIZACAO_URL,
    headers={"Authorization": f"Bearer {token}"}
    )
    if response.status_code == 200:
        return response.json()
    print(f"A api de buscar_voos_brasil : {requests.response}")



resultado = autenticacao_url(TOKEN_URL)
local = buscar_voos_brasil(resultado,LOCALIZACAO_URL)

print(local)

