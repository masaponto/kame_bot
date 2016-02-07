#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import traceback
import functools

from slacker import Slacker


class Kamebot:

    def __init__(self, token='', channel='#random', title=None, initial_comment=None, filetype=None):

        if token == '':
            if os.environ.get("KAMEBOT_TOKEN") == '':
                print('environment vars KAMEBOT_TOKEN not found')
                sys.exit()
            else:
                token = os.environ.get("KAMEBOT_TOKEN")

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

    def afile(self, func):
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

    def comment(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            import io
            f = io.StringIO('')
            sys.stdout = f

            if self.title:
                print(self.title)
            if self.initial_comment:
                print(self.initial_comment)

            self.run_func(func, *args, **kwargs)

            sys.stdout = sys.__stdout__
            f.seek(0)

            self.slack.chat.post_message(self.channel, f.read(), as_user=True)
            f.close()
        return wrapper

bot = Kamebot(channel='#random')

@bot.comment
def hoge():
    print('this is a test')


if __name__ == "__main__":
    hoge()
