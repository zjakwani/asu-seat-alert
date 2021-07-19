import scraper
import email_sender

# The AWS Lambda function
# Make sure to append this file to zipped dependencies file
# In runtime settings name the handler "lambda_function.lambda_handler"
def lambda_handler(event, context):
    if scraper.get_seats():
        email_sender.send_email()
        return "Spot open, email sent"
    else:
        return "Class full, do nothing"
