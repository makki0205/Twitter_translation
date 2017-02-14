# -*- coding: utf-8 -*-
from api.twitter import twitter as tw


def nullfunc(msg):
    pass


class TweetStream(object):

    def __init__(self, screen_name):
        self.screen_name = screen_name
        self.on_tweet_func = nullfunc
        self.on_delete_func = nullfunc

    def on_tweet(self, function):
        self.on_tweet_func = function

    def on_delete(self, function):
        self.on_delete_func = function

    def middleware(self, msg):
        if 'text' in msg:
            self.on_tweet_func(msg)
            return
        if 'delete' in msg:
            self.on_delete_func(msg)
            return

    def run(self):
        tw.stream(self.screen_name, self.middleware)
