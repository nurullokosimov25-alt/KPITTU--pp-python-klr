import math
import logging
# Настройка логирования
logging.basicConfig(
    filename="math.log",
    level=logging.ERROR,
    format="%(levelname)s: %(message)s"
)
def safe_divide(a, b):
    try:
        return a / b
    except Exception as e:
        logging.error(f"division | a={a}, b={b} | {e}")
        return None
def safe_sqrt(x):
    try:
        return math.sqrt(x)
    except Exception as e:
        logging.error(f"sqrt | x={x} | {e}")
        return None
def safe_log(x):
    try:
        return math.log(x)
    except Exception as e:
        logging.error(f"log | x={x} | {e}")
        return None
