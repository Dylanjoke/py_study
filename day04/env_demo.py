import os
from dotenv import load_dotenv

# 显式指定 .env 路径，避免交互式窗口 cwd 不同导致找不到
load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))

api_key = os.getenv("DEEPSEEK_API_KEY")
url = os.getenv("HITOKOTO_URL")

if not api_key:
    print("API key not found")
else:
    print(f"API key: loaded ({len(api_key)} chars)")
    print(f"URL: {url}")
