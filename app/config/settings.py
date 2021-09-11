import os

from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = int(os.getenv('DB_PORT'))  # type: ignore
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_MAX_CONNECTIONS = int(os.getenv('DB_MAX_CONNECTIONS'))  # type: ignore

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

TG_BOT_TOKEN = os.getenv('TG_BOT_TOKEN')
TG_CHAT_ID = os.getenv('TG_CHAT_ID')
