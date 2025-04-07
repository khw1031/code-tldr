import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=os.getenv("ENV_FILE", ".env"))

    # Bitbucket settings
    bitbucket_access_token: str
    bitbucket_workspace: str

    # AWS settings
    aws_access_key_id: str
    aws_secret_access_key: str
    aws_region: str


settings = Settings()
