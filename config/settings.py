import os

# настройка браузера
BROWSER = os.getenv("BROWSER", "chrome")
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
WINDOW_SIZE = os.getenv("WINDOW_SIZE", "1920,1080")

# таймауты
DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10"))
EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "15"))
POLL_FREQUENCY = float(os.getenv("POLL_FREQUENCY", "0.5"))

RETRY_COUNT = int(os.getenv("RETRY_COUNT", "1"))

# пути
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "reports/screenshots")
ALLURE_RESULTS_DIR = os.path.join(BASE_DIR, "reports/allure")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

# на будущее
VALID_TEST_USER = os.getenv("VALID_USER_EMAIL")
AUTH_CODE = os.environ.get("AUTH_CODE")