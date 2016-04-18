#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import traceback
import functools
import argparse
import datetime

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

            p = argparse.ArgumentParser()
            p.add_argument('-of', '--outfile', type=str, help='out put file name',
                           default=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S.txt'))
            p.add_argument('-cm', '--comment', type=str,
                           help='comment', default=None)

            option_args = p.parse_args()
            fname = option_args.outfile

            title = self.title if self.title == None else fname
            comment = self.initial_comment if option_args.comment == None else option_args.comment

            sys.stdout = open(fname, 'a')
            self.run_func(func, *args, **kwargs)
            sys.stdout.close()
            sys.stdout = sys.__stdout__

            self.slack.files.upload(
                fname, filename=fname, channels=self.channel, title=title,
                initial_comment=comment, filetype=self.filetype)

        return wrapper

    def comment(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            import io
            sys.stdout = f
            f = io.StringIO('')

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

@bot.afile
def hoge():
    print('this is a test')


if __name__ == "__main__":
    hoge()
