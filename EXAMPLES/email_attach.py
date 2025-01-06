import smtplib
import os
from datetime import datetime
import magic  # module to determine image type (install as python-magic-bin)
from email.message import EmailMessage  # module for creating email message
from getpass import getpass  # module for reading password privately


SMTP_SERVER = "smtp2go.com"  # global variables for external information (IRL should be from environment -- command line, config file, etc.)
SMTP_PORT = 2525

SMTP_USER = 'pythonclass'

SENDER = 'jstrickler@gmail.com'
RECIPIENTS = ['jstrickler@gmail.com']


def main():
    smtp_server = create_smtp_server()
    now = datetime.now()
    msg = create_message(
        SENDER,
        RECIPIENTS,
        'Here is your attachment',
        f'Testing email attachments from python class at {now}\n\n',
    )
    add_text_attachment('../DATA/parrot.txt', msg)
    add_image_attachment('../DATA/felix_auto.jpeg', msg)
    add_image_attachment('../DATA/zen_of_python.pdf', msg)
    send_message(smtp_server, msg)


def create_message(sender, recipients, subject, body):
    msg = EmailMessage()  # create instance of EmailMessage to hold message
    msg.set_content(body)  # set content (message text) and various headers
    msg['From'] = sender
    msg['To'] = recipients
    msg['Subject'] = subject
    return msg


def add_text_attachment(file_path, message):
    with open(file_path) as file_in:  # read data for text attachment
        attachment_data = file_in.read()
        file_name = os.path.basename(file_path)
    message.add_attachment(attachment_data, filename=file_name)  # add text attachment to message
    # if filename not specified, adds text inline


def add_image_attachment(file_path, message):
    with open(file_path, 'rb') as file_in:  # read data for binary attachment
        attachment_data = file_in.read()
    mime_type = magic.from_buffer(attachment_data, mime=True)
    main_type, sub_type = mime_type.split(mime_type)
    file_name = os.path.basename(file_path)
    # add binary attachment to message, including type and subtype (e.g., "image/jpg)"
    message.add_attachment(attachment_data, filename=file_name, maintype=main_type, subtype=sub_type)  
    

def create_smtp_server():
    password = getpass("Enter SMTP server password:")  # get password from user (don't hardcode sensitive data in script)
    smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)  # create SMTP server connection
    smtpserver.login(SMTP_USER, password)  # log into SMTP connection

    return smtpserver


def send_message(server, message):
    try:
        server.send_message(message)  # send message
    except smtplib.SMTPException as err:
        print(err)
    else:
        print("Mail sent.")
    finally:
        server.quit()


if __name__ == '__main__':
    main()
