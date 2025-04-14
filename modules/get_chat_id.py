from modules.auth import start_client

async def main():
    client = await start_client()

    async for dialog in client.iter_dialogs():
        print(f"Chat Name: {dialog.name} → chat_id: {dialog.id}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
