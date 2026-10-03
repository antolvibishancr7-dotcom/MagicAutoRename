import os
import asyncio
from aiohttp import web
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

async def handle(request):
    return web.Response(text="Bot is running!")

async def web_server():
    server = web.Application()
    server.add_routes([web.get('/', handle)])
    runner = web.AppRunner(server)
    await runner.setup()
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()

async def main():
    await web_server()
    await app.start()
    print("Bot started")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
