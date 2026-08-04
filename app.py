import asyncio
from config import BOT_TOKEN

async def main():
    print("SPB ZAGS Monitor запущен")

    if not BOT_TOKEN:
        print("Ошибка: не найден BOT_TOKEN")
        return

    print("Telegram бот настроен")


if __name__ == "__main__":
    asyncio.run(main())
