# -*- coding: utf-8 -*-
from util.settings import settings
import json
from requests_oauthlib import OAuth1Session


class Twtter(object):
    def __init__(self):
        keys = settings.get_twtter_conf()
        self.tw = OAuth1Session(keys['CONSUMER_KEY'], keys['CONSUMER_SECRET'], keys['ACCESS_TOKEN'], keys['ACCESS_SECRET'])

    def tweet(self,text):
        URL = 'https://api.twitter.com/1.1/statuses/update.json'

        # Tweetを作成
        payload = {'status': text}
        res = self.tw.post(URL, params = payload)

        # レスポンスコードを返す
        return res.text

    def get_tweet(self):
        URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

        payload = {'user_id': '1659468336'}
        res = self.tw.get(URL, params = payload)

        return json.loads(res.text)

twitter = Twtter()
