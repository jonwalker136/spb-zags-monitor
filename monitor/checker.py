import time


def check_availability():
    """
    Здесь позже будет логика проверки доступности.
    Сейчас это тестовый модуль.
    """

    return {
        "available": False,
        "message": "Проверка выполнена"
    }


def run_check_loop(interval=60):
    while True:
        result = check_availability()

        print(result["message"])

        time.sleep(interval)