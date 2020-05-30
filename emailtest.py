import smtplib, ssl

port = 587 # For ssl
smtp_server = "smtp.office365.com"
password = input("Type your password and press enter:")
sender_email = "tanyuhao@hotmail.com"
receiver_email = "tanyuhao@gmail.com"
message = """\
Subject: Hi there

This message is sent from Python."""

with smtplib.SMTP(smtp_server,port,timeout=20) as server:
    server.ehlo()
    server.starttls()
    server.login("tanyuhao@hotmail.com", password)
    server.sendmail(sender_email, receiver_email, message)
    server.quit()
    print('Sent email successfully')
