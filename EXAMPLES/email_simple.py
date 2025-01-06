from getpass import getpass  # module for hiding password
import smtplib  # module for sending email
from email.message import EmailMessage  # module for creating message
from datetime import datetime

TIMESTAMP = datetime.now().ctime()  # get a time string for the current date/time

SENDER = 'jstrickler@gmail.com'
RECIPIENTS = ['jstrickler@gmail.com']
MESSAGE_SUBJECT = 'Python SMTP example'

MESSAGE_BODY = f"""
Hello at {TIMESTAMP}.

Testing email from Python
"""

SMTP_USER = 'pythonclass'
SMTP_PASSWORD = getpass("Enter SMTP server password:")  # get password (not echoed to screen)

msg = EmailMessage()  # create empty email message
msg.set_content(MESSAGE_BODY)  # add the message body
msg['Subject'] = MESSAGE_SUBJECT  # add the message subject
msg['from'] = SENDER  # add the sender address
msg['to'] = RECIPIENTS  # add a list of recipients

smtp = smtplib.SMTP("smtp2go.com", 2525)  # connect to SMTP server
smtp.login(SMTP_USER, SMTP_PASSWORD)  # log into SMTP server

try:
    smtp.send_message(msg)  # send the message
except smtplib.SMTPException as err:
    print("Unable to send mail:", err)
else:
    print("Mail sent.")
finally:
    smtp.quit()  # disconnect from SMTP server
