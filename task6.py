import schedule
import time
from datetime import datetime


def print_phrase(phrase):
    current_hour = datetime.now().hour
    repetitions = min(current_hour, 12)
    print(phrase * repetitions)


schedule.every().hour.at(":00").do(lambda: print_phrase("Ку"))

while True:
    schedule.run_pending()
    time.sleep(1)
