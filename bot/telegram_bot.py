from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from config import BOT_TOKEN


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 SPB ZAGS Monitor запущен!\n\n"
        "Я буду помогать отслеживать появление свободного времени."
    )


def run_bot():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    print("Telegram бот работает")

    app.run_polling()
