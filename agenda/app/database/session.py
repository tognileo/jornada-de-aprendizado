from sqlalchemy.orm import sessionmaker

from app.database.connection import engine

SessionLocal = sessionmaker(bind=engine, autoflush=False)


def get_db():
    """Abre uma sessão com o banco para cada requisição e fecha no final."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
