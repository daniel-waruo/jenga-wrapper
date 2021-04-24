# settings.py
import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path('/home/daniel/PycharmProjects/jenga-wrapper/.env')

load_dotenv(dotenv_path=env_path, verbose=True)
print(env_path)
JENGA_API_KEY = os.getenv("JENGA_API_KEY")
JENGA_MERCHANT_CODE = os.getenv("JENGA_MERCHANT_CODE")
JENGA_PASSWORD = os.getenv("JENGA_PASSWORD")
JENGA_PRIVATE_KEY = os.getenv("JENGA_PRIVATE_KEY", "").replace('\\n', '\n')
