import scraper
import email_sender
import time

# Option to run script continuously on user's machine
def run_local():
    activated = True
    while activated:
        if scraper.get_seats():
            email_sender.send_email()
            activated = False
            print("Opening found at " + time.ctime())
            print("Local script stopped")
        else:
            print("Class still full... at " + time.ctime())

    # set to check every 5 minutes
    time.sleep(10)


# Script can run while computer is on and alert via console logs and email
run_local()
