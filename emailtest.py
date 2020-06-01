import smtplib, ssl

# Import the email modules we'll need
from email.message import EmailMessage

port = 587 # For ssl
smtp_server = "smtp.office365.com"
password = input("Type your password and press enter:")
sender_email = "tanyuhao@hotmail.com"
receiver_email = input("Type the receiver_email:")
message = """\
Subject: Hi there

This message is sent from Python."""

with smtplib.SMTP(smtp_server,port,timeout=20) as server:
    # SMTP automatically tries ESMTP EHLO first when there are no previous EHLO or HELO command in the session.
    server.starttls()
    server.login("tanyuhao@hotmail.com", password)
    server.sendmail(sender_email, receiver_email, message)
    print('Sent email successfully')
except Exception as e: print(e)
