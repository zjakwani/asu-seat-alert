import scraper
import email_sender

# AWS Lambda function
def lambda_handler(event, context):
    if scraper.get_seats():
        email_sender.send_email()
        return "There's a spot open! Just sent an email."
    else:
        return "Sorry, class is still full"
