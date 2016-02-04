#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import traceback
import functools

from slacker import Slacker


class Kamebot:

    def __init__(self, token, channel='#random', title=None, initial_comment=None, filetype=None):
        self.slack = Slacker(token)
        self.channel = channel
        self.title = title
        self.initial_comment = initial_comment
        self.filetype = filetype

    def run_func(self, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            print('--------------------------------------------')
            print(traceback.format_exc())
            print('--------------------------------------------')

    def send_file(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            param = sys.argv
            assert(len(param) is 2)
            fname = param[1]

            if self.title is None:
                title = fname

            sys.stdout = open(fname, 'a')

            self.run_func(func, *args, **kwargs)

            sys.stdout.close()
            sys.stdout = sys.__stdout__
            self.slack.files.upload(
                fname, filename=fname, channels=self.channel, title=self.title,
                initial_comment=self.initial_comment, filetype=self.filetype)

        return wrapper

    def send_comment(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            import io
            f = io.StringIO('')
            sys.stdout = f

            self.run_func(func, *args, **kwargs)

            sys.stdout = sys.__stdout__
            f.seek(0)

            if self.title:
                print(self.title)
            if self.initial_comment:
                print(self.initial_comment)

            self.slack.chat.post_message(self.channel, f.read(), as_user=True)
            f.close()
        return wrapper

bot = Kamebot('<your-slack-api-token-goes-here>', channel='#random')

@bot.send_comment
def hoge():
    print('this is a test')
    print('this is a test')
    i = 1 + 'a'


if __name__ == "__main__":
    hoge()
