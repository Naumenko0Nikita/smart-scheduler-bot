from telethon import TelegramClient
from .config import API_ID, API_HASH, SESSION_NAME, PHONE_NUMBER


client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

async def start_client():
    await client.start(PHONE_NUMBER)
    return client


async def send_message(chat, text):
    await client.send_message(chat, text)
