from monitor.checker import run_check_loop
from config import CHECK_INTERVAL


if __name__ == "__main__":
    print("SPB ZAGS Monitor запущен")

    run_check_loop(CHECK_INTERVAL)