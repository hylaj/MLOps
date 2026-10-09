# settings.py
from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    API_KEY: str

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value):
        ...  # implement me!
        # prepare validator that will check whether the value of ENVIRONMENT is in (dev, test, prod)
        allowed_environments = ["dev", "test", "prod"]
        if value not in allowed_environments:
            raise ValueError(
                f"Environment must be one of {allowed_environments}, got '{value}'"
            )

        return value
