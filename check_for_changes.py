import difflib
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
import requests  # Add this line to import the requests module


# Load the saved source code
saved_source_code_path = Path("source_code.html")
saved_source_code = saved_source_code_path.read_text(encoding="utf-8")

# Fetch the current source code
url = "https://cdn.digialm.com/EForms/configuredHtml/1258/83923/Index.html"
response = requests.get(url)
current_source_code = response.text

# Compare the source codes
differ = difflib.Differ()
diff = list(differ.compare(saved_source_code.splitlines(), current_source_code.splitlines()))

# If there are differences, send an email
if any(line.startswith('+ ') or line.startswith('- ') for line in diff):
    subject = "Change Detected in IB JIO Website"
    body = "\n".join(diff)

    # Email configuration
    sender_email = "ekanturadescript@rediffmail.com"
    receiver_email = "ekant.urade@gmail.com"
    smtp_server = "smtp.rediffmailpro.com"
    smtp_port = 586
    smtp_username = "ekanturadescript@rediffmail.com"
    smtp_password = "Password@123"

    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls(context=ssl.create_default_context())
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
