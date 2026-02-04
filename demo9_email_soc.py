import smtplib
import os
from email.message import EmailMessage
import mimetypes

# Configuration
smtp_server = 'smtp.example.com'  # Replace with your SMTP server
smtp_port = 587  # Usually 587 for TLS
smtp_user = 'your_email@example.com'  # Replace with your email
smtp_password = 'your_password'  # Replace with your password

sender = 'your_email@example.com'  # Replace with your email
receiver = 'soc_team@example.com'  # Replace with SOC email
subject = 'Evidence Folder - Incident Report'
body = 'Please find attached the evidence folder for the incident.'

evidence_folder = r"D:\Mine\Company\KPMG Feb 2026\BuildingAutomationSession\Evidence"

# Create the email message
msg = EmailMessage()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = subject
msg.set_content(body)

# Attach all files in the evidence folder
for filename in os.listdir(evidence_folder):
    filepath = os.path.join(evidence_folder, filename)
    if os.path.isfile(filepath):
        ctype, encoding = mimetypes.guess_type(filepath)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        with open(filepath, 'rb') as f:
            file_data = f.read()
            msg.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=filename)

# Send the email
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(msg)
    print('Email sent successfully to SOC.')
except Exception as e:
    print(f'Failed to send email: {e}')
