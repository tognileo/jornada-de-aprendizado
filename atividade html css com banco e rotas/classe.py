from sqlalchemy import Integer,String,Column,DECIMAL
from sqlalchemy.orm import  declarative_base
base = declarative_base()


class Produto (base):
    __tablename__ = "produto"
    id = Column (Integer, primary_key=True, index = True)
    nome = Column(String,nullable=True)
    marca = Column (String)
    preco = Column (DECIMAL, nullable=True)
    data_validade = Column (String )











































    
