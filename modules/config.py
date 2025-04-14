import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
SESSION_NAME = os.getenv("SESSION_NAME")
TARGET_CHAT = int(os.getenv("TARGET_CHAT"))
SCHEDULE_FILE = os.getenv("SCHEDULE_FILE")

schedule = [
    {
        "day": 0,  
        "time": "15:10",
        "message": "TEST"
    },
]
