from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

from app.core.config import settings

url_do_banco = URL.create(
    drivername="mysql+pymysql",
    username=settings.db_user,
    password=settings.db_password,
    host=settings.db_host,
    port=settings.db_port,
    database=settings.db_name,
)

engine = create_engine(url_do_banco, pool_pre_ping=True)


def testar_conexao() -> bool:
    try:
        with engine.connect() as conexao:
            conexao.execute(text("SELECT 1"))
        return True
    except Exception:
        return False
