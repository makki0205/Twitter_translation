# -*- coding: utf-8 -*-
from api.twitter import twitter as tw
from api.translator import translation as tr

# print (tw.tweet("test03"))
# # print (tw.get_tweet())
#
# for tweet in tw.get_tweet():
#   print (tweet["text"])
#   print ('-------------------')


print(tr.ja_to_tw('お腹が空いたのでご飯を食べようと考えています!'))
