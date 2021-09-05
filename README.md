# asu-seat-alert

_A useful side project I used to enroll in full ASU classes by alerting when spots open._<br/><br/>

Written in **Python**, with **BeautifulSoup** and **requests_html** libraries for web scraping, and **AWS SES** for email alerts.<br/><br/>

To use this project **locally**:
<<<<<<< HEAD

=======
>>>>>>> 63e41022179fcc0c1b6cad976386942ad3550244
1. Clone the repo and navigate to it on the command line
2. Create a virtual environment: `python -m venv env` and activate it: `source env/bin/activate`
3. Use pip to install the requirements file: `python -m pip install -r requirements.txt`
4. Find your desired class here: https://webapp4.asu.edu/catalog/
5. Change class_num in the class_num.py file to your class number
6. Set the check frequency to your liking, in local_launcher.py at line: `time.sleep(60)`
7. Run local_launcher.py<br/><br/>

To enable email alerts:
<<<<<<< HEAD

=======
>>>>>>> 63e41022179fcc0c1b6cad976386942ad3550244
1. Obtain Amazon SES SMTP credentials: https://docs.aws.amazon.com/ses/latest/DeveloperGuide/smtp-credentials.html
2. In the repo, create a file called credentials.py
3. Add string variables my_email, my_ses_username, and my_ses_password with your email address, SES username, and SES password respectively
4. Uncomment the following line in local_launcher: `email_sender.send_email()`<br/><br/><br/><br/>

Deployed to **AWS Lambda** following these instructions: https://docs.aws.amazon.com/lambda/latest/dg/python-package.html

Alternative Docker image method: https://docs.aws.amazon.com/lambda/latest/dg/python-image.html

Scheduling the script: https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/RunLambdaSchedule.html
<<<<<<< HEAD
<br/><br/>
=======
>>>>>>> 63e41022179fcc0c1b6cad976386942ad3550244
