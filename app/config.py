import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

# Настройки подключения к Yandex Cloud S3 через IAM-токен
class Settings:
    def __init__(self) -> None:
        self.endpoint_url: str = os.getenv(
            "S3_ENDPOINT_URL", "https://storage.yandexcloud.net"
        )
        self.iam_token: str = os.getenv("IAM_TOKEN", "")

    def validate(self) -> None:
        if not self.iam_token:
            raise RuntimeError("Не задана переменная окружения: IAM_TOKEN")


settings = Settings()