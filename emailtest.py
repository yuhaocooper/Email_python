import smtplib, ssl

# Import the email modules we'll need
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

port = 587 # For ssl
smtp_server = "smtp.office365.com"
sender_email = "tanyuhao@hotmail.com"
password = input("Type your password and press enter:")
receiver_email = input("Type the receiver_email:")
subject = input("Type the subject of the email:")
content = input("Type the content of the email:")
Attachment = input("Type any attachment file name:")

#Attachment details
filename = Attachment
with open(filename,"rb") as attachment:
    # The content type "application/octet-stream" means that a MIME attachment is a binary file
    part = MIMEBase('application','octet-stream')
    part.set_payload(attachment.read())

#Encode to base64
encoders.encode_base64(part)

# Add header
part.add_header("Content-Disposition",
                "attachment", filename = filename
)

# Create the container email EmailMessage
msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = receiver_email #separate by ','
# Add body to email
msg.attach(MIMEText(content, 'plain'))
# Add attachment to your message and convert it to string
msg.attach(part)


with smtplib.SMTP(smtp_server,port,timeout=20) as server:
# SMTP automatically tries ESMTP EHLO first when there are no previous EHLO or HELO command in the session.
    server.starttls()
    server.login("tanyuhao@hotmail.com", password)
    server.send_message(msg)
    print('Sent email successfully')
