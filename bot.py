import asyncio
from pyrogram import Client

API_ID = 39784792
API_HASH = "af8bb8dfb528691edbb3f7ee7669d0c6"
BOT_TOKEN = "8763983777:AAEQaJY_fslgnRtOq3VjHK-7sewHMdk-eXo"

app = Client(
    "audio_renamer_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

async def main():
    await app.start()
    print("Bot Started Successfully as Background Worker!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
