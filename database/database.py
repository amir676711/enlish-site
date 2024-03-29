from sqlalchemy import create_engine,URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = URL.create(
    drivername="mysql+pymysql",
    username="Arkad",
    password="Number13@@",
    host="185.81.96.252",
    database="AvisanEn_fastapi"
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
