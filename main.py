import schedule
import time
import logging
from scheduler import update_ssl_info

logging.basicConfig(level=logging.INFO)

schedule.every().monday.at("08:00").do(update_ssl_info)

if __name__ == "__main__":
    logging.info("SSL Monitor Started")
    while True:
        schedule.run_pending()
        time.sleep(60)
