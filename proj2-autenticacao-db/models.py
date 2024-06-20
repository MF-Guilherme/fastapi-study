from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timezone


USER = 'root'
PASSWORD = ''
HOST = 'localhost'
DB = 'aulafastapi'
PORT = '3306'

CONN = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Pessoa(Base):
    __tablename__ = 'Pessoa'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    usuario = Column(String(20))
    senha = Column(String(10))


class Tokens(Base):
    __tablename__ = 'Tokens'
    id = Column(Integer, primary_key=True)
    id_pessoa = Column(Integer, ForeignKey('Pessoa.id'))
    token = Column(String(100))
    data = Column(DateTime, default=lambda: datetime.now(timezone.utc))


Base.metadata.create_all(engine)
