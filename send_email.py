import smtplib
from email.message import EmailMessage
from configparser import ConfigParser


def send_email(attachment_file_name):
    config = ConfigParser()
    config.read('config.ini')

    email_config = config['EMAIL']

    EMAIL_ADDRESS = email_config['email']
    EMAIL_PASSWORD = email_config['password']

    contacts = [email_config['email']]

    msg = EmailMessage()
    msg['Subject'] = 'Disney Dining Schedule'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = contacts
    msg.set_content('Disney Dining Availability...')

    with open(attachment_file_name, 'rb') as f:
        file_data = f.read()
        file_name = f.name

        msg.add_attachment(file_data, maintype='application',subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)