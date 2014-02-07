# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.log

import email
import sys
sys.path = ['..'] + sys.path

from bonzo.server import SMTPServer


def receive_message(message):
    print("New received message: ")
    print("From: %s" % message['from'])
    print("Subject: %s" % message['subject'])
    for line in email.iterators.body_line_iterator(message):
        print(line)


if __name__ == '__main__':
    tornado.log.enable_pretty_logging()
    SMTPServer(receive_message).listen(2525)
    tornado.ioloop.IOLoop.instance().start()
