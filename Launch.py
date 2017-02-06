# -*- coding: utf-8 -*-
from api.twitter import twitter as tw
from api.translator import translation as tr
from service.tweetStream import TweetStream
from util.logging import logger
import json

# print ( tr.ja_to_tw('こんにちは　https://t.co/h9JmioNM51'))

def tweet (msg):
    if msg['text'].find('@') != -1:
        logger.info(msg['text'] + " is @tweet")
        return
    tw_text = tr.ja_to_tw(msg['text'])

    if tw_text is not None:
        logger.info(msg['text'] + " => " + tw_text)
        tw.tweet(tw_text)

def delete(msg):
    pass
logger.info("start")

hoge ="aabbccddd"

ts = TweetStream('makki0205')

ts.on_tweet(tweet)
ts.on_delete(delete)


ts.run()
