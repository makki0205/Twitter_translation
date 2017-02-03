# -*- coding: utf-8 -*-
from api.twitter import twitter as tw
from api.translator import translation as tr
from service.tweetStream import TweetStream
import json

# print ( tr.ja_to_tw('こんにちは　https://t.co/h9JmioNM51'))

def tweet (msg):
    tw_text = tr.ja_to_tw(msg['text'])
    print(msg['text'] + " => " + tw_text)
    tw.tweet(tw_text)

def delete(msg):
    print('delete')
    print(msg)


ts = TweetStream('makki0205')

ts.on_tweet(tweet)
ts.on_delete(delete)


ts.run()
