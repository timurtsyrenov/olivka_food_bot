import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv(key="BOT_TOKEN"))
ADMIN_ID = int(os.getenv(key="ADMIN_ID"))
FONT_LINK = os.getenv(key="FONT_LINK", default="/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf")
LOG_LEVEL = str(os.getenv(key="LOG_LEVEL", default="DEBUG"))
