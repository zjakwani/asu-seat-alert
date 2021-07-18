import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SENDER = "zjakwani@gmail.com"
SENDERNAME = "asu-seat-alert"

RECIPIENT = "zjakwani@gmail.com"

USERNAME_SMTP = "AKIAYJ4PBKZYXVPNTJEH"

PASSWORD_SMTP = "BFRtXNZuSn3aKPG3R3eG1ivDs91AgCf6wvtc5MUsZOx1"

HOST = "email-smtp.us-east-2.amazonaws.com"
PORT = 587

# The subject line of the email.
SUBJECT = "asu-seat-alert"

# The email body for recipients with non-HTML email clients.
BODY_TEXT = "asu-seat-alert\r\nFirst test email"


BODY_HTML = """<html>
<head></head>
<body>
  <h1>Your class has opened up!</h1>
  <p>This email was sent with Amazon SES using the
    <a href='https://www.python.org/'>Python</a>
    <a href='https://docs.python.org/3/library/smtplib.html'>
    smtplib</a> library.</p>
</body>
</html>
            """


msg = MIMEMultipart("alternative")
msg["Subject"] = SUBJECT
msg["From"] = email.utils.formataddr((SENDERNAME, SENDER))
msg["To"] = RECIPIENT

part1 = MIMEText(BODY_TEXT, "plain")
part2 = MIMEText(BODY_HTML, "html")

msg.attach(part1)
msg.attach(part2)

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
    print("Email sent!")
