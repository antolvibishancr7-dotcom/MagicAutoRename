import os
from pyrogram import Client, filters
from pyrogram.types import Message

API விவரங்கள் மற்றும் பாட் டோக்கன்
API_ID = 39784792
API_HASH = "af8bb8dfb528691edbb33f7ee7669f2d"
BOT_TOKEN = "8763983777:AAEQaJY_fslgnRtOq3VjhK-7sewHMdk-eXo"

ADMIN_ID = 5727705309
ADMIN_USERNAME = "@SilentKingKiller"

Pyrogram Client உருவாக்கம்
app = Client(
"audio_renamer_bot",
api_id=API_ID,
api_hash=API_HASH,
bot_token=BOT_TOKEN
)

அங்கீகரிக்கப்பட்ட பயனர்களின் பட்டியல்
AUTHORIZED_USERS = [ADMIN_ID]

def is_authorized(user_id):
return user_id in AUTHORIZED_USERS

def access_denied_text():
return (
f"⛔️ Access Denied: Your account is not authorized. Contact {ADMIN_USERNAME} to get a subscription.\n\n"
f"💡 Contact {ADMIN_USERNAME} to get a subscription."
)

/start கட்டளை
@app.on_message(filters.command("start"))
async def start_command(client, message: Message):
if not is_authorized(message.from_user.id):
await message.reply_text(access_denied_text(), parse_mode="markdown")
return

await message.reply_text(
"👋 Welcome to Advanced Audio Rename Bot!\n\n"
"Send me any large audio or document file (up to 2GB), and I will rename and watermark it for you.",
parse_mode="markdown"
)

அட்மின் கட்டளை: பிரீமியம் யூசரைச் சேர்க்க
@app.on_message(filters.command("add_premium"))
async def add_premium(client, message: Message):
if message.from_user.id != ADMIN_ID:
await message.reply_text("❌ You are not authorized to use this command.")
return

try:
parts = message.text.split()
if len(parts) < 2:
await message.reply_text("Usage: /add_premium &lt;user_id>", parse_mode="markdown")
return

new_user_id = int(parts[1])
if new_user_id not in AUTHORIZED_USERS:
AUTHORIZED_USERS.append(new_user_id)

await message.reply_text(f"✅ User {new_user_id} successfully added to authorized list.", parse_mode="markdown")
except Exception as e:
await message.reply_text(f"⚠️ Error: {str(e)}")

அட்மின் கட்டளை: பிரீமியம் யூசரை நீக்க
@app.on_message(filters.command("remove_premium"))
async def remove_premium(client, message: Message):
if message.from_user.id != ADMIN_ID:
await message.reply_text("❌ You are not authorized to use this command.")
return

try:
parts = message.text.split()
if len(parts) < 2:
await message.reply_text("Usage: /remove_premium &lt;user_id>", parse_mode="markdown")
return

old_user_id = int(parts[1])
if old_user_id in AUTHORIZED_USERS and old_user_id != ADMIN_ID:
AUTHORIZED_USERS.remove(old_user_id)
await message.reply_text(f"✅ User {old_user_id} removed from authorized list.", parse_mode="markdown")
else:
await message.reply_text("⚠️ User not found or cannot remove admin.")
except Exception as e:
await message.reply_text(f"⚠️ Error: {str(e)}")

பெரிய ஆடியோ மற்றும் டாக்குமெண்ட் ஃபைல்களைக் கையாளுதல்
@app.on_message(filters.audio | filters.document)
async def handle_audio_files(client, message: Message):
if not is_authorized(message.from_user.id):
await message.reply_text(access_denied_text(), parse_mode="markdown")
return

try:
media = message.audio or message.document
file_name = getattr(media, "file_name", "audio.mp3")

status_msg = await message.reply_text("📥 Downloading large audio file... Please wait.", parse_mode="markdown")
downloaded_path = await message.download()

await status_msg.edit_text("⚙️ Processing & Adding Watermark...", parse_mode="markdown")

watermark = "@MagicFM"
base_name, ext = os.path.splitext(file_name)
new_file_name = f"{base_name} [{watermark}]{ext}"

os.makedirs("downloads", exist_ok=True)
final_path = os.path.join("downloads", new_file_name)
os.rename(downloaded_path, final_path)

await status_msg.edit_text("📤 Uploading renamed file...", parse_mode="markdown")

caption = f"✨ File Successfully Renamed!\n\n🎧 {new_file_name}\n📢 Powered by Magic FM"
await message.reply_audio(
audio=final_path,
caption=caption,
parse_mode="markdown"
)

await status_msg.delete()
if os.path.exists(final_path):
os.remove(final_path)

except Exception as e:
await message.reply_text(f"⚠️ Error: {str(e)}")

print("Pyrogram Auto Rename Bot is running smoothly for large files...")
app.run()