import schedule
import time
from datetime import datetime


def print_phrase(phrase):
    current_hour = datetime.now().hour
    repetitions = min(current_hour, 12)
    print(phrase * repetitions)


def run_scheduler(message, silence_hours):
    start_hour, end_hour = map(int, silence_hours.split('-'))
    for h in range(24):
        if start_hour <= h <= end_hour:
            continue
        schedule.every().hour.at(f"{h:02}:00").do(lambda: print_phrase(message))


message = input("Введите сообщение для вывода в консоль: ")
silence_hours = input("Введите диапазон времени (часы, когда программа должна молчать) в формате '00-07': ")

run_scheduler(message, silence_hours)

while True:
    schedule.run_pending()
    time.sleep(1)
