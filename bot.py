import os
from aiohttp import web
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

# API credentials and bot token
API_ID = 39784792
API_HASH = "af8bb8dfb528691edbb3f7ee7669d0c6"
BOT_TOKEN = "8763983777:AAEQaJY_fslgnRtOq3VjHK-7sewHMdk-eXo"

ADMIN_ID = 5727705309
ADMIN_USERNAME = "@SilentKingKiller"

# Initialize Pyrogram Client
app = Client(
    "audio_renamer_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# HTTP Server handler for Render
async def health_check(request):
    return web.Response(text="Bot is running smoothly!")

async def start_web_server():
    server = web.Application()
    server.add_routes([web.get('/', health_check)])
    runner = web.AppRunner(server)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"Web server started on port {port}")

async def main():
    await start_web_server()
    await app.start()
    print("Pyrogram Bot Started")
    # Keep the loop running
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
