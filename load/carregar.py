import os 
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()


def criar_engine():
    usuario = os.getenv("DB_USER")
    senha = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    porta = os.getenv("DB_PORT")
    banco = os.getenv("DB_NAME")
    engine = create_engine(f"postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}")
    return engine


def salvar_dataframe(df,tabela,engine):
    df.to_sql(
        name=tabela,
        con=engine,
        if_exists="append",
        index=False
    )
    print(f"{len(df)} registros inseridos em {tabela}")