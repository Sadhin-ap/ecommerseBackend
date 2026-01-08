from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from dotenv import load_dotenv
import os


load_dotenv()

DATABASE_URL ='postgresql://neondb_owner:npg_6ROUVWtp2ufL@ep-raspy-violet-a4xfnnec-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit = False,
    autoflush=False,
    bind = engine
)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()