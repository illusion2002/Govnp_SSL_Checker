import smtplib
from email.mime.text import MIMEText
import logging
from config import SMTP_SERVER, SMTP_PORT, EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER

def send_email_alert(host, days_left):
    subject = f"SSL Expiry - {days_left} Days Left - {host}"
    body = f"The SSL certificate for {host} will expire in {days_left} day(s)."
    msg = MIMEText(body)
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    msg['Subject'] = subject

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        logging.info(f"Alert sent for {host}")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")
