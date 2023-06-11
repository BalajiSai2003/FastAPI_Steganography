from pydantic import BaseSettings


class Settings(BaseSettings):
    image_path : str
    encoded_image_path : str
    class Config:
        env_file = ".env"


settings = Settings()