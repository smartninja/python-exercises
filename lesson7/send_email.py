#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib


def main():
    sender = "YOUR.EMAIL@gmail.com"
    senders_password = "your password - don't put it on GitHub!!!"  # Don't put your password on GitHub!
    receiver = "email.to@send.to"
    subject = "Hello from the other side"
    text = "This comes from your Python script ;)"

    msg = "From:{0}\nTo:{1}\nSubject:{2}\n\n{3}".format(sender, receiver, subject, text)

    send_simple_email(sender=sender, senders_password=senders_password, receiver=receiver, msg=msg)


def send_simple_email(sender, senders_password, receiver, msg):
    try:
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()

        server.login(user=sender, password=senders_password)
        server.sendmail(from_addr=sender, to_addrs=receiver, msg=msg)

        server.quit()
        print "Email was successfully sent to {0}!".format(receiver)
    except Exception as e:
        print "Error!"
        print e

if __name__ == "__main__":
    main()
    print "END"
