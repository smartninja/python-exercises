#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib

sender = "your.email@gmail.com"
senders_password = "your password - don't put it on GitHub!!!"  # Don't put your password on GitHub!
receiver = "address.to@send.to"
subject = "Hello from the other side"
text = "This comes from your Python script ;)"

msg = "From:{0}\nTo:{1}\nSubject:{2}\n\n{3}".format(sender, receiver, subject, text)

try:
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()

    server.login(user=sender, password=senders_password)
    server.sendmail(from_addr=sender, to_addrs=receiver, msg=msg)

    server.quit()
    print("Email was successfully sent to {0}!".format(receiver))
except Exception, e:
    print("Error!")
    print(e)
