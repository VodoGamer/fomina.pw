import os

from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "qwerty")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = int(os.getenv("POSTGRES_PORT", 5432))
DB_TABLE = os.getenv("POSTGRES_TABLE", "fomina_pw")

BASE_DB_URI = f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_TABLE}"
PSYCOPG_DB_URI = f"postgresql://{BASE_DB_URI}"
ASYNC_DB_URI = f"postgresql+asyncpg://{BASE_DB_URI}"
