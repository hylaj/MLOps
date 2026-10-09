import os
import yaml
import argparse
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:
    file = f"config/.env.{environment}"
    load_dotenv(dotenv_path=file)

    # implement me!
    load_yaml_secrets("secrets.yaml")


def load_yaml_secrets(filepath: str) -> None:
    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            secrets = yaml.safe_load(file)
            if secrets:
                for key, value in secrets.items():
                    os.environ[key.upper()] = str(value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("API_KEY: ", settings.API_KEY)
