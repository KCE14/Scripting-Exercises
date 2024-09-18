from cryptography.fernet import Fernet
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


server = smtplib.SMTP_SSL('smtp.gmail.com')
server.connect('smtp.gmail.com', 465)
server.ehlo()

password = "Google App Password" # A better method is to read password from txt file

server.login('Your email', password)

msg = MIMEMultipart()
msg['From'] = 'Your Name'
msg['To'] = 'Target email'
msg['Subject'] = 'Subject of Email'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))


#attach image
image = 'image file'
attachment = open(image, 'rb')

#payload
with attachment as file:
    p = MIMEImage(file.read(), _subtype="jpeg")
    p.add_header('Content-Dispostion', 'attachement', filename='image')
    msg.attach(p)

text = msg.as_string()
server.sendmail('Your email', 'Target email', text)