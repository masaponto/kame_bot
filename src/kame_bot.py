#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from slacker import Slacker

class KameBot:
    def __init__(self, token, channel):
        self.slack = Slacker(token)
        self.channel = channel

    def toslack(self, func):
        import functools
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            param = sys.argv
            assert(len(param) is 2)
            fname = param[1]
            sys.stdout = open(fname, 'w')
            func(*args, **kwargs)
            sys.stdout.close()
            sys.stdout = sys.__stdout__
            self.slack.files.upload(fname, filename=fname, channels=self.channel)
        return wrapper


bot = KameBot('<your-slack-api-token-goes-here>',channel='#random')

@bot.toslack
def hoge():
    print('this is a test')


if __name__ == "__main__":
    hoge()
