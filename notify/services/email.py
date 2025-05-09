import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv


load_dotenv()

class DispatchEmail:

    def __init__(self) -> None:
        self.__email_host = os.getenv('EMAIL_HOST')
        self.__email_port = os.getenv('EMAIL_PORT')
        self.__email_host_user = os.getenv('EMAIL_HOST_USER')
        self.__email_host_password = os.getenv('EMAIL_HOST_PASSWORD')

        if not all([self.__email_host, self.__email_port, self.__email_host_user, self.__email_host_password]):
            raise ValueError("Missing required email configuration in environment variables.")

    def send_email(self, subject, recipient_email, body):
        email_message = EmailMessage()

        email_message['Subject'] = subject
        email_message['From'] = self.__email_host
        email_message['To'] = recipient_email

        email_message.set_content(body)

        try:
            with smtplib.SMTP(self.__email_host, self.__email_port) as smtp:
                smtp.starttls()
                smtp.login(self.__email_host_user, self.__email_host_password)
                smtp.send_message(email_message)

                print("Email sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")
