import email.utils
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from class_num import class_num
# see instructions in the readme
from credentials import my_email, my_ses_password, my_ses_username

# can send and receive from same email as long as verified on AWS SES
SENDER = my_email
RECIPIENT = my_email

# How to obtain credentials: https://docs.aws.amazon.com/ses/latest/DeveloperGuide/smtp-credentials.html
USERNAME_SMTP = my_ses_username
PASSWORD_SMTP = my_ses_password

# Using AWS SES SMTP interface to send email
def send_email():

    # email sender
    SENDERNAME = "asu-seat-alert"

    # can adjust based on user's AWS region
    HOST = "email-smtp.us-east-2.amazonaws.com"
    PORT = 587

    # email subject
    SUBJECT = "asu-seat-alert"

    # email body
    # includes class num and link to sign up portal
    BODY_HTML = f"""<html>
    <head></head>
    <body>
    
    <h1>Your class has opened up!</h1>
    <p>Sign up now at

        <a href='https://webapp4.asu.edu/myasu/'>MyASU</a>
        and search class number {class_num}.</p>
    </body>
    </html>
    """

    # In case email recipient does not use HTML
    BODY_TEXT = "asu-seat-alert\r\nYour class is open"

    # message container initialization
    msg = MIMEMultipart("alternative")
    msg["Subject"] = SUBJECT
    msg["From"] = email.utils.formataddr((SENDERNAME, SENDER))
    msg["To"] = RECIPIENT

    part1 = MIMEText(BODY_TEXT, "plain")
    part2 = MIMEText(BODY_HTML, "html")

    msg.attach(part1)
    msg.attach(part2)

    # Guide: https://docs.aws.amazon.com/ses/latest/DeveloperGuide/examples-send-using-smtp.html
    try:
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(USERNAME_SMTP, PASSWORD_SMTP)
        server.sendmail(SENDER, RECIPIENT, msg.as_string())
        server.close()
    except Exception as e:
        print("Error: ", e)
    else:
        print("Alert sent via email.")
