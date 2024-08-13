import os
from dotenv import load_dotenv
import yagmail

load_dotenv()


yag = yagmail.SMTP('arjunadabir@gmail.com', os.getenv('APP_PASSWORD'))

SUBJECT = 'Thank you for RSVPing to SASICon 2024!'


def send_email(form_response, qr_code_file):
    """
    Sends an email to the form response with the QR code attached
    """
    to = form_response.email

    body = f"""
Hello {form_response.firstname}!

Thank you for RSVPing to SASICon 2024! 

Attached to this email is your QR code. This will be used throughout the conference to track attendance. The more events you attend, the more tickets you will have entered in the raffle.

We look forward to seeing you at the conference!

Best,
SASI
"""
    attachments = qr_code_file

    if not form_response.email_sent:
        yag.send(to=to, subject=SUBJECT, contents=body,
                 attachments=attachments)
        print('Email sent successfully!')
    else:
        print('Email already sent!')
