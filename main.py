

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email_id = 'likhokapesi04@gmail.com'
receiver_email_id = ['kapesilikho39@gmail.com', 'likhokapesi135@gmail.com', 'likhokapesi@gmail.com']
password = input('Enter your password: ')
subject = 'Greetings'
msg = MIMEMultipart()
msg['From'] = sender_email_id
msg['To'] = ', ' . join(receiver_email_id)
msg['Subject'] = subject
body = 'Life Choices Academy is great. Coding is fun!!!\n'

msg.attach(MIMEText(body, 'plain'))

text = msg.as_string()
s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login(sender_email_id, password)
