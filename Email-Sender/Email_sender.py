import smtplib
import os
from email.message import EmailMessage

sender = input("Enter Your Email: ").strip()
app_key = input("Enter Your App Password: ").strip()
receiver = input("Enter the Receiver's Email: ").strip()

subject = input("Enter the Subject of Your Email: ").strip()
body = input("Enter the Body of Your Email: ").strip()

msg = EmailMessage()
msg["From"] = sender
msg["To"] = receiver
msg["Subject"] = subject
msg.set_content(body)

attachment = input("Enter file to attach (press Enter to skip): ").strip()

if attachment:
    try:
        with open(attachment, "rb") as file:
            file_data = file.read()
            file_name = os.path.basename(attachment)
            msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)
            print(f"✅ Attached: {file_name}")
    except FileNotFoundError:
        print(f"❌ {attachment} not found. Skipping attachment.")

print("📡 Sending Mail...")
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, app_key)
        smtp.send_message(msg)
        print("✅ Email sent successfully!")
except Exception as e:
    print("❌ Failed to send email:", e)
