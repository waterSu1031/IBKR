from pydantic import BaseSettings

class Settings(BaseSettings):
    IBKR_CLIENT_ID: int = 123
    IBKR_HOST: str = "127.0.0.1"
    IBKR_PORT: int = 7497
    IBKR_ACCOUNT: str = "DU123456"
    PAPER_TRADING: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
