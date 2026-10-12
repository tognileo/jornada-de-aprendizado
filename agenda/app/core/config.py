from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Meu Dia"
    app_env: str = "development"

    db_host: str = "localhost"
    db_port: int = 3306
    db_name: str = "agenda"
    db_user: str = "root"
    db_password: str = ""
    secret_key: str = "chave-de-desenvolvimento-troque-no-env"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
