import threading

from bot.telegram_bot import run_bot
from monitor.checker import run_check_loop
from config import CHECK_INTERVAL


def start_monitor():
    run_check_loop(CHECK_INTERVAL)


if __name__ == "__main__":

    print("SPB ZAGS Monitor запускается")

    monitor_thread = threading.Thread(
        target=start_monitor,
        daemon=True
    )

    monitor_thread.start()

    run_bot()