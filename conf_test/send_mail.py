import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.header import Header
import datetime
import os
from datetime import datetime

from dotenv import dotenv_values

envs = dotenv_values('.env')


def send_report(receiver_email, reports, project_name):
    sender = 'unidevgo.qa3@gmail.com'
    receiver = receiver_email

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Email Subject
    mail_title = f'Test Report of {project_name} ' + str(current_time)

    print("*" * 80)
    mail_body = "Here is the report for the test run at " + str(current_time) + "\n\n"

    # Mail content, format, encoding
    message = MIMEMultipart("alternative")
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header(mail_title, 'utf-8')

    message.attach(MIMEText(mail_body))

    for report in reports:  # add files to the message
        filename = os.path.basename(report)
        attachment = MIMEApplication(open(report, "rb").read(), _subtype="txt")
        attachment.add_header('Content-Disposition', 'attachment', filename=filename)
        message.attach(attachment)

    print("Sending report...")
    print("*" * 80)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(envs["email_address"], envs["email_password"])
        server.sendmail(sender, receiver, message.as_string())
        print(f"Sent report successfully to {receiver_email} !!!")
        server.close()

    except Exception as e:
        print("Failed to send mail!!!, Error:", e)
