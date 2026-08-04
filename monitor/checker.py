import time
import asyncio

from bot.notifier import send_notification


def check_availability():
    """
    Здесь позже будет настоящая проверка.
    Сейчас тестовое событие.
    """

    return {
        "available": False,
        "message": "Проверка выполнена"
    }


def run_check_loop(interval=60):

    while True:

        result = check_availability()

        print(result["message"])

        if result["available"]:
            asyncio.run(
                send_notification(
                    "🎉 Найдено свободное время!"
                )
            )

        time.sleep(interval)