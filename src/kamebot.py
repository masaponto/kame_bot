#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import traceback

from slacker import Slacker


class Kamebot:

    def __init__(self, token, channel='#random', title=None, initial_comment=None, filetype=None):
        self.slack = Slacker(token)
        self.channel = channel
        self.title = title
        self.initial_comment = initial_comment
        self.filetype = filetype

    def toslack(self, func):
        import functools

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            param = sys.argv
            assert(len(param) is 2)
            fname = param[1]

            if self.title is None:
                title = fname

            sys.stdout = open(fname, 'w')

            try:
                func(*args, **kwargs)
            except:
                print('--------------------------------------------')
                print(traceback.format_exc())
                print('--------------------------------------------')

            sys.stdout.close()
            sys.stdout = sys.__stdout__
            self.slack.files.upload(
                fname, filename=fname, channels=self.channel, title=self.title, initial_comment=self.initial_comment, filetype=self.filetype)
        return wrapper


bot = Kamebot('<your-slack-api-token-goes-here>', channel='#random')



@bot.toslack
def hoge():
    print('this is a test')
    i = 1 + 'a'


if __name__ == "__main__":
    hoge()
