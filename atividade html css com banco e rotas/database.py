from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/cadastro_produto"

#engine conversa com o banco de dados 
engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False,autoflush=False , bind=engine)















