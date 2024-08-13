import os
from dotenv import load_dotenv
import yagmail

load_dotenv()

BODY = """
Hello!

Thank you for RSVPing to SASICon 2024! 

Attached to this email is your QR code. This will be used throughout the conference to track attendance. The more events you attend, the more tickets you will have entered in the raffle.

We look forward to seeing you at the conference!

Best,
SASI
"""

yag = yagmail.SMTP('arjunadabir@gmail.com', os.getenv('APP_PASSWORD'))

subject = 'Thank you for RSVPing to SASICon 2024!'
body = BODY
to = 'dabira@uci.edu'
attachments = './qrcode/qr_with_logo.png'

# Send email
yag.send(to=to, subject=subject, contents=body, attachments=attachments)

print('Email sent successfully!')
