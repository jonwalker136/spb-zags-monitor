from telegram import Bot

from config import BOT_TOKEN, CHAT_ID


async def send_notification(message):
    if not BOT_TOKEN or not CHAT_ID:
        print("Нет BOT_TOKEN или CHAT_ID")
        return

    bot = Bot(token=BOT_TOKEN)

    await bot.send_message(
        chat_id=CHAT_ID,
        text=message
    )