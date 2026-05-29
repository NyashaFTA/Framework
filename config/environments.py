import os

ENV = os.getenv("ENV", "stage")

ENV_CONFIG = {
    "stage": {
        "base_url": "https://stage.pstv.ru",
        # "api_url": None,
    },
    "test": {
        "base_url": "https://test.pstv.ru",
        # "api_url": None,
    },
}
