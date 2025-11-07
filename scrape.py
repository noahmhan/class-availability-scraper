from bs4 import BeautifulSoup
import cloudscraper
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os;
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env if present

# Email configuration from environment variables
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")  # Change for other providers if needed
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")  # Your email address
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")  # App password (for Gmail)
# Comma-separated list of recipients in TO_EMAIL, defaults to self if not set
TO_EMAILS = [e.strip() for e in os.getenv("TO_EMAIL", EMAIL_ADDRESS or "").split(",") if e.strip()]

def send_email(subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = ", ".join(TO_EMAILS)
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
            raise RuntimeError("Missing EMAIL_ADDRESS or EMAIL_PASSWORD environment variables.")
        if not TO_EMAILS:
            raise RuntimeError("No recipients provided. Set TO_EMAIL with one or more comma-separated emails.")

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        # send to multiple recipients
        server.sendmail(EMAIL_ADDRESS, TO_EMAILS, msg.as_string())
        server.quit()
        
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Test send email
# send_email("Test Email", "This is a test email from the class availability scraper.")
# exit()

url = "https://classes.berkeley.edu/content/2026-spring-compsci-185-001-lec-001"

scraper = cloudscraper.create_scraper()
response = scraper.get(url)
if response.status_code == 200:
    html_content = response.text
    print("Page fetched successfully.")

    soup = BeautifulSoup(html_content, 'html.parser')
    stats = soup.find(class_="stats")
    if stats:
        text = stats.get_text().split("\n")

        waitlist_count = int(text[2].split(": ")[1])
        class_capacity = int(text[3].split(": ")[1])
        waitlist_capacity = int(text[4].split(": ")[1])
        print(waitlist_count != waitlist_capacity, waitlist_count, waitlist_capacity)
        
        if class_capacity > 70:
            subject = "Class Capacity Alert"
            body = f"Class capacity for class:\n{url}\n\nClass Capacity: {class_capacity}\n\nClass size has expanded!"
            send_email(subject, body)

        if waitlist_count != waitlist_capacity:
            subject = "Class Waitlist Availability Alert"
            body = f"Waitlist update for class:\n{url}\n\nWaitlist Count: {waitlist_count}\nWaitlist Capacity: {waitlist_capacity}\n\nThere may be availability on the waitlist!"
            send_email(subject, body)
        else:
            print("Waitlist is full. No email sent.")
    else:
        print("No stats found")
        exit()
else:
    print(f"Failed to fetch page. Status code: {response.status_code}")
    exit()