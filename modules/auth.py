from telethon import TelegramClient
from .config import API_ID, API_HASH, SESSION_NAME, PHONE_NUMBER


async def start_client():
    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

    await client.start(PHONE_NUMBER)
    
    return client
