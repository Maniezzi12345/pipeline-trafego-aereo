import requests
import os
from dotenv import load_dotenv
load_dotenv()



TOKEN_URL = "https://auth.opensky-network.org/auth/realms/opensky-network/protocol/openid-connect/token"

def autenticacao_url(TOKEN_URL):
    response = requests.post(
        TOKEN_URL,
        data={
            "grant_type":"client_credentials",
            "client_id": os.getenv("CLIENT_ID"),
            "client_secret":os.getenv("CLIENT_SECRET")
        }
    )


    token = response.json()["access_token"]

   
    if response.status_code == 200:
        return token
    else:
        print(f"O codigo deu erro {requests.response}")

resultado = autenticacao_url(TOKEN_URL)
print(resultado)