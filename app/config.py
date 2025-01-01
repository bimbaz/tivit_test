import os

from dotenv import load_dotenv

load_dotenv(override=True)


class EnvConfig:
    access_token_expire_minutes = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

    secret_key = os.getenv(
        "SECRET_KEY", "1ca74d102466ff5c2553ed1a6dd61a5948f2544d978cf179a33941160a9b4c91"
    )
    algorithm = os.getenv("ALGORITHM", "HS256")
