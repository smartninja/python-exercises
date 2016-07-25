#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


def main():
    sender = "YOUR.EMAIL@gmail.com"
    senders_password = "your password - don't put it on GitHub!!!"  # Don't put your password on GitHub!
    receiver = "email.to@send.to"
    subject = "Sending a SmartNinja logo"
    text = "This image comes from your Python script ;)"

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject

    image = open("smartninja.jpg", "rb")
    msg.attach(MIMEText(text))  # add text to email
    msg.attach(MIMEImage(image.read()))  # add image to email
    image.close()

    send_attachment_email(sender=sender, senders_password=senders_password, receiver=receiver, msg=msg)


def send_attachment_email(sender, senders_password, receiver, msg):
    try:
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()

        server.login(user=sender, password=senders_password)
        server.sendmail(from_addr=sender, to_addrs=receiver, msg=msg.as_string())

        server.quit()
        print("Email was successfully sent to {0}!".format(receiver))
    except Exception, e:
        print("Error!")
        print(e)

if __name__ == "__main__":
    main()
    print("END")
