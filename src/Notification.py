import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_notification(target_email, message, url):
    # Set up the SMTP server details
    smtp_server = os.getenv("smtp_server")
    smtp_port = os.getenv("smtp_port")
    sender_email = os.getenv("sender_email")
    sender_password = os.getenv("sender_password")

    # Create a MIMEText object for the email content
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = target_email
    msg['Subject'] = 'Notification:' + message

    body = "Bonjour chelfi, \n il se peut kayn jdid f la plateforme en ile de france, go check it out. \n URL :  \n" + url
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, target_email, msg.as_string())
        print("Notification email sent successfully.")
        server.quit()
    except Exception as e:
        print(f"Error while sending the email: {e}")