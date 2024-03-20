import schedule
import time
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText

# Load environment variables
load_dotenv()


def connect_to_mongodb():
    client = MongoClient(os.getenv("MONGODB_URL"))
    db_handle = client.get_database()
    return list(db_handle['Products'].find())

def check_stock_and_send_email():
    products = connect_to_mongodb()
    low_stock_products = [product for product in products if product.get('current', 0) < product.get('reorderLevel', 0)]
    for product in low_stock_products:
        send_email(product)

def send_email(product):
    email_address = os.getenv('NODEMAILER_USER')
    email_password = os.getenv('NODEMAILER_PASS')
    recipient = os.getenv('NODEMAILER_USER')

    subject = 'Low Stock Alert'
    body = f'The stock for product {product.get("name", "Unknown")} is low. Please check.'

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = recipient

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(email_address, email_password)
            server.sendmail(email_address, recipient, msg.as_string())
    except Exception as e:
        print(f"Failed to send email: {e}")

schedule.every(10).seconds.do(check_stock_and_send_email)

print("Starting scheduled tasks...")
while True:
    schedule.run_pending()
    time.sleep(1)
