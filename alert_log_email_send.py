import smtplib
from email.mime.text import MIMEText

# Sender's Gmail credentials
gmail_user = "ganaaganaa6728@gmail.com"
gmail_password = "udgksojlwxjsusfe"  # If using App Password, provide the App Password here

# Recipient's email address
to_email = "tee370154@gmail.com"

# Create an email message
subject = "Snort Alert"
message = "A Snort alert has been triggered on your network. View the alert log here: https://drive.google.com/drive/folders/1s5zyXYAo53yKrVWiMXjFigjTTobISQZ7?usp=share_link"

msg = MIMEText(message, 'plain')
msg['From'] = gmail_user
msg['To'] = to_email
msg['Subject'] = subject

try:
    # Connect to Gmail's SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Login using the provided Gmail credentials or App Password
    server.login(gmail_user, gmail_password)

    # Send the email
    server.sendmail(gmail_user, to_email, msg.as_string())
    server.close()
    print("Email sent successfully.")
except smtplib.SMTPAuthenticationError as e:
    print(f"Email sending failed: {e}")
