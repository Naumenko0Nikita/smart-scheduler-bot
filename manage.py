import asyncio
import sys
from modules.messenger import start_client, send_message
from modules.scheduler import schedule_loop
from modules.config import TARGET_CHAT
from modules.logger import log_info, log_error


async def main():
    await start_client()
    await send_message(chat = TARGET_CHAT, text = "Aboba test")
    await schedule_loop()



async def run_bot():
    while True:
        try:
            log_info("Bot_Started...")
            await main()
        except Exception as _ex:
            log_error(f"\n\n\nError: {_ex}")
            await asyncio.sleep(5)

if __name__ == "__main__":
    log_info("Bot_Modules_Started...")
    
    if len(sys.argv) > 1 and sys.argv[1] == "reset":
        from tools.reset import reset_limits
        reset_limits()
        print("✅ Limits reset from terminal.")
    else:
        asyncio.run(main())