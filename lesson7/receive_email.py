#!/usr/bin/env python
# -*- coding: utf-8 -*-

import imaplib


def main():
    your_email = "YOUR.EMAIL@gmail.com"
    your_password = "your password - don't put it on GitHub!!!"  # Don't put your password on GitHub!

    receive_email(your_email=your_email, your_password=your_password)


def receive_email(your_email, your_password):
    try:
        # login to email server via IMAP
        server = imaplib.IMAP4_SSL("imap.gmail.com", "993")
        server.login(user=your_email, password=your_password)
        server.select()

        typ, data = server.search(None, "UnSeen")  # get unread messages (data has a list of message numbers)

        # loop through all message numbers
        for message_number in data[0].split():
            # important: this will mark your unread message as read!
            typ, data = server.fetch(message_number, "(RFC822)")  # get email via it's message number
            print(data[0][1])

        server.close()
        print("Email was successfully retrieved!")
    except Exception, e:
        print("Error!")
        print(e)

if __name__ == "__main__":
    main()
    print("END")
