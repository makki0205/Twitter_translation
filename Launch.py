# -*- coding: utf-8 -*-
from twitter.twitter import twitter as tw

print (tw.tweet("test03"))
# print (tw.get_tweet())

for tweet in tw.get_tweet():
  print (tweet["text"])
  print ('-------------------') 
