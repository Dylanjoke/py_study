import os
from dotenv import load_dotenv

load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
HITOKOTO_URL = os.getenv("HITOKOTO_URL")

TIMEOUT = int(os.getenv("TIMEOUT", 10))
MAX_RETRY = int(os.getenv("MAX_RETRY", 3))
