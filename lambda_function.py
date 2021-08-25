import scraper
import email_sender

# AWS Lambda function
def lambda_handler(event, context):
    if scraper.get_seats():
        email_sender.send_email()
        return "Spot open, email sent"
    else:
        return "Class full, do nothing"
