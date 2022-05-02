import schedule
import time
import test

schedule.every().day.at("19:01").do(test.api_to_db,'It is 19:01')

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute