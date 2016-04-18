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

    def __init__(self, token='', channel='#random', title=None, initial_comment=None, filetype=None, error_comment=''):

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
        self.error_comment = error_comment

    def run_func(self, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            print(self.error_comment)
            print('--------------------------------------------')
            print(traceback.format_exc())
            print('--------------------------------------------')

    def afile(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            p = argparse.ArgumentParser()
            p.add_argument('-of', '--outfile', type=str, help='out put file name',
                           default=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S.txt'), nargs='?')
            p.add_argument('-cm', '--comment', type=str,
                           help='comment for upload file', default=None, nargs='?')

            p.add_argument('-test', help='for test runnnig. stdout without slack', action='store_true')

            option_args = p.parse_known_args()[0]

            if option_args.test:
                self.run_func(func, *args, **kwargs)
                return wrapper

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

            p = argparse.ArgumentParser()
            p.add_argument('-test', help='test', action='store_true')
            option_args = p.parse_known_args()[0]

            if option_args.test:
                self.run_func(func, *args, **kwargs)
                return wrapper

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
@bot.afile
def hoge():
    print('this is a test')
    print('aaaaaaaaaaaaaaaaaaaa')


if __name__ == "__main__":
    hoge()
