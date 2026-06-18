from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
from urllib.parse import quote_plus
import os

load_dotenv()

PGHOST = os.getenv("PGHOST")
PGPORT = os.getenv("PGPORT", "5432")
PGDATABASE = os.getenv("PGDATABASE")
PGUSER = os.getenv("PGUSER")
PGPASSWORD = quote_plus(os.getenv("PGPASSWORD", ""))

DATABASE_URL = (
    f"postgresql://{PGUSER}:{PGPASSWORD}"
    f"@{PGHOST}:{PGPORT}/{PGDATABASE}"
    f"?sslmode=require"
)
print("PGHOST =", os.getenv("PGHOST"))
print("PGUSER =", os.getenv("PGUSER"))
print("PGDATABASE =", os.getenv("PGDATABASE"))
print("PGPASSWORD =", os.getenv("PGPASSWORD"))

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()