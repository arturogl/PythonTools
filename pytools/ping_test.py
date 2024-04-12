import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to send email notification
def send_email(host):
    sender_email = "your_email@example.com"
    receiver_email = "recipient_email@example.com"
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_username = "your_smtp_username"
    smtp_password = "your_smtp_password"

    # Prepare email content
    email_subject = "Ping Test Failed"
    email_body = f"The host {host} did not respond to ping."

    # Create a MIMEText object for the email content
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = email_subject

    # Attach the email body
    message.attach(MIMEText(email_body, "plain"))

    # Connect to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Start TLS encryption
        server.login(smtp_username, smtp_password)  # Login to the SMTP server
        server.sendmail(sender_email, receiver_email, message.as_string())  # Send the email

# Read hostnames from file and perform ping test
with open("hostnames.txt", "r") as file:
    for line in file:
        hostname = line.strip()
        ping_process = subprocess.Popen(["ping", "-c", "4", hostname], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ping_output, ping_error = ping_process.communicate()
        if ping_process.returncode != 0:
            print(f"The host {hostname} did not respond to ping.")
            #send_email(hostname)
