import smtplib  # module for sending email
from email.message import EmailMessage  # module for creating email message
from getpass import getpass  # module for reading password privately

from datetime import datetime

TIMESTAMP = datetime.now().ctime()  # get a time string for the current date/time

SENDER = 'jstrickler@gmail.com'
RECIPIENTS = 'jstrickler@gmail.com'
MESSAGE_SUBJECT = 'Python SMTP example'

PLAIN_BODY = f"""
Hello at {TIMESTAMP}.

Testing text-only email from Python
"""

HTML_BODY = f"""
<html>
<head></head>
<body>
<h1>Hello</h1>
<h2>{TIMESTAMP}</h2>
<h3>Testing HTML email from Python</h3>
See more examples of using EmailMessage <a href="https://docs.python.org/3/library/email.examples.html">here</a>
<body>
</html>
"""


SMTP_USER = 'pythonclass'
SMTP_PASSWORD = getpass("Enter SMTP server password:")  # get password (not echoed to screen)
smtp = smtplib.SMTP("smtp2go.com", 2525)  # connect to SMTP server
smtp.login(SMTP_USER, SMTP_PASSWORD)  # log into SMTP server

msg = EmailMessage()  # create empty email message
msg['Subject'] = MESSAGE_SUBJECT  # add the message subject
msg['from'] = SENDER  # add the sender address
msg['to'] = RECIPIENTS  # add a list of recipients

msg.set_content(PLAIN_BODY)
msg.add_alternative(HTML_BODY, subtype='html')

try:    
    smtp.sendmail(SENDER, RECIPIENTS, msg.as_string())  # send the message
except smtplib.SMTPException as err:
    print("Unable to send mail:", err)
else:
    print("Mail sent.")
finally:
    smtp.quit()  # disconnect from SMTP server
