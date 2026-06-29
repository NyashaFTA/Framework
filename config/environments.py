import os

ENV = os.getenv("ENV", "local")

ENV_CONFIG = {
    "local": {
        #"base_url": None,
        "api_url": "http://127.0.0.1:8000/"
    },

    "stage": {
        "base_url": "https://stage.pstv.ru",
        # "api_url": None,
    },
    "test": {
        "base_url": "https://test.pstv.ru",
        # "api_url": None,
    },
}

BASE_URL = ENV_CONFIG[ENV]["base_url"]
API_URL = ENV_CONFIG[ENV]["api_url"]