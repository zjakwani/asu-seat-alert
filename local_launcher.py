import scraper
import email_sender
import time

# Option to run script continuously on user's machine
def run_local():
    activated = True
    while activated:
        if scraper.get_seats():

            # UNCOMMENT THE LINE BELOW FOR EMAIL ALERTS (CREDENTIALS FILE REQUIRED)
            # email_sender.send_email()

            activated = False
            print("Opening found at " + time.ctime())
            print("Local script stopped")
        else:
            print("Class still full... at " + time.ctime())

    # CHECK FREQUENCY (in seconds)
    time.sleep(60)


# Script can run while computer is on and alert via console logs and email
run_local()
