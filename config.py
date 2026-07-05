import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))

BOT_NAME = "AntiScamGuardian"

DATABASE = "database/guild.db"

EMBED_COLOR = 0x2F3136